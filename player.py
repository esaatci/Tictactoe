
class Player(object):

    def __init__(self):
        self.score = 0
        self.char = None

    def get_score(self):
        return self.score
    
    def set_char(self, char):
        self.char = char
    
    def get_char(self):
        return self.char
    
    def increment_score(self):
        self.score += 1
    
    def reset(self):
        self.score = 0
    
