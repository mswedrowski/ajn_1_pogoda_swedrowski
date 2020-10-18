import os
from config import Config

END_OF_SENTENCE_SIGNS = ['!','.','?']


class Tokenizer():

    def __init__ (self,config:Config):
        self.config = config

    def is_end_of_sentence(self, w):
        if any(eos_sign in w for eos_sign in END_OF_SENTENCE_SIGNS):
            return True
        return False 


    def add_sentence_separator(self, text):
        text = ''
        for word in text.splitlines():
            if self.is_end_of_sentence(word):
                text += self.SENTENCE_SEPARATOR
            else:
                text += f'{word}\n'
        return text

    def remove_empty_lines(self,text):
        return "\n".join([ll.rstrip() for ll in text.splitlines() if ll.strip()])

    def split_by_word(self,text):
        if self.config.ommit_abbreviations_linesplit:
            splitted_text= text.replace(' ','\n')
        else:
            return text.replace(' ','\n')

    def tokenize(self,text:str):
        text = self.remove_empty_lines(text)
        return text

if __name__ == "__main__":

    files = []


    for r, d, f in os.walk(DATA_PATH):
        for file in f:
                files.append(os.path.join(r, file))

    for f_path in files:
        with open(f_path,'r') as i:
            text = i.read()
            text = tokenize(text)
            text = split_by_word(text)
            print(text)
