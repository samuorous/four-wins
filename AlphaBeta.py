class AlphaBeta:
    """ Simple Alpha Beta pruning used to determine a good move."""
    def __init__(self, game):
        self.game = game

    def iterate(self, node, depth, alpha, beta, player):
        """ Walk along the tree starting at node until a certain depth.

        :param node: node to start with
        :param depth: depth to stop at
        :param alpha: initial alpha
        :param beta: initial beta
        :param player: player in turn at this node.
        :return: best score.
        """
        if depth == 0 or node.is_terminal():
            return node.get_score(depth)

        if player == self.game.max_player:
            children = node.fetch_children(player)
            for child in children:
                eval = self.iterate(child, depth - 1, alpha, beta, self.game.opponent(player))
                if eval > alpha:
                    alpha = eval
                    child.value = eval
                    child.alpha = eval
                if alpha >= beta:
                    break
            return alpha
        else:
            children = node.fetch_children(player)
            for child in children:
                eval = self.iterate(child, depth - 1, alpha, beta, self.game.opponent(player))
                if eval < beta:
                    beta = eval
                    child.beta = eval
                if alpha >= beta:
                    break
            return beta

    def iterate_2(self, node, depth, alpha, beta, player):
        """ Walk along the tree starting at node until a certain depth.

        :param node: node to start with
        :param depth: depth to stop at
        :param alpha: initial alpha
        :param beta: initial beta
        :param player: player in turn at this node.
        :return: best score.
        """
        if depth == 0 or node.is_terminal():
            return node.get_score_2(depth)

        if player == self.game.max_player:
            children = node.fetch_children(player)
            for child in children:
                eval = self.iterate_2(child, depth - 1, alpha, beta, self.game.opponent(player))
                if eval > alpha:
                    alpha = eval
                    child.value = eval
                    child.alpha = eval
                if alpha >= beta:
                    break
            return alpha
        else:
            children = node.fetch_children(player)
            for child in children:
                eval = self.iterate_2(child, depth - 1, alpha, beta, self.game.opponent(player))
                if eval < beta:
                    beta = eval
                    child.beta = eval
                if alpha >= beta:
                    break
            return beta
