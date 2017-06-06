import copy

from Board import Board


class Node:
    def __init__(self, board, my_move=None):
        self.board = board
        self.my_move = my_move
        self.children = []
        self.value = -100
        self.alpha = -10000
        self.beta = 10000

    def __lt__(self, other):
        return self.value < other.value

    def fetch_children(self, player):
        """ Returns a list of all possible moves for a player

        :param player: actual player.
        :type player:
        :return: List of nodes.
        :rtype: list
        """
        chlds = self.board.get_possible_moves()
        self.children = []
        for pos in chlds:
            _board = Board(copy.copy(self.board.map))
            #_board = copy.deepcopy(self.board)
            _board[pos] = player
            self.children.append(Node(_board, pos))
        return self.children

    def is_terminal(self):
        """ Determines if the game is over.

        :return:
        :rtype:
        """
        if not self.board.get_possible_moves():
            return True
        if self.board.won('X') or self.board.won('O'):
            return True
        return False

    def get_score_2(self, depth):
        """ Score a position

        :param depth: The current depth we are looking at
        :type depth: int
        :return: Score
        :rtype: int
        """
        result = 0
        lines = self.get_eval_lines()

        for line in lines:
            if line in ['XX__', '_XX_', '__XX']:
                result += 2
            elif line in ['OO__', '_OO_', '__OO']:
                result -= 2
            elif line in ['_XXX', 'X_XX', 'XX_X', 'XXX_']:
                result += 3
            elif line in ['_OOO', 'O_OO', 'OO_O', 'OOO_']:
                result -= 3
            elif line == 'XXXX':
                result += 1000
                break
            elif line == 'OOOO':
                result -= 1000
                break
        result += self.get_middle_score()
        return result * (depth + 1)

    def get_score(self, depth):
        """ Score a position

        :param depth: he current depth we are looking at
        :type depth: int
        :return: Score
        :rtype: int
        """
        result = 0
        lines = self.get_eval_lines()

        for line in lines:
            if line in ['XX__', '_XX_', '__XX']:
                result += 2
            elif line in ['OO__', '_OO_', '__OO']:
                result -= 2
            if line in ['_XXX', 'X_XX', 'XX_X', 'XXX_']:
                result += 3
            elif line in ['_OOO', 'O_OO', 'OO_O', 'OOO_']:
                result -= 3
            elif line == 'XXXX':
                result += 1000
                break
            elif line == 'OOOO':
                result -= 1000
                break
        return result * (depth + 1)

    def get_middle_score(self):
        """ Count the hits in the middle lane. +1 for each hit, -1 for each enemy hit.

        :return: Score
        :rtype: int
        """
        count = 0
        for x in range(2, 5):
            for y in range(6):
                if self.board[(x, y)] == 'X':
                    count += 1
                elif self.board[(x, y)] == 'O':
                    count -= 1
        return count

    def get_eval_lines(self):
        """ Return a list of all possible lines in the board and its current occupants.

        :return: List of lines with current occupants.
        :rtype: list
        """
        lines = [self.board[(x, y + 0)] + self.board[(x, y + 1)] + self.board[(x, y + 2)] + self.board[(x, y + 3)] for x in range(7) for y in range(3)]
        lines += [self.board[(x + 0, y)] + self.board[(x + 1, y)] + self.board[(x + 2, y)] + self.board[(x + 3, y)] for y in range(6) for x in range(4)]
        lines += [self.board[(x + 0, y + 0)] + self.board[(x + 1, y + 1)] + self.board[(x + 2, y + 2)] + self.board[(x + 3, y + 3)] for x in range(4) for y in range(3)]
        lines += [self.board[(x + 0, 5 - y)] + self.board[(x + 1, 4 - y)] + self.board[(x + 2, 3 - y)] + self.board[(x + 3, 2 - y)] for x in range(4) for y in range(3)]

        return lines
