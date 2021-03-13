class TicTacToe:
    def __init__(self):
        # Keeps player's score
        self.player_board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        # Keeps computer's score
        self.computer_board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        # Keeps both opponents' moves
        self.gaming_board = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        # Magic square
        self.winning_board = [
            [8, 1, 6],
            [3, 5, 7],
            [4, 9, 2]
        ]

    def __str__(self):
        return f"Gaming board:\n{self.gaming_board[0]}\n{self.gaming_board[1]}\n{self.gaming_board[2]}\n"

    def turn_x(self, position):
        """Adds O in the given position.
        Takes an int list as the position parameter, e.g. [1, 2].
        Returns True if O was successfully added and False if it was not."""
        if type(position) == list and len(position) == 2:
            try:
                # Check whether there is already "x" or "o" at the position:
                if type(self.gaming_board[position[0]][position[1]]) == int:
                    # Make turn, add the correct number from the winning_board to the player_board
                    self.player_board[position[0]][position[1]] = self.winning_board[position[0]][position[1]]
                    # Record the turn on the gaming board
                    self.gaming_board[position[0]][position[1]] = "X"
                    return True
            except IndexError:
                return False
        return False

    def turn_o(self, position):
        """Adds O in the given position.
        Takes an int list as the position parameter, e.g. [1, 2].
        Returns True if O was successfully added and False if it was not."""
        if type(position) == list and len(position) == 2:
            try:
                # Check whether there is already "x" or "o" at the position:
                if type(self.gaming_board[position[0]][position[1]]) == int:
                    # Make turn, add the correct number from the winning_board to the player_board
                    self.computer_board[position[0]][position[1]] = self.winning_board[position[0]][position[1]]
                    # Record the turn on the gaming board
                    self.gaming_board[position[0]][position[1]] = "O"
                    return True
            except IndexError:
                return False
        return False

    def check_game(self):
        """Checks whether the game is over and its outcome.
        Returns: int 1 - player wins
                 int 2 - computer wins
                 int 3 - draw
                 int 0 - game continues"""

        row_player, row_computer = 0, 0
        diagonal_player, diagonal_computer = 0, 0
        diagonal2_player, diagonal2_computer = 0, 0
        length = len(self.gaming_board) - 1
        # If any horizontal, vertical or diagonal line sum equals to 15, player or computer has won.
        for i in range(len(self.gaming_board)):
            # Check horizontal lines
            if sum(self.player_board[i]) == 15:
                return 1
            if sum(self.computer_board[i]) == 15:
                return 2

            # Check vertical lines, values have to be reset every cycle
            row_computer = 0
            row_player = 0
            for j in range(len(self.gaming_board)):
                row_player += self.player_board[j][i]
                row_computer += self.computer_board[j][i]

            # Check diagonal 1
            diagonal_player += self.player_board[i][i]
            diagonal_computer += self.computer_board[i][i]
            # Check diagonal 2
            diagonal2_player += self.player_board[i][length-i]
            diagonal2_computer += self.computer_board[i][length-i]

        # If player 1 wins
        if row_player == 15 or diagonal_player == 15 or diagonal2_player == 15:
            return 1
            print(row_player)
            print(diagonal_player)
            print(diagonal2_player)
        # If player 2 wins
        if row_computer == 15 or diagonal_computer == 15 or diagonal2_computer == 15:
            print(row_computer)
            print(self.computer_board[0])
            print(self.computer_board[1])
            print(self.computer_board[2])
            return 2

        # Check whether the board is full - if it is a draw
        # Inefficient for now, needs improvement
        space_left = False
        for i in range(len(self.gaming_board)):
            if space_left:
                break
            for j in range(len(self.gaming_board)):
                if type(self.gaming_board[i][j]) == int:
                    space_left = True
                    break
        # If there is no space left, return 3 for draw
        if not space_left:
            return 3

        # Game continues
        return 0
