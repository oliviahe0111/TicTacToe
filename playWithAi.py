# set up board with key and value pairs
board = {0: ' ', 1: ' ', 2: ' ',
         3: ' ', 4: ' ', 5: ' ',
         6: ' ', 7: ' ', 8: ' '}


# display the board
def display_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


# check if the position is taken
def space_is_free(position):
    if board[position] == ' ':
        return True
    else:
        return False


def insert_letter(letter, position):
    # can insert letter at that position
    if space_is_free(position):
        board[position] = letter
        display_board(board)
        if check_if_tie():
            print("Draw!")
            exit()
        if check_for_winner():
            if letter == 'X':
                print("AI wins!")
                exit()
            else:
                print("Player wins!")
                exit()

        return

    # position taken
    else:
        print("Position taken!")
        position = int(input("Please enter a new position:  "))
        insert_letter(letter, position)
        return


def check_for_winner():
    if board[0] == board[1] == board[2] != " ":
        return True
    elif board[3] == board[4] == board[5] != " ":
        return True
    elif board[6] == board[7] == board[8] != " ":
        return True
    elif board[0] == board[3] == board[6] != " ":
        return True
    elif board[1] == board[4] == board[7] != " ":
        return True
    elif board[2] == board[5] == board[8] != " ":
        return True
    elif board[0] == board[4] == board[8] != " ":
        return True
    elif board[6] == board[4] == board[2] != " ":
        return True
    else:
        return False


def check_rows():
    if board[0] == board[1] == board[2] != " ":
        return True
    elif board[3] == board[4] == board[5] != " ":
        return True
    elif board[6] == board[7] == board[8] != " ":
        return True
    else:
        return False


def check_columns():
    if board[0] == board[3] == board[6] != " ":
        return True
    elif board[1] == board[4] == board[7] != " ":
        return True
    elif board[2] == board[5] == board[8] != " ":
        return True
    else:
        return False


def check_diagonals():
    if board[0] == board[4] == board[8] != " ":
        return True
    elif board[6] == board[4] == board[2] != " ":
        return True
    else:
        return False


def check_if_tie():
    for key in board.keys():
        if board[key] == ' ':
            return False
    return True


# chess
player = 'O'
ai = 'X'


def player_turn():
    position = input("Choose a position from 1-9 to play for 'O': ")
    insert_letter(player, int(position)-1)
    return


def ai_turn():
    position = input("Choose a position from 1-9 to play for 'X': ")
    insert_letter(ai, int(position)-1)
    return


def play_game_ai():
    # Display initial board
    display_board(board)

    while not check_for_winner():
        ai_turn()
        player_turn()


play_game_ai()

