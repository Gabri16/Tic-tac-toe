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

        print('')

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

        print('')
        return

    # mechanism to check winning line of matrix length
    def check_winner(self, matrix, symbol):

        # turn counter to detected draw after all position populated
        self.turn_counter += 1

        # checking if all positions in a row are populated by the symbol
        for row in range(MATRIX_SIZE):
            winner = symbol
            for col in range(MATRIX_SIZE):
                if matrix[row][col] != symbol:
                    winner = None
                    break
            if winner:
                return winner

        # checking if all positions in a col are populated by the symbol
        for col in range(MATRIX_SIZE):
            winner = symbol
            for row in range(MATRIX_SIZE):
                if matrix[row][col] != symbol:
                    winner = None
                    break
            if winner:
                return winner

        # checking if all positions in diagonal are populated by the symbol
        for row_col in range(MATRIX_SIZE):
            winner = symbol
            if matrix[row_col][row_col] != symbol:
                winner = None
                break
        if winner:
            return winner

        # checking if all positions in antidiagonal are populated by the symbol
        for row_col in range(MATRIX_SIZE):
            winner = symbol
            if matrix[row_col][MATRIX_SIZE - 1 - row_col] != symbol:
                winner = None
                break
        if winner:
            return winner

        # in case of DRAW, when all fields where populated and no winner was found
        if self.turn_counter == MATRIX_SIZE * MATRIX_SIZE:
            return 'DRAW'

        # when no full succession was found, the function returns None
        return None
