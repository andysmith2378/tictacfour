import main
import random


class FirstOpen(main.Bot):
    pass


class RandomChoice(main.Bot):
    def __call__(self, board, player):
        return random.choice(RandomChoice.opencells(board))

    @staticmethod
    def opencells(board):
        return [ind for ind, member in enumerate(board) if member == '']


class Immediate(RandomChoice):
    def __call__(self, board, player):
        move = self.threeinarow(board, player)
        if move is None:
            return RandomChoice.__call__(self, board, player)
        return move

    def threeinarow(self, boardtuple, player):
        enemy = Immediate.fetchEnemy(player)
        block = None
        for candidate in RandomChoice.opencells(boardtuple):
            boardlist            = list(boardtuple)
            boardlist[candidate] = player
            if main.checkforwin(boardlist, player, main.Bot.THREE_IN_A_ROW):
                return candidate
            boardlist[candidate] = enemy
            if main.checkforwin(boardlist, enemy, main.Bot.THREE_IN_A_ROW):
                block = candidate
        return block

    @staticmethod
    def fetchEnemy(player):
        if player == main.Bot.PLAYER_1:
            return main.Bot.PLAYER_2
        return main.Bot.PLAYER_1


class Pairs(Immediate):
    TWO_TWO_IN_A_ROW = ((( 1,  2), ( 4,  8), ( 5, 10),                     ),
                        (( 5,  9), ( 2,  3), ( 2,  0), ( 6, 11),           ),
                        (( 1,  0), ( 1,  3), ( 5,  8), ( 6, 10),           ),
                        (( 2,  1), ( 7, 11), ( 6,  9),                     ),
                        (( 0,  8), ( 5,  6),                               ),
                        (( 1,  9), ( 0, 10), ( 2,  8), ( 4,  6), ( 6,  7), ),
                        (( 5,  7), ( 5,  4), ( 1, 11), ( 3,  9), ( 2, 10), ),
                        (( 3, 11), ( 6,  5),                               ),
                        (( 4,  0), ( 9, 10), ( 5,  2),                     ),
                        (( 8, 10), ( 5,  1), ( 6,  3), (10, 11),           ),
                        (( 9,  8), ( 5,  0), ( 6,  2), (11,  9),           ),
                        ((10,  9), ( 6,  1), ( 7,  3),                     ), )
    PREFERENCES      = (5, 6, 0, 3, 8, 11, 1, 2, 9, 10, 4, 7)

    def __call__(self, board, player):
        move = self.threeinarow(board, player)
        if move is None:
            enemy = Immediate.fetchEnemy(player)
            block = None
            for centre, placeTuple in enumerate(Pairs.TWO_TWO_IN_A_ROW):
                if board[centre] == '':
                    for n, (first, second) in enumerate(placeTuple[:-1]):
                        occupants = board[first], board[second]
                        if '' in occupants:
                            if player in occupants:
                                if self.checkForSecond(board, n, placeTuple, player):
                                    return centre
                            if enemy in occupants:
                                if self.checkForSecond(board, n, placeTuple, enemy):
                                    block = centre
            if block is None:
                options = RandomChoice.opencells(board)
                for favourite in Pairs.PREFERENCES:
                    if favourite in options:
                        return favourite
                return main.Bot.__call__(self, board, player)
            return block
        return move

    def checkForSecond(self, board, indx, placeTuple, target):
        for left, right in placeTuple[indx+1:]:
            occupants = board[left], board[right]
            if ('' in occupants) and (target in occupants):
                return True
        return False