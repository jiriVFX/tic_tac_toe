from tic_tac_toe import TicTacToe

# Read the ascii art
with open("ascii.txt", "r") as file:
    ascii_art = file.read()

coordinates = {
    "1": [0, 0],
    "2": [0, 1],
    "3": [0, 2],
    "4": [1, 0],
    "5": [1, 1],
    "6": [1, 2],
    "7": [2, 0],
    "8": [2, 1],
    "9": [2, 2]
}

gaming_board_pos = """
 Positions
 1 | 2 | 3
-----------
 4 | 5 | 6
-----------
 7 | 8 | 9  
"""

print(ascii_art)
print(gaming_board_pos)
new_game = TicTacToe()

for i in range(0, 9):
    # Handle player moves
    if i % 2 == 0:
        while True:
            position = input("Player 1(X) coords: ")
            if position in coordinates:
                if not new_game.turn_x(coordinates[position]):
                    print("Position is already filled. Choose a different position.")
                else:
                    break
            else:
                print("Not a valid position, type only numbers 1 to 9.")
    else:
        while True:
            position = input("Player 2(0) coords: ")
            if position in coordinates:
                if not new_game.turn_o(coordinates[position]):
                    print("Position is already filled. Choose a different position.")
                else:
                    break
            else:
                print("Not a valid position, type only numbers 1 to 9.")

    # Gaming board update
    gaming_board = f""" 
 {new_game.gaming_board[0][0]} | {new_game.gaming_board[0][1]} | {new_game.gaming_board[0][2]}
-----------
 {new_game.gaming_board[1][0]} | {new_game.gaming_board[1][1]} | {new_game.gaming_board[1][2]}
-----------
 {new_game.gaming_board[2][0]} | {new_game.gaming_board[2][1]} | {new_game.gaming_board[2][2]}"""

    # Check the game state
    outcome = new_game.check_game()
    if outcome == 0:
        print(gaming_board)
    elif outcome == 3:
        print(gaming_board)
        print("It's a draw!")
        break
    elif outcome == 1:
        print(gaming_board)
        print("Player 1(X) wins!")
        break
    elif outcome == 2:
        print(gaming_board)
        print("Player 2(O) wins!")
        break
