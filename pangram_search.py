'''
Скприпт проверяет сколько символов алфавита содержат предложения.
Панграммы - осмысленные фразы-панграммы, в которых все буквы алфавита встречаются ровно один раз. 
В нашем случае, мы ищем в текстовом файле предложения, в которых представлено максимальное количество букв алфавита.
Для работы требуются модели русского языка: https://spacy.io/models/ru
Пример установки модуля: python -m spacy download ru_core_news_sm
'''
import os
import spacy
from spacy.language import Language
import pdb
import string


nlp = spacy.load("ru_core_news_lg")


@Language.component("custom_sentence_boundary")
def set_custom_sentence_boundary(doc):
    for token in doc[:-1]:
        if token.text == '\n':
            doc[token.i + 1].is_sent_start = True
    return doc


nlp.add_pipe("custom_sentence_boundary", before="parser")


def is_pangram(sentence):
    alphabet = set("йцукенгшщзхъфывапролджэячсмитьбюё")
    sentence = ''.join(filter(str.isalpha, sentence.lower()))
    sentence = sentence.translate(str.maketrans("", "", string.punctuation))
    return set(sentence) == alphabet


def count_alphabet_chars(sentence):
    chars = set(filter(str.isalpha, sentence.lower()))
    return len(chars)


filename = input("Введите имя файла: ")

if not os.path.exists(filename):
    print(f"Файл {filename} не найден")
    exit()

print(f"Файл {filename} найден")

with open(filename, "r", encoding="utf-8") as file:
    text = file.read()

doc = nlp(text)

pangrams = []

for sent in doc.sents:
    sentence = sent.text.strip()
    if len(sentence) < 30:
        continue
    if is_pangram(sentence):
        num_chars = count_alphabet_chars(sentence)
        print(f"Предложение: '{sentence}'")
        print(f"Количество уникальных символов алфавита: {num_chars}")
        print("🎉 Это панграмма! 🎉\n")
        pangrams.append(sentence)
    else:
        num_chars = count_alphabet_chars(sentence)
        print(f"Предложение: '{sentence}'")
        print(f"Количество уникальных символов алфавита: {num_chars}")
        print("👎 Это не панграмма. 👎\n")

print("Найдены следующие панграммы:")
for pangram in pangrams:
    print(pangram)
