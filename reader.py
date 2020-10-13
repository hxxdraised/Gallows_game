def read_words(difficulty_lvl = 0): # Cчитывание словаря
    
    if difficulty_lvl == 0:
        inp = open('words/easy.txt', 'r', encoding='utf-8')

    elif difficulty_lvl == 1:
        inp = open('words/med.txt', 'r', encoding='utf-8')

    elif difficulty_lvl == 2:
        inp = open('words/hard.txt', 'r', encoding='utf-8')

    words = []
    for line in inp:
        words.append(line.split())
    return(words)

def read_rules():

    inp = open('rules.txt', 'r', encoding='utf-8')
    return(inp)
