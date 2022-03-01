class Bot(object):
    def __call__(self, board, player):
        """ Receives a 12-member tuple, (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),
            representing the board,

              0 |  1 |  2 |  3
            ----+----+----+----
              4 |  5 |  6 |  7
            ----+----+----+----
              8 |  9 | 10 | 11

            where each 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 equals either:

            'x' player-1 has placed an 'x' in this cell,
            'o' player-2 has placed an 'o' in this cell or
            '' neither player has placed a symbol in this cell;

            and a symbol, either 'x' or 'o', telling the bot whether it
            plays as player-1 or player-2:

            'x' player-1,
            'o' player-2.


            Returns the index of the cell where the bot will play its move:
            the integer 0 for cell-0, the integer 1 for cell-1, etc.


            For example, receiving the tuple,
            ('', '', 'x', 'o', 'o', 'x', 'x', 'o', '', '', 'o', 'x'),
            representing the board,

                |    |  x |  o
            ----+----+----+----
              o |  x |  x |  o
            ----+----+----+----
                |    |  o |  x

            and the symbol 'x', telling it it plays as player-1, a bot might
            return the integer 8 to play to the bottom, leftmost cell and win.
        """

        return [indx for indx, member in enumerate(board) if member == ''][0]

    THREE_IN_A_ROW     = (( 0,  1,  2), ( 1,  2,  3), ( 4,  5,  6), ( 5,  6,  7),
                          ( 8,  9, 10), ( 9, 10, 11), ( 0,  4,  8), ( 1,  5,  9),
                          ( 2,  6, 10), ( 3,  7, 11), ( 0,  5, 10), ( 1,  6, 11),
                          ( 2,  5,  8), ( 3,  6,  9))
    PLAYER_1, PLAYER_2 = 'x', 'o'


def checkForWin(board, player, winningTuples):
    places = [indx for indx, member in enumerate(board) if member == player]
    for win in winningTuples:
        if win[0] in places and win[1] in places and win[2] in places:
            return True
    return False