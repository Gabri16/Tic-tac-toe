from random import randint

class ai:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def turn(self, matrix):
        if self.difficulty == 'easy':
            return self.play_easy(matrix)

    # primitive algorithm based on random placement of symbols into blank spots in the play field
    def play_easy(self, matrix):
        turn = []

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
                            turn = [row, column]
                            return turn

    # TODO: prepare some more sophisticated algorithm for computer opponent
    def play_hard(self, matrix):
        return