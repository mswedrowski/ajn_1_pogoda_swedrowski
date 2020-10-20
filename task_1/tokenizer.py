import os
from config import Config




class Tokenizer():

    def __init__ (self,config:Config):
        self.config = config
        if config.ommit_abbreviations_sentence_split:
            with open(f'{config.DICTIONARIES_DIR}/abbreviations','r') as f_abb:
                self.abbreviations_list = [abb.rstrip('\n') for abb in f_abb]
        if config.avoid_splitting_phrases:
            with open(f'{config.DICTIONARIES_DIR}/phrases','r') as f_p:
                self.phrases = [p.rstrip('\n') for p in f_p]
        if config.convert_abbreviations:
            self.abbreviations_mapping = {}
            with open(f'{config.DICTIONARIES_DIR}/abbreviations_mapping','r') as f_abb_m:
                abbreviations_m_list = [abb_m.rstrip('\n') for abb_m in f_abb_m]
                for mapping in abbreviations_m_list:
                    mapping_abb, mapping_full_n = mapping.split(';')
                    self.abbreviations_mapping[mapping_abb] = mapping_full_n


    def remove_punctuation_marks(self, word):
        for p_mark in self.config.END_OF_SENTENCE_SIGNS:
            word = word.replace(p_mark,'')
        return word

    def is_end_of_sentence(self, w):
        if any(eos_sign in w for eos_sign in self.config.END_OF_SENTENCE_SIGNS):
            if self.config.ommit_abbreviations_sentence_split and self.remove_punctuation_marks(w) in self.abbreviations_list:
                return False
            else:
                return True
        return False 


    def add_sentence_separator(self, text):
        new_text = ''
        for word in text.splitlines():
            new_text += f'{word}\n'
            if self.is_end_of_sentence(word):
                new_text += f'{self.config.SENTENCE_SEPARATOR}\n'
        return new_text

    def remove_empty_lines(self, text):
        return "\n".join([ll.rstrip() for ll in text.splitlines() if ll.strip()])

    def split_by_word(self, text):
        return text.replace(' ','\n')

    def split_by_signs(self, text):
        found_changes = False
        for sign in self.config.TOKEN_SPLITTING_SIGNS:
            new_text = []
            for token in text.splitlines():
                if sign in token and token.replace(sign, '') != "":
                    new_tokens = token.split(sign)
                    new_tokens = f"\n{sign}\n".join(new_tokens)

                    new_text.append(new_tokens)
                else:
                    new_text.append(token)

            text = "\n".join(new_text)

        return text
            

    def remove_bad_signs(self,text):
        new_text = ''
        for token in text.splitlines():
            if token not in self.config.TOKEN_SPLITTING_SIGNS:
                new_text += f'{token}\n'
        return new_text

    def merge_phrases(self, text):
        new_text = ''
        text = text.splitlines()
        for i in range(len(text)):
            new_text += f'{text[i]}'
            for phrase in self.phrases:
                p_as_list = phrase.lower().split(' ')
                if i+1 <= len(text) and text[i] in p_as_list[0] and text[i+1] in p_as_list[1]:
                    new_text += f' {text[i+1]}'
                    i += 1
            new_text += '\n'
                    
        return new_text

    
    def convert_abbreviations(self, text):
        new_text=''
        for token in text.splitlines():
            if self.remove_punctuation_marks(token) in self.abbreviations_mapping.keys():
                new_text += f'{self.abbreviations_mapping[self.remove_punctuation_marks(token)]}\n'
            else:
                new_text += f'{token}\n'
        return new_text

    def tokenize(self,text:str):
        text = self.remove_empty_lines(text)

        text = self.split_by_word(text)
        text = self.remove_empty_lines(text)

        text = self.add_sentence_separator(text)

        text = self.split_by_signs(text)
        text = self.remove_empty_lines(text)

        if self.config.to_lowercase:
            text = text.lower()
        if self.config.remove_punctuation_marks:
            text =  "\n".join([self.remove_punctuation_marks(w) for w in text.splitlines()])
        if self.config.avoid_splitting_phrases:
            text = self.merge_phrases(text)
        if self.config.convert_abbreviations:
            text = self.convert_abbreviations(text)

        return text

if __name__ == "__main__":

    config = Config(ommit_abbreviations_sentence_split= True,
                    convert_abbreviations=True,
                    avoid_splitting_phrases=True,
                    remove_punctuation_marks=True,
                    to_lowercase= True,
                    ignore_bad_signs= True)

    tokenizer = Tokenizer(config)

    files = []

    for r, d, f in os.walk(config.DATA_PATH):
        for file in f:
                files.append(os.path.join(r, file))

    for f_path in files:
        with open(f_path,'r') as i:
            text = i.read()
            text = tokenizer.tokenize(text)

        f_name = f_path.split('/')[-1].replace('.txt','_res.txt')
        with open(f'task_1/results/{f_name}','w') as w_f:
            w_f.write(text)
