from random import randint

class ai:
    def __init__(self, player_symbol, ai_symbol, difficulty):
        self.difficulty = difficulty
        self.symbol = ai_symbol
        self.player_symbol = player_symbol

    def turn(self, matrix):
        if self.difficulty == 'easy':
            return self.play_easy(matrix)
        if self.difficulty == 'medium':
            return self.play_medium(self.player_symbol, matrix)

    # primitive algorithm based on random placement of symbols into blank spots in the play field
    def play_easy(self, matrix):
        turn = ()

        # while loop until random decision is valid
        while not turn:
            for row in range(0, len(matrix)):
                for column in range(0, len(matrix[row])):

                    # search for blank spot in the playing field
                    if matrix[row][column] == ' ':

                        # randomness generator, based on length of matrix
                        # there is a lower chance of fullfilling the condition below for matrices of bigger size,
                        # thus higher chance to populate distant corner of the playing field
                        if randint(0, len(matrix)) == 1:
                            turn = (row, column)
                            return turn


    # this algorithm regards player's turn (symbol) and tries to block him before full succession line is created
    # if no blocking was deemed necessary, computers marks random spot
    # honestly, does not work very well as it regards creation of lines only in one direction
    def play_medium(self, symbol, matrix):
        turn = ()

        # finds an occurence of 'symbol' in the matrix and starts checking
        for row in range(0, len(matrix)):
            for column in range(0, len(matrix[row])):
                if matrix[row][column] == symbol:
                    suceeding_symbols = 1
                    # check if almost full row exists, if so, block it
                    while True:
                        try:
                            if matrix[row][column + suceeding_symbols] == symbol:
                                suceeding_symbols += 1
                            else:
                                break
                        except IndexError:
                            break

                    if suceeding_symbols == len(matrix) - 1:
                        print('i see two in row')
                        try:
                            if matrix[row][column + suceeding_symbols] == ' ':
                                turn = (row, column + suceeding_symbols)
                                return turn
                        except IndexError: # blunt way how to avoid IndexErrors
                            pass
                    else:
                        suceeding_symbols = 1

                        # check if almost full column exists
                        while True:
                            try:
                                if matrix[row + suceeding_symbols][column] == symbol:
                                    suceeding_symbols += 1
                                else:
                                    break
                            except IndexError:
                                break

                        if suceeding_symbols == len(matrix) - 1:
                            print('i see two in col')
                            try:
                                if matrix[row + suceeding_symbols][column] == ' ':
                                    turn = (row + suceeding_symbols, column)
                                    return turn
                            except IndexError:
                                pass
                        else:
                            suceeding_symbols = 1

                            # check if almost full row in diagonal exists
                            while True:
                                try:
                                    if matrix[row + suceeding_symbols][column + suceeding_symbols] == symbol:
                                        suceeding_symbols += 1
                                    else:
                                        break
                                except IndexError:
                                    break

                            if suceeding_symbols == len(matrix) - 1:
                                print('i see two in diagonal')
                                try:
                                    if matrix[row + suceeding_symbols][column + suceeding_symbols] == ' ':
                                        turn = (row + suceeding_symbols, column + suceeding_symbols)
                                        return turn
                                except IndexError:
                                    pass
                            else:
                                suceeding_symbols = 1

                                # check if almost full row in anti-diagonal exists
                                while True:
                                    try:
                                        if column - suceeding_symbols != -1:
                                            if matrix[row + suceeding_symbols][column - suceeding_symbols] == symbol:
                                                suceeding_symbols += 1
                                            else:
                                                break
                                        else:
                                            break
                                    except IndexError:
                                        break

                                if suceeding_symbols == len(matrix) - 1:
                                    print('i see two in antidiagonal')
                                    try:
                                        if matrix[row + suceeding_symbols][column - suceeding_symbols] == ' ':
                                            turn = (row + suceeding_symbols, column - suceeding_symbols)
                                            return turn
                                    except IndexError:
                                        pass
                                else:
                                    suceeding_symbols = 1

        # algo from easy difficulty - puts symbol into blank space if no blocking was neccessary
        while not turn:
            for row in range(0, len(matrix)):
                for column in range(0, len(matrix[row])):
                    if matrix[row][column] == ' ':
                        if randint(0, len(matrix)) == 1:
                            turn = (row, column)
                            return turn