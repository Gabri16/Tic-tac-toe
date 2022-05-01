from game import TicTacToe
from ai import ai
from helpers import the_winner_is, request_player_turn_coordinates, request_player_play_symbol

if __name__ == "__main__":

    # assigning playing symbols
    player_symbol = request_player_play_symbol()
    if player_symbol == 'O':
        opponent_symbol = 'X'
    else:
        opponent_symbol = 'O'

    # creates object 'game_brain' containing playing mechanisms
    game_brain = TicTacToe()

    # creates object 'opponent' with ai algorithms
    opponent = ai(player_symbol, opponent_symbol, 'medium') # select difficulty: 'easy', 'medium', 'hard'

    # game runs indefinitely in loop, until winner is found - then the loop is broken
    while True:
        # player's turn
        players_turn = request_player_turn_coordinates(game_brain.matrix)

        # populates playing field with player's symbol with requested coordinates
        game_brain.matrix[players_turn[0]][players_turn[1]] = player_symbol
        game_brain.draw_field(game_brain.matrix) # displaying playing field after player's turn

        # checking if there is a winning line
        winner = game_brain.check_winner(game_brain.matrix, player_symbol)
        if winner:
            break

        # opponent's turn
        print("OPPONENT'S TURN")
        opponents_turn = opponent.turn(game_brain.matrix)
        game_brain.matrix[opponents_turn[0]][opponents_turn[1]] = opponent_symbol
        game_brain.draw_field(game_brain.matrix)

        winner = game_brain.check_winner(game_brain.matrix, opponent_symbol)
        if winner:
            break

    # announces result of the game according return value from 'game_brain.check_winner' function
    the_winner_is(winner)