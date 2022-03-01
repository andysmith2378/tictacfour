import Bots
from main import Bot, checkforwin


BOTS_PLAYING = {Bot.PLAYER_1: Bots.Immediate(),
                Bot.PLAYER_2: Bots.Pairs()}


def makemove(boardtuple, boardlist, movenumber, turn):
    move = BOTS_PLAYING[turn](boardtuple, turn)
    if move is None:
        raise RuntimeError(
            f'{BOTS_PLAYING[turn].__class__.__name__} did not return a move')
    elif isinstance(move, int):
        print(f'\nmove-{movenumber:d}: {turn} plays to cell-{move:d}\n')
        if move < 0 or move > 11:
            raise RuntimeError(f'{turn} tried to play outside the board')
        else:
            if boardlist[move] == '':
                boardlist[move] = turn
                if checkforwin(boardlist, turn, Bot.THREE_IN_A_ROW):
                    draw(boardlist)
                    print(f'\n{turn} wins\n')
                    exit()
            else:
                raise RuntimeError(f'{turn} tried to play to an occupied cell')
    else:
        raise RuntimeError(f'{BOTS_PLAYING[turn].__class__.__name__} returned an '
                           f'object of type {type(move)}')


def draw(board, rowdivider="\n---+---+---+---\n"):
    print(rowdivider.join(["|".join([f"{cell:^3}" for cell in board[indx:indx+4]])
                           for indx in range(0, 12, 4)]))


def play(turn=Bot.PLAYER_1):
    boardList = [''] * 12
    for movenumber in range(1, 13):
        board = tuple(boardList)
        draw(board)
        try:
            makemove(board, boardList, movenumber, turn)
        except RuntimeError as err:
            raise err
            exit()
        turn = Bot.PLAYER_2 if turn == Bot.PLAYER_1 else Bot.PLAYER_1
    draw(boardList)
    print('\ndraw\n')


if __name__ == '__main__':
    play()
