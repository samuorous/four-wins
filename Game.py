import time

import sys

from AlphaBeta import AlphaBeta
from Board import Board
from Node import Node


class Game:
    """ A simple 4 wins game. Provides a interactive and automatic version. """
    def __init__(self):
        self.start_depth = 6
        self.target_round_time = 2500
        self.max_player = 'X'
        self.min_player = 'O'
        self.board = Board()
        self.actual_depth = 0
        self.turn = 0

    def opponent(self, player):
        """ Returns the opponent for a player

        :param player: The player
        :type player: str
        :return: Its opponent
        :rtype: str
        """
        return self.max_player if player == self.min_player else self.min_player

    def reset(self):
        """ Reset the game.

        """
        self.board = Board()
        self.actual_depth = self.start_depth
        self.turn = 0

    def automatic_game(self, start_player=True):
        """ Play an automatic game to the end

        :param start_player: If the 'Human' player should start
        :type start_player: bool
        """
        my_turn = start_player
        self.actual_depth = self.start_depth
        self.turn = 0
        print('Starting game..')
        start_time = int(time.time() * 1000)
        turn_time = int(time.time() * 1000)
        while True:
            self.turn += 1
            print('Turn: ', self.turn)
            print(self.board)
            sys.stdout.flush()
            if self.board.won('O') or self.board.won('X') or not self.board.get_possible_moves():
                print(' Finished')
                print(self.board)
                end = int(time.time() * 1000)
                elapsed = end - start_time
                print("needed: ", elapsed, 'ms')
                self.reset()
                break
            if my_turn:
                ab = AlphaBeta(self)
                tree = Node(self.board)
                score = ab.iterate_2(tree, self.actual_depth, -100, 100, 'O')
                print('player O thinks score:', score, 'Search depth:', self.actual_depth)
                if tree.children:
                    tree.children.sort(key=lambda x: x.beta, reverse=False)
                    candidate = tree.children[0]
                    self.board.play(candidate.my_move, 'O')
                my_turn = False
            else:
                ab = AlphaBeta(self)
                tree = Node(self.board)
                score = ab.iterate(tree, self.actual_depth, -100, 100, 'X')
                print('player X thinks score:', score, 'Search depth:', self.actual_depth)
                if tree.children:
                    tree.children.sort(key=lambda x: x.alpha, reverse=True)
                    candidate = tree.children[0]
                    self.board.play(candidate.my_move, 'X')
                my_turn = True
            if int(time.time() * 1000) - turn_time < self.target_round_time:
                pass
                # self.actual_depth += 1
            else:
                pass
                # self.actual_depth -= 1

            turn_time = int(time.time() * 1000)

    def interactive_game(self, human_first=True):
        """ Start a interactive game

        :param human_first: If the human should begin.
        :type human_first: bool
        """
        my_turn = human_first
        self.actual_depth = self.start_depth
        while True:
            self.turn += 1
            print(self.board)
            print('Turn: ', self.turn)
            if self.board.won('O'):
                print('Yay, you won... lets go again....')
                print('###########################')
                self.reset()
                continue
            if self.board.won('X'):
                print('Lol, you lost... lets go again....')
                print('###########################')
                self.reset()
                continue
            if not self.board.get_possible_moves():
                print('Okay, draw ... lets go again....')
                print('###########################')
                self.reset()
                continue
            if my_turn:
                choise = input("Select position (1, 2, 3, 4, 5, 6, 7):")
                if choise in '1234567':
                    if self.board.play_slot(choise, 'O'):
                        my_turn = False
                    else:
                        print('Yo fucker, dont try to trick me!')
                else:
                    print('Yo fucker, dont try to trick me!')
            else:
                ab = AlphaBeta(self)
                tree = Node(self.board)

                start_time = int(time.time()*1000)
                print("Start searching...", end=' ')
                sys.stdout.flush()
                score = ab.iterate(tree, self.actual_depth, -100, 100, 'X')
                end = int(time.time()*1000)
                elapsed = end - start_time
                print("Finished in", elapsed, 'ms. Searching depth:', self.actual_depth, 'moves. Score:', score)
                if elapsed < self.target_round_time:
                    pass
                    # self.actual_depth += 1
                else:
                    pass
                    # self.actual_depth -= 1
                if tree.children:
                    candidate = max(tree.children)
                    self.board.play(candidate.my_move, 'X')
                my_turn = True
