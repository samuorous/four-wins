class Board:
    """ Class representing a Board used in the connect four game. """
    def __init__(self, map=None, w=7, h=6):
        self.w = w
        self.h = h
        if not map:
            self.map = dict((key, value) for key, value in [((i, j), '_')
                                                            for i in range(self.w)
                                                            for j in range(self.h)])
        else:
            self.map = map
        self.last_move = None

    def __repr__(self):
        r = ''
        for j in range(6):
            for i in range(7):
                if i == 0:
                    r += '|'
                if (i, j) == self.last_move:
                    if self.map[(i, j)] == 'X':
                        r += '\x1b[6;30;42m' + self.map[(i, j)] + '\x1b[0m' + '|'
                    else:
                        r += '\x1b[6;30;41m' + self.map[(i, j)] + '\x1b[0m' + '|'
                else:
                    if self.map[(i, j)] == 'X':
                        r += '\x1b[3;30;42m' + self.map[(i, j)] + '\x1b[0m' + '|'
                    elif self.map[(i, j)] == 'O':
                        r += '\x1b[3;30;41m' + self.map[(i, j)] + '\x1b[0m' + '|'
                    else:
                        r += self.map[(i, j)] + '|'
            r += '\n'
        r += '|1|2|3|4|5|6|7|\n'
        return r

    def __getitem__(self, item):
        return self.map[item]

    def __setitem__(self, key, value):
        self.map[key] = value

    def empty(self, pos):
        """ Check is a position is empty on the board.
        :param pos: position (x, y) on the board
        :return: True if position is empty else False
        """
        return True if self.map[pos] == '_' else False

    def count_empty(self):
        """ Count empty spots on the Board.
        :rtype: int
        :return: number of empty spots in the board
        """
        count = 0
        for pos in self.map:
            if self.empty(pos):
                count += 1
        return count

    def get_possible_moves(self):
        """ Fetch empty positions.
        :return: set containing all the free positions (x, y) on the board
        :rtype: set
        """
        moves = set()
        i = 0
        while i < self.w:
            #  for i in (3, 2, 4, 1, 5, 0, 6):  # better sorting (prefer the middle to expand first)
            for j in range(self.h - 1, -1, -1):
                if self.map[(i, j)] == '_':
                    moves.add((i, j))
                    break
            i += 1
        return moves

    def won(self, player):
        """ Determine if player won the game (has 4 connected in a row).
        :rtype: bool
        :param player: the player ('X' or 'Y')
        :return: True if player won the game.
        """
        lines = [self.map[(x, y + 0)] + self.map[(x, y + 1)] + self.map[(x, y + 2)] + self.map[(x, y + 3)] for x in range(7) for y in range(3)]
        lines += [self.map[(x + 0, y)] + self.map[(x + 1, y)] + self.map[(x + 2, y)] + self.map[(x + 3, y)] for y in range(6) for x in range(4)]
        lines += [self.map[(x + 0, y + 0)] + self.map[(x + 1, y + 1)] + self.map[(x + 2, y + 2)] + self.map[(x + 3, y + 3)] for x in range(4) for y in range(3)]
        lines += [self.map[(x + 0, 5 - y)] + self.map[(x + 1, 4 - y)] + self.map[(x + 2, 3 - y)] + self.map[(x + 3, 2 - y)] for x in range(4) for y in range(3)]

        return player + player + player + player in lines

    def play(self, pos, player):
        """ Occupy pos by player.
        :rtype: bool
        :param pos: Position to be occupied
        :param player: Player to be put on the board
        :return: True if move was legal else False
        """
        if pos in self.get_possible_moves():
            self.map[pos] = player
            self.last_move = pos
            return True
        else:
            return False

    def play_slot(self, slot, player):
        """ Play (drop) as player into a slot on the board
        :param slot: 1, 2, 3, 4, 5, 6 or 7
        :param player: player
        :return: True if it was legal to play this slot else False
        """
        possible = self.get_possible_moves()
        if slot == '1':
            for p in possible:
                if p[0] == 0:
                    self.play(p, player)
                    return True
        elif slot == '2':
            for p in possible:
                if p[0] == 1:
                    self.play(p, player)
                    return True
        elif slot == '3':
            for p in possible:
                if p[0] == 2:
                    self.play(p, player)
                    return True
        elif slot == '4':
            for p in possible:
                if p[0] == 3:
                    self.play(p, player)
                    return True
        elif slot == '5':
            for p in possible:
                if p[0] == 4:
                    self.play(p, player)
                    return True
        elif slot == '6':
            for p in possible:
                if p[0] == 5:
                    self.play(p, player)
                    return True
        elif slot == '7':
            for p in possible:
                if p[0] == 6:
                    self.play(p, player)
                    return True
        return False
