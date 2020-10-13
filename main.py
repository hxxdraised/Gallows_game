import game_manager as game

game.print_welcome()
score = [0, 0]
start_game = True

while start_game:
	score = game.play_game(score)
	game.print_score(score)
	start_game = game.ask_for_game()