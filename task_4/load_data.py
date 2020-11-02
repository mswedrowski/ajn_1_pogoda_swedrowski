import os
import xml.etree.ElementTree as ET
from lxml import etree


# Get a file path and return tulpe (words:List,part of speech:List) for a file
def load_file(file):
    print(f" Loading file -  {file}")
    with open(file, 'r', encoding="utf-8") as xml_file:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        words = []
        pos = []
        for chunk in root:
            for sentence in chunk:
                for token in sentence:
                    if token.tag == 'tok':
                        words.append(token[1][0].text)
                        pos.append(token[1][1].text)
        return words, pos, file.split("/")[-1].split("_")[0]


# Read all files in a given dir and return xml's
def read_files(dir_path: str):
    words = []
    labels = []
    for r, d, f in os.walk(dir_path):
        for file_name in f:
            file_path = os.path.join(dir_path, file_name)
            w, p, f = load_file(file_path)
            words.append((w, p))
            labels.append(f)
    return words, labels


# if __name__ == '__main__':
#     words, pos = load_file('data/test/cmc/Albania_10730.txt')
