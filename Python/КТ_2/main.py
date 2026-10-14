import game


game.start_game()

while game.is_playing():
    game.play_turn()

game.finish_game()
