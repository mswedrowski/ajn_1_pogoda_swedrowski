class Config():
    def __init__(self,
                ommit_abbreviations_sentence_split = False,
                convert_abbreviations = False,
                avoid_splitting_phrases = False,
                remove_punctuation_marks = False,
                to_lowercase = False,
                ignore_bad_signs = False):

        self.ommit_abbreviations_sentence_split = ommit_abbreviations_sentence_split
        self.convert_abbreviations = convert_abbreviations
        self.avoid_splitting_phrases = avoid_splitting_phrases
        self.remove_punctuation_marks = remove_punctuation_marks
        self.to_lowercase = to_lowercase,
        self.ignore_bad_signs = ignore_bad_signs

        self.DATA_PATH = 'task_1/test_data/'
        self.DICTIONARIES_DIR = 'task_1/tokenizer_data/'
        self.SENTENCE_SEPARATOR = '<eos>'
        self.END_OF_SENTENCE_SIGNS = ['!','.','?']
        self.BAD_SIGNS_AS_TOKEN = ['-','/','–']