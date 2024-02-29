import pygame
import sys

WIN_SIZE = 780
CELL_SIZE = WIN_SIZE // 3
EMPTY = None
O = 0
X = 1
FONT_NAME = 'Verdana'
FONT_SIZE = CELL_SIZE // 4

#loading images
FIELD_IMAGE = pygame.transform.scale(pygame.image.load('game_data/images/field.png'), (WIN_SIZE, WIN_SIZE))
O_IMAGE = pygame.transform.scale(pygame.image.load('game_data/images/O.png'), (CELL_SIZE, CELL_SIZE))
X_IMAGE = pygame.transform.scale(pygame.image.load('game_data/images/X.png'), (CELL_SIZE, CELL_SIZE))

def draw_text(screen, text, size, x, y):
    font = pygame.font.SysFont(FONT_NAME, size, True)
    text_surface = font.render(text, True, pygame.Color('black'))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    screen.blit(text_surface, text_rect)

def check_winner(board):

    for row in board:
        if len(set(row)) == 1 and row[0] is not EMPTY:
            return row[0]

    for col in range(3):
        column = [row[col] for row in board]
        if len(set(column)) == 1 and column[0] is not EMPTY:
            return column[0]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not EMPTY:
        return board[0][2]
    return EMPTY

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIN_SIZE, WIN_SIZE))
    clock = pygame.time.Clock()
    running = True
    board = [[EMPTY, EMPTY, EMPTY] for _ in range(3)]
    player_turn = X
    winner = EMPTY

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and winner is EMPTY:
                x, y = pygame.mouse.get_pos()
                col, row = x // CELL_SIZE, y // CELL_SIZE
                if board[row][col] is EMPTY:
                    board[row][col] = player_turn
                    player_turn = O if player_turn == X else X
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                board = [[EMPTY, EMPTY, EMPTY] for _ in range(3)]
                player_turn = X
                winner = EMPTY
        #render screen
        screen.fill(pygame.Color('black'))
        screen.blit(FIELD_IMAGE, (0, 0))

        for y, row in enumerate(board):
            for x, cell in enumerate(row):
                if cell == X:
                    screen.blit(X_IMAGE, (x * CELL_SIZE, y * CELL_SIZE))
                elif cell == O:
                    screen.blit(O_IMAGE, (x * CELL_SIZE, y * CELL_SIZE))
        #winner condition
        winner = check_winner(board)
        if winner is not EMPTY:
            winner_text = 'Player "X" wins!' if winner == X else 'Player "O" wins!'
            draw_text(screen, winner_text, FONT_SIZE, WIN_SIZE // 2, WIN_SIZE // 4)
            draw_text(screen, 'Press SPACE to reset the game', FONT_SIZE // 2, WIN_SIZE // 2, WIN_SIZE - FONT_SIZE)
        elif EMPTY not in [cell for row in board for cell in row]:
            draw_text(screen, 'Game Over! Press SPACE to reset the game', FONT_SIZE // 2, WIN_SIZE // 2, WIN_SIZE // 4)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
