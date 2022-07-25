# set up board with key and value pairs
board = {0: ' ', 1: ' ', 2: ' ',
         3: ' ', 4: ' ', 5: ' ',
         6: ' ', 7: ' ', 8: ' '}
# board = {1: ' ', 2: ' ', 3: ' ',
#          4: ' ', 5: ' ', 6: ' ',
#          7: ' ', 8: ' ', 9: ' '}


# display the board
def display_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])
    # print(board[1] + " | " + board[2] + " | " + board[3])
    # print(board[4] + " | " + board[5] + " | " + board[6])
    # print(board[7] + " | " + board[8] + " | " + board[9])


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
        insert_letter(letter, position-1)
        return


def check_for_winner():
    # if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
    #     return True
    # elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
    #     return True
    # elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
    #     return True
    # elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
    #     return True
    # elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
    #     return True
    # elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
    #     return True
    # elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
    #     return True
    # elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
    #     return True
    # else:
    #     return False
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


def check_which_player_won(chess):
    # if board[1] == board[2] and board[1] == board[3] and board[1] == mark:
    #     return True
    # elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
    #     return True
    # elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
    #     return True
    # elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
    #     return True
    # elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
    #     return True
    # elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
    #     return True
    # elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
    #     return True
    # elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
    #     return True
    # else:
    #     return False
    if board[0] == board[1] == board[2] == chess:
        return True
    elif board[3] == board[4] == board[5] == chess:
        return True
    elif board[6] == board[7] == board[8] == chess:
        return True
    elif board[0] == board[3] == board[6] == chess:
        return True
    elif board[1] == board[4] == board[7] == chess:
        return True
    elif board[2] == board[5] == board[8] == chess:
        return True
    elif board[0] == board[4] == board[8] == chess:
        return True
    elif board[6] == board[4] == board[2] == chess:
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
    best_score = -800
    best_move = 0
    for key in board.keys():
        if board[key] == ' ':
            board[key] = ai
            # calculate the score for each open spot
            score = minimax(board, 0, False)
            # reverse the spot to empty and try another spot
            board[key] = ' '
            # update best move
            if score > best_score:
                best_score = score
                best_move = key

    insert_letter(ai, best_move)
    return


# minimax functions need a current board state and the depth and also know if it's maximizing or minimizing
def minimax(try_board,depth, is_maximizing):
    # the minimax function is favouring the AI; will reward the move which makes the AI wins more score
    if check_which_player_won(ai):
        return 100
    elif check_which_player_won(player):
        return -100
    elif check_if_tie():
        return 0

    if is_maximizing:
        best_score = -800
        for key in try_board.keys():
            if try_board[key] == ' ':
                try_board[key] = ai
                # calculate the score for each open spot
                score = minimax(try_board, depth + 1, False)
                # reverse the spot to empty and try another spot
                try_board[key] = ' '
                # update best move
                if score > best_score:
                    best_score = score

        return best_score
    else:
        best_score = 800
        for key in try_board.keys():
            if try_board[key] == ' ':
                try_board[key] = player
                score = minimax(try_board, depth + 1, True)
                try_board[key] = ' '
                if score < best_score:
                    best_score = score
        return best_score


def play_game_ai():
    # Display initial board
    display_board(board)

    chosen = False
    while not chosen:
        first_player = input("Type '1' to play first; Type '2' to let the AI play first: ")
        if first_player == '1':
            chosen = True
            while not check_for_winner():
                player_turn()
                print("\n")
                ai_turn()
        elif first_player == '2':
            chosen = True
            while not check_for_winner():
                ai_turn()
                print("\n")
                player_turn()
        else:
            print("Invalid input. Please try again!")


