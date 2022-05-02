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
        if self.difficulty == 'hard':
            return self.play_hard(self.player_symbol, self.symbol, matrix)


    ### GAME DIFFICULTIES ###
    def play_easy(self, matrix):
        return self.populate_random_blank(matrix)

    # this algorithm initially tries to block player's moves, then places symbol randomly to blank space
    def play_medium(self, symbol, matrix):

        if self.blocking_strategy(symbol, matrix):
            return self.blocking_strategy(symbol, matrix)
        else:
            return self.populate_random_blank(matrix)

    # this algorithm initially tries to win and if not possible, then blocks player
    # if there is no danger of other player winning, randomly places symbol to blank space
    def play_hard(self, player_symbol, ai_symbol, matrix):

        try_win = self.try_win(ai_symbol, matrix)
        if try_win:
            return try_win

        blocking_strategy = self.blocking_strategy(player_symbol, matrix)
        if blocking_strategy:
            return blocking_strategy
        else:
            return self.populate_random_blank(matrix)


    ### PLAYING STRATEGIES ###
    def populate_random_blank(self, matrix):
        turn = ()

        # while loop until random decision is valid
        while not turn:
            # search for blank spot in the playing field
            for row in range(0, len(matrix)):
                for column in range(0, len(matrix[row])):
                    if matrix[row][column] == ' ':
                        # randomness generator, based on length of matrix
                        # there is a lower chance of fullfilling the condition below for matrices of bigger size,
                        # thus higher chance to populate distant corner of the playing field
                        if randint(0, len(matrix)) == 1:
                            turn = (row, column)
                            return turn

    def blocking_strategy(self, symbol, matrix):
        turn = ()

        # checks rows for player's moves
        for row in range(len(matrix)):
            player_populated_fields = 0
            for col in range(len(matrix)):
                if matrix[row][col] == symbol:
                    player_populated_fields += 1
            # if row is almost fully populated (except for one field), find 'blank' space and populate it
            if player_populated_fields == len(matrix) - 1:
                for col in range(len(matrix)):
                    if matrix[row][col] == ' ':
                        turn = (row, col)
                        return turn

        # checks cols for player's moves
        for col in range(len(matrix)):
            player_populated_fields = 0
            for row in range(len(matrix)):
                if matrix[row][col] == symbol:
                    player_populated_fields += 1
            # if col is almost fully populated (except for one field), find 'blank' space and populate it
            if player_populated_fields == len(matrix) - 1:
                for row in range(len(matrix)):
                    if matrix[row][col] == ' ':
                        turn = (row, col)
                        return turn

        # checks diagonal for player's moves
        player_populated_fields = 0
        for row_col in range(len(matrix)):
            if matrix[row_col][row_col] == symbol:
                player_populated_fields += 1
        # if diagonal is almost fully populated (except for one field), find 'blank' space and populate it
        if player_populated_fields == len(matrix) - 1:
            for row_col in range(len(matrix)):
                if matrix[row_col][row_col] == ' ':
                    turn = (row_col, row_col)
                    return turn

        # checks antidiagonal for player's moves
        player_populated_fields = 0
        for row_col in range(len(matrix)):
            if matrix[row_col][len(matrix) - 1 - row_col] == symbol:
                player_populated_fields += 1
        # if antidiagonal is almost fully populated (except for one field), find 'blank' space and populate it
        if player_populated_fields == len(matrix) - 1:
            for row_col in range(len(matrix)):
                if matrix[row_col][len(matrix) - 1 - row_col] == ' ':
                    turn = (row_col, len(matrix) - 1 - row_col)
                    return turn

        # if nothing to block was found, return None
        return None

    def try_win(self, ai_symbol, matrix):
        turn = ()

        # checks rows for ai moves
        for row in range(len(matrix)):
            ai_populated_fields = 0
            for col in range(len(matrix)):
                if matrix[row][col] == ai_symbol:
                    ai_populated_fields += 1
            # if row contains almost all ai symbols, find 'blank' space and populate it
            if ai_populated_fields == len(matrix) - 1:
                for col in range(len(matrix)):
                    if matrix[row][col] == ' ':
                        turn = (row, col)
                        return turn

        # checks cols for ai moves
        for col in range(len(matrix)):
            ai_populated_fields = 0
            for row in range(len(matrix)):
                if matrix[row][col] == ai_symbol:
                    ai_populated_fields += 1
            # if col is almost fully populated (except for one field), find 'blank' space and populate it
            if ai_populated_fields == len(matrix) - 1:
                for row in range(len(matrix)):
                    if matrix[row][col] == ' ':
                        turn = (row, col)
                        return turn

        # checks diagonal for ai moves
        ai_populated_fields = 0
        for row_col in range(len(matrix)):
            if matrix[row_col][row_col] == ai_symbol:
                ai_populated_fields += 1
        # if diagonal is almost fully populated (except for one field), find 'blank' space and populate it
        if ai_populated_fields == len(matrix) - 1:
            for row_col in range(len(matrix)):
                if matrix[row_col][row_col] == ' ':
                    turn = (row_col, row_col)
                    return turn

        # checks antidiagonal for player's moves
        ai_populated_fields = 0
        for row_col in range(len(matrix)):
            if matrix[row_col][len(matrix) - 1 - row_col] == ai_symbol:
                ai_populated_fields += 1
        # if antidiagonal is almost fully populated (except for one field), find 'blank' space and populate it
        if ai_populated_fields == len(matrix) - 1:
            for row_col in range(len(matrix)):
                if matrix[row_col][len(matrix) - 1 - row_col] == ' ':
                    turn = (row_col, len(matrix) - 1 - row_col)
                    return turn

        # if nothing to win was found, return None
        return None
