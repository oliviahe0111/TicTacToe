import playWithAi
# ----Global Variables -----

# If game is still going
game_still_going = True

# Who won? Or tie?
winner = None

# Who's turn is it
first_player = "Hi"
second_player = "O"
current_player = None

# empty game board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]


# play the game of tic-tac-toe
def play_game_human():

    global first_player, second_player, current_player
    first_player = input("Please input first player's name: ")
    second_player = input("Please input second player's name: ")
    current_player = first_player

    # Display initial board
    display_board()

    # While the game is still going continue loop
    while game_still_going:
        # handle a single turn of an arbitrary player
        handle_turn(current_player)

        # check if the game has ended
        check_if_game_over()

        # flip to the other player
        flip_player()

    # The game has ended
    if winner == "X" or winner == "O":
        if winner == "X":
            print(str(first_player) + " won.")
        else:
            print(str(second_player) + " won.")

    elif winner is None:
        print("Tie.")


def play_game():
    chosen = False
    while not chosen:
        game_choice = input("Type '1' to enter a two-player game; Type '2' to compete with an AI: ")
        if game_choice == "1":
            chosen = True
            play_game_human()
        elif game_choice == "2":
            chosen = True
            playWithAi.play_game_ai()
        else:
            print("Invalid input. Please try again!")


# display the board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


# handle a single turn of an arbitrary player
def handle_turn(player):
    print(str(player) + "'s turn.")
    position = input("Choose a position from 1-9: ")

    valid = False
    while not valid:
        # Check invalid input
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid input. Choose a new position from 1-9: ")

        position = int(position) - 1

        # Check over-written position
        if board[position] == "-":
            valid = True
        else:
            position = input("Position taken. Choose a open position from 1-9: ")

    if str(player) == str(first_player):
        board[position] = "X"
    else:
        board[position] = "O"

    display_board()


# check if the game has ended
def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():
    # Set up global variables
    global winner

    # check rows
    row_winner = check_rows()
    # check columns
    column_winner = check_columns()
    # check diagonals
    diagonal_winner = check_diagonals()

    # Get the winner
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None

    return


# return row winner if win
def check_rows():
    # Set up global variables
    global game_still_going

    # check if any of the rows have all the same value (and is not empty)
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    # If any row has a match, flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    # Return the winner (X or O)
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


# return column-winner if wins
def check_columns():
    # Set up global variables
    global game_still_going

    # check if any of the columns have all the same value (and is not empty)
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    # If any column has a match, flagthat there is a win
    if column_1 or column_2 or column_3:
        game_still_going = False
    # Return the winer (X or O)
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return


def check_diagonals():
    # Set up global variables
    global game_still_going

    # check if any of the diagonals have all the same value (and is
    # not empty)
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[6] == board[4] == board[2] != "-"

    # If any diagonal has a match, flag that there is a win
    if diagonal_1 or diagonal_2:
        game_still_going = False
    # Return the winner (X or O)
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]
    return


def check_if_tie():
    global game_still_going

    if "-" not in board:
        game_still_going = False
    return


def flip_player():
    # global varaibles we need
    global current_player
    # if the current player was X, then change it to O
    if current_player == first_player:
        current_player = second_player
    # if the current player was O, then change it to X
    elif current_player == second_player:
        current_player = first_player
    return


play_game()


# board
# display
# play game
# handle a turn
# check win
# check rows
# check columns
# check diagonals
# check tie
# flip players

