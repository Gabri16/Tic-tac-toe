from game import TicTacToe
from ai import ai
from helpers import the_winner_is, request_player_turn_coordinates, request_player_play_symbol
from random import randint

# defined player's/opponent's turn functions
def players_turn(game_brain, player_symbol):
    # player's turn
    print('YOUR TURN')
    players_turn = request_player_turn_coordinates(game_brain.matrix)

    # populates playing field with player's symbol with requested coordinates
    game_brain.matrix[players_turn[0]][players_turn[1]] = player_symbol
    game_brain.draw_field(game_brain.matrix)  # displaying playing field after player's turn

    # checking if there is a winning line
    return game_brain.check_winner(game_brain.matrix, player_symbol)

def opponents_turn(game_brain, opponent_symbol):
    # opponent's turn
    print("OPPONENT'S TURN")
    opponents_turn = opponent.turn(game_brain.matrix)
    game_brain.matrix[opponents_turn[0]][opponents_turn[1]] = opponent_symbol
    game_brain.draw_field(game_brain.matrix)

    return game_brain.check_winner(game_brain.matrix, opponent_symbol)


### MAIN ###
if __name__ == "__main__":

    # assignement of play symbols
    player_symbol = request_player_play_symbol()
    if player_symbol == 'O':
        opponent_symbol = 'X'
    else:
        opponent_symbol = 'O'

    # creating object 'game_brain' containing playing mechanisms
    game_brain = TicTacToe()
    # creating object 'opponent' with ai algorithms
    opponent = ai(player_symbol, opponent_symbol, 'hard') # select difficulty: 'easy', 'medium'

    # decision on who starts the game
    start_game = randint(0, 1)

    while True:  # game runs indefinitely in loop, until winner is found - then the loop is broken

        if start_game == 0:
            # player starts
            print('YOU PLAY FIRST')
            winner = players_turn(game_brain, player_symbol)
            if winner:
                break
            start_game += 1

        elif start_game == 1:
            # opponent starts
            winner = opponents_turn(game_brain, opponent_symbol)
            start_game += 1

        else:
            # player's turn
            winner = players_turn(game_brain, player_symbol)
            if winner:
                break

            # opponent's turn
            winner = opponents_turn(game_brain, opponent_symbol)
            if winner:
                break

    # announcing result of the game
    the_winner_is(winner)