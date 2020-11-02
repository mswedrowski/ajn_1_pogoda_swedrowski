import os

from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import classification_report

from task_4.load_data import read_files
from task_4.config import *


def filter_part_of_speech(words, part_of_speech):
    new_docs = []
    for doc in words:
        word_list = doc[0]
        pos_list = doc[1]
        new_doc_desc = []
        for doc_i in range(len(pos_list)):
            if part_of_speech == POS_NOUN:
                if any(pos_list[doc_i].startswith(tag) for tag in NOUN_TAGS):
                    new_doc_desc.append(word_list[doc_i])
            elif part_of_speech == POS_VERB:
                if any(pos_list[doc_i].startswith(tag) for tag in VERB_TAGS):
                    new_doc_desc.append(word_list[doc_i])
            else:
                if any(pos_list[doc_i].startswith(tag) for tag in ADJECTIVE_TAGS):
                    new_doc_desc.append(word_list[doc_i])
        new_docs.append(new_doc_desc)
    return new_docs


def preprocess_data(X_train, y_train, X_test, y_test, pos, ):
    encoder = LabelEncoder()
    count_vectorizer = CountVectorizer()
    filtered_words_train = filter_part_of_speech(X_train, pos)
    filtered_words_test = filter_part_of_speech(X_test, pos)

    x_train = [' '.join(x) for x in filtered_words_train]
    x_test = [' '.join(x) for x in filtered_words_test]

    X_train = count_vectorizer.fit_transform(x_train)
    y_train = encoder.fit_transform(y_train)
    X_test = count_vectorizer.transform(x_test)
    y_test = encoder.transform(y_test)
    return X_train, y_train, X_test, y_test


if __name__ == '__main__':
    tagger = 'wcrft2'
    train_dir_path = os.path.join(TRAIN_DATA_DIR, tagger)
    test_dir_path = os.path.join(TEST_DATA_DIR, tagger)

    train_words, train_labels = read_files(train_dir_path)
    test_words, test_labels = read_files(test_dir_path)
    X_train, y_train, X_test, y_test = preprocess_data(train_words, train_labels, test_words, test_labels, POS_NOUN)

    clf = MultinomialNB()
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)

    print(classification_report(y_true=y_test, y_pred=y_pred))
