MATRIX_SIZE = 3

class TicTacToe():

    def __init__(self):
        self.matrix = self.create_matrix(MATRIX_SIZE)
        self.draw_field(self.matrix)
        self.turn_counter = 0

    
    # creates multidimensional list (matrix) 'size' * 'size'
    def create_matrix(self, size):
        matrix = []

        # When I tried to initialize multidimensional list as below, it did not work as expected

        # cols = [' ' for columns in range(0, size)]
        # matrix = [cols for rows in range(0, size)]

        # this way, Python generates a list of three references to the same list of strings
        # this solution worked (https://medium.com/evenbit/some-odd-behavior-with-lists-in-python-51e8c0daf5e2):
        for i in range(size):
            cols = [' '] * size
            matrix.append(cols)

        return matrix

    
    # visualisation of playing field in the console
    def draw_field(self, matrix):

        # preparation of column and row labels
        column_labels = [f' {column} ' for column in range(0, len(matrix))]
        row_labels = [row for row in range(0, len(matrix))]

        # formatting and printing of column labels
        print('  ', end='')
        print(*column_labels)

        for row in range(0, len(matrix)):
            # formatting and printing of row labels
            print(row_labels[row], end='  ')

            for column in range(0, len(matrix[row])):
                print(matrix[row][column], end='')

                # separator of columns, except the last column
                if column != len(matrix) - 1:
                    print(' | ', end='')
            print('')

            # generates line separator of appropriate length after each row (except after the last row)
            if row != len(matrix) - 1:
                print(f'  {"----" * (len(matrix) - 1)}---')
        return

    
    # mechanism to check winning line of matrix length
    def check_winner(self, matrix, symbol):

        self.turn_counter += 1
        if self.turn_counter >= MATRIX_SIZE * MATRIX_SIZE:
            return 'DRAW'

        # counter of suceeding symbols; game ends when matrix length number of succeeding symbols is found
        suceeding_symbols = 1

        # this function checks all detected symbols in all directions
        # finds an occurence of 'symbol' in the matrix and starts checking
        for row in range(0, len(matrix)):
            for column in range(0, len(matrix[row])):
                if matrix[row][column] == symbol:

                    # check if full row exists
                    while True:
                        try:
                            if matrix[row][column + suceeding_symbols] == symbol:
                                suceeding_symbols += 1
                            else:
                                break
                        except IndexError:
                            break

                    if suceeding_symbols == len(matrix):
                        # when winning succesion was detected, the function returns winning symbol
                        return symbol
                    else:
                        suceeding_symbols = 1

                        # check if full column exists
                        while True:
                            try:
                                if matrix[row + suceeding_symbols][column] == symbol:
                                    suceeding_symbols += 1
                                else:
                                    break
                            except IndexError:
                                break

                        if suceeding_symbols == len(matrix):
                            return symbol
                        else:
                            suceeding_symbols = 1

                            # check if full row in diagonal exists
                            while True:
                                try:
                                    if matrix[row + suceeding_symbols][column + suceeding_symbols] == symbol:
                                        suceeding_symbols += 1
                                    else:
                                        break
                                except IndexError:
                                    break

                            if suceeding_symbols == len(matrix):
                                return symbol
                            else:
                                suceeding_symbols = 1

                                # check if full row in anti-diagonal exists
                                while True:
                                    try:
                                        if matrix[row + suceeding_symbols][column - suceeding_symbols] == symbol:
                                            suceeding_symbols += 1
                                        else:
                                            break
                                    except IndexError:
                                        break

                                if suceeding_symbols == len(matrix):
                                    return symbol
                                else:
                                    suceeding_symbols = 1

        # when no full succession was found, the function returns None
        return None