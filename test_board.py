from unittest import TestCase
from Board import Board


class TestBoard(TestCase):
    def test_empty(self):
        board = Board()
        for i in range(board.w):
            for j in range(board.h):
                err_msg = 'Position ({}, {}) should be empty for a newly created board'.format(i, j)
                self.assertTrue(board.empty((i, j)), err_msg)
                err_msg = 'Position ({}, {}) should no longer be empty after setting it to {}'.format(i, j, 'X')
                board[(i, j)] = 'X'
                self.assertFalse(board.empty((i, j)), err_msg)

    def test_count_empty(self):
        board = Board()
        size = board.w * board.h
        err_msg = 'Board should have {} empty fields after \
        creation of a {} by {} field'.format(size, board.w, board.h)
        self.assertTrue(board.count_empty() == board.w * board.h, err_msg)
        count = 0
        for i in range(board.w):
            for j in range(board.h):
                count += 1
                board[(i, j)] = 'X'
                err_msg = 'Board should have {} free fields.'.format(size - count)
                self.assertTrue(board.count_empty() == size - count, err_msg)

    def test_get_possible_moves(self):
        board = Board()
        all_moves = {(i, board.h - 1) for i in range(board.w)}
        self.assertEqual(board.get_possible_moves(), all_moves)
        # Fill one slot to the top
        for i in range(board.h):
            board[0, i] = 'X'
        all_moves.remove((0, board.h - 1))
        self.assertEqual(board.get_possible_moves(), all_moves)

    def test_won(self):
        board = Board()
        self.assertFalse(board.won('X'))

    def test_play(self):
        board = Board()
        pos = (0, board.h - 1)
        board.play(pos, 'X')  # Do a legal move.
        self.assertFalse(board.empty(pos))
        self.assertEqual(board[pos], 'X')
        board.play(pos, 'O')  # Do a illegal move.
        self.assertEqual(board[pos], 'X')  # should stay the same.
