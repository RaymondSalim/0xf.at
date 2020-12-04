import hashlib


def loop(word_list):
    for el in word_list:
        for el2 in word_list:
            text = hashlib.md5((el + el2).encode())
            if (text.hexdigest() == '2c0372f626a9029084f8c7242ac2587e'):
                print(text)
                return

word_list = []
with open('wordlist.txt', 'r') as f:
    for el in f:
        word_list.append(el.rstrip())

loop(word_list)
