import os

DATA_PATH = 'tokenizer_data/'
SENTENCE_SEPARATOR = '<eos>'
END_OF_SENTENCE_SIGNS = ['!','.','?']


files = []

def remove_empty_lines(text):
    return "\n".join([ll.rstrip() for ll in text.splitlines() if ll.strip()])

def split_by_word(text):
    return text.replace(' ','\n')


def is_end_of_sentence(w):
    if any(eos_sign in w for eos_sign in END_OF_SENTENCE_SIGNS):
        return True
    return False 


def add_sentence_separator(text):
    text = ''
    for word in text.splitlines():
        if is_end_of_sentence(word):
            text += SENTENCE_SEPARATOR
        else:
            text += f'{word}\n'
    return text


def tokenize(text):
    text = remove_empty_lines(text)
    return text

for r, d, f in os.walk(DATA_PATH):
        for file in f:
                files.append(os.path.join(r, file))

for f_path in files:
    with open(f_path,'r') as i:
        text = i.read()
        text = tokenize(text)
        text = split_by_word(text)
        print(text)