from board import Board
from player import Player

class Game(object):

    def __init__(self):
        self.board = Board()
        self.player1 = Player()
        self.player2 = Player()
    
    def reset_game(self):
        self.board = Board()
        self.player1.reset()
        self.player2.reset()
    
    def reset_board(self):
        self.board = Board()
    
    def set_players(self, char1, char2):
        if char1 == char2:
            return -1
        self.player1.set_char(char1)
        self.player2.set_char(char2)
    
    def get_scores(self):
        return self.player1.get_score, self.player2.get_score
    
    def insert(self, player, tile):
        if player == 1:
            x = tile + [self.player1.get_char()]
        elif player == 2:
            x = tile + [self.player2.get_char()]
        if self.board.insert(x) == -1:
            return - 1
    
    def check_board(self):
        c = self.board.validate()
        if c == -1:
            return -1 
        return c
    
    def update_scores(self):
        b = self.check_board()
        if b != -1:
            if b == self.player1.get_char:
                self.player1.increment_score()
                self.reset_board()
            else:
                self.player2.increment_score()
                self.reset_board()
    
    def check_winner(self):
        scores = self.get_scores()
        if scores[0] == 3:
            return 0
        elif scores[1] == 3:
            return 1
        else:
            return -1
    



    
    
    
