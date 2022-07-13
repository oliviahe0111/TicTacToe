import pygame, sys
import numpy as np


pygame.init()

WIDTH = 600
HEIGHT = WIDTH

BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // BOARD_COLS
LINE_WIDTH = SQUARE_SIZE // 12
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = CIRCLE_RADIUS // 4
CROSS_WIDTH = CIRCLE_WIDTH
SPACE_BTW_CORNER = SQUARE_SIZE // 4

#COLORS
RED = (255, 0, 0)
# background color
BG_COLOR = (164, 202, 202)
# line_color
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)

screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption("Tic Tac Toe")
screen.fill(BG_COLOR)

# board
board = np.zeros((BOARD_ROWS, BOARD_COLS))
print(board)


# draw four main lines
def draw_lines():
    # first horizontal line
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    # second horizontal line
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)
    # first vertical line
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    # second vertical line
    pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)


def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * SQUARE_SIZE + SQUARE_SIZE / 2),
                                                          int(row * SQUARE_SIZE + SQUARE_SIZE / 2)), CIRCLE_RADIUS,
                                   CIRCLE_WIDTH)
            elif board[row][col] == 2:
                # ascending line
                pygame.draw.line(screen, CROSS_COLOR,
                                 (col * SQUARE_SIZE + SPACE_BTW_CORNER,
                                                       row * SQUARE_SIZE + SQUARE_SIZE - SPACE_BTW_CORNER),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE_BTW_CORNER,
                                  row * SQUARE_SIZE + SPACE_BTW_CORNER),
                                 CROSS_WIDTH)
                # descending line
                pygame.draw.line(screen, CROSS_COLOR,
                                 (col * SQUARE_SIZE + SPACE_BTW_CORNER,
                                                       row * SQUARE_SIZE + SPACE_BTW_CORNER),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE_BTW_CORNER,
                                  row * SQUARE_SIZE + SQUARE_SIZE - SPACE_BTW_CORNER),
                                 CROSS_WIDTH)


def mark_square(row, col, player):
    board[row][col] = player


def available_square(row, col):
    if board[row][col] == 0:
        return True
    else:
        return False


def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            # if the block is empty, return false indicating board not full
            if board[row][col] == 0:
                return False
    return True


def check_win(player):
    #vertical win check
    for col in range(BOARD_COLS):
        if board[0][col] == player == board[1][col] == board[2][col]:
            draw_vertical_winning_line(col, player)
            return True

    #horizontal win check
    for row in range(BOARD_ROWS):
        if board[row][0] == player == board[row][1] == board[row][2]:
            draw_horizontal_winning_line(row, player)
            return True

    # asce diagonal win check
    if board[2][0] == player == board[1][1] == board[0][2]:
        draw_asc_diagonal_winning_line(player)
        return True

    # desc diagonal win check
    if board[0][0] == player == board[1][1] == board[2][2]:
        draw_des_diagonal_winning_line(player)
        return True

    return False


def draw_vertical_winning_line(col, player):
    posX = col * SQUARE_SIZE + SQUARE_SIZE/2

    if player ==1:
        color = CIRCLE_COLOR
    elif player ==2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (posX, LINE_WIDTH), (posX, HEIGHT - LINE_WIDTH), LINE_WIDTH)


def draw_horizontal_winning_line(row, player):
    posY = row * SQUARE_SIZE + SQUARE_SIZE/2

    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (LINE_WIDTH, posY), (WIDTH - LINE_WIDTH, posY), LINE_WIDTH)


def draw_asc_diagonal_winning_line(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (LINE_WIDTH, HEIGHT - LINE_WIDTH), (WIDTH - LINE_WIDTH, LINE_WIDTH), LINE_WIDTH)


def draw_des_diagonal_winning_line(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (LINE_WIDTH, LINE_WIDTH), (WIDTH - LINE_WIDTH, HEIGHT - LINE_WIDTH), LINE_WIDTH)


def restart():
    screen.fill(BG_COLOR)
    draw_lines()
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0


draw_lines()

player = 1
game_over = False


# mainloop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

            mouseX = event.pos[0] # x coordinate
            mouseY = event.pos[1] # y coordinate

            clicked_row = int(mouseY // SQUARE_SIZE )
            clicked_col = int(mouseX // SQUARE_SIZE)

            if available_square(clicked_row, clicked_col):

                mark_square(clicked_row, clicked_col, player)
                if check_win(player):
                    game_over = True
                player = player % 2 + 1

                # if player == 1:
                #     mark_square(clicked_row, clicked_col, 1)
                #     check_win(player)
                #     if check_win(player):
                #         game_over = True
                #     player = 2
                #
                # elif player == 2:
                #     mark_square(clicked_row, clicked_col, 2)
                #     check_win(player)
                #     if check_win(player):
                #         game_over = True
                #     player = 1

                draw_figures()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                player = 1
                game_over = False

    pygame.display.update()
