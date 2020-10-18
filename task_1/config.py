class Config():
    def __init__(self,
                ommit_abbreviations_linesplit = False,
                convert_abbreviations = False,
                avoid_splitting_phrases = False,
                remove_punctuation_marks = False):

        self.ommit_abbreviations_linesplit = ommit_abbreviations_linesplit
        self.convert_abbreviations = convert_abbreviations
        self.avoid_splitting_phrases = avoid_splitting_phrases
        self.remove_punctuation_marks = remove_punctuation_marks
        self.DATA_PATH = 'test_data/'
        self.DICTIONARIES_PATH = 'tokenizer_data/'
        self.SENTENCE_SEPARATOR = '<eos>'