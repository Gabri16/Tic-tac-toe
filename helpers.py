def request_player_play_symbol():
    player_symbol = input('Select symbol (O or X): ').upper()
    while player_symbol != 'O' and player_symbol != 'X':
        player_symbol = input('Invalid char. Select player_symbol: O or X').upper()
    return player_symbol

def request_player_turn_coordinates(matrix):
    print("Your turn")

    # a lot of screaming until correct input is entered
    while True:
        try:
            player_turn_column = int(input('Select column: '))
            player_turn_row = int(input('Select row: '))

            if player_turn_column not in range(0, len(matrix)) \
                    or player_turn_row not in range(0, len(matrix)):
                print('Index out of range, select position within playing field')
            elif matrix[player_turn_row][player_turn_column] != ' ':
                print('Selected position was already populated')
            else:
                break
        except ValueError:
            print(f'Invalid input, select number between 0 - {len(matrix)}')
    return player_turn_row, player_turn_column


def the_winner_is(result):
    if result == 'DRAW':
        print('The game ended in draw')
    else:
        print(f'{result} is the winner')
