import random as rand
import dictionary_reader as dict_reader

words = dict_reader.read_from_file()  # считывание слов и подсказок для дальнейшего использования

def print_welcome():          # вывод при запуске
	print("""-------------- Добро пожаловать в "виселицу" --------------""")


def print_score(score):       # вывод счета игр
	print("Слов отгадано:", score[0], "Неудачных попыток", score[1])


def ask_for_game():           # опрос игрока о повторной игре
	print("Играть еще раз? 0 - нет, 1 - да")
	start_game = bool(input())
	print()
	return start_game


def play_game(score):         # основная логика игры 

	mistake_counter = 0
	word_index = rand.randint(0, len(words) - 1)
	word = words[word_index][0]
	hint = words[word_index][1]
	hidden_word = ["_" for i in range(len(word))]

	print("...::: Слово загадано :::...", end="\n \n")

	while (mistake_counter < 8) and ("_" in hidden_word):
		print(*hidden_word,"Подсказка:", hint)
		print("Ошибок(дебаг):", mistake_counter)
		print("Введите букву:", end=" ")
		letter = input()
		print()

		if letter in word:
			if letter not in hidden_word:
				for letter_index in range(len(word)):
					if word[letter_index] == letter:
						hidden_word[letter_index] = letter
				print("Да, такая буква есть в слове")
			else:
				print("Вы уже проверяли эту букву!")
		else:
			print("К сожалению, такой буквы нет в слове")
			mistake_counter += 1

	if mistake_counter < 8:
		score[0] += 1
		print("...::: Слово отгадано:", word ,":::...", end = "\n \n")
	else:
		score[1] -= 1
		print("...::: Вы проиграли :( Загаданное слово:", word ,":::...", end = "\n \n")

	return score
