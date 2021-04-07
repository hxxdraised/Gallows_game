import pickle


def read_words(difficulty_lvl=0):
    if difficulty_lvl == 0:
        inp = open('words/easy.pickle', 'rb')

    elif difficulty_lvl == 1:
        inp = open('words/med.pickle', 'rb')

    elif difficulty_lvl == 2:
        inp = open('words/hard.pickle', 'rb')

    words = pickle.load(inp)
    return [(w, "Нет") for w in words]


def read_rules():
    inp = open('rules.txt', 'r', encoding='utf-8')
    return inp
