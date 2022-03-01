import Bots
from main import Bot, checkForWin

BOTS_PLAYING = {Bot.PLAYER_1: Bots.Immediate(),
                Bot.PLAYER_2: Bots.Pairs()}

def makeMove(board, boardList, movenumber, turn):
    move = BOTS_PLAYING[turn](board, turn)
    if move is None:
        raise RuntimeError(
            f'{BOTS_PLAYING[turn].__class__.__name__} did not return a move')
    else:
        print(f'\nmove-{movenumber:d}: {turn} plays to cell-{move:d}\n')
        if boardList[move] == '':
            boardList[move] = turn
            if checkForWin(boardList, turn, Bot.THREE_IN_A_ROW):
                draw(boardList)
                print(f'\n{turn} wins\n')
                exit()
        else:
            raise RuntimeError(f'{turn} tried to play to an occupied cell')


def draw(board, rowdivider="\n---+---+---+---\n"):
    print(rowdivider.join(["|".join([f"{cell:^3}" for cell in board[indx:indx+4]])
                           for indx in range(0, 12, 4)]))

def play(turn=Bot.PLAYER_1):
    boardList = [''] * 12
    for movenumber in range(1, 13):
        board = tuple(boardList)
        draw(board)
        try:
            makeMove(board, boardList, movenumber, turn)
        except RuntimeError as err:
            raise err
            exit()
        turn = Bot.PLAYER_2 if turn == Bot.PLAYER_1 else Bot.PLAYER_1
    draw(boardList)
    print('\ndraw\n')


if __name__ == '__main__':
    play()
