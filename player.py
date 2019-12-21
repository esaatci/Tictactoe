
class Player(object):

    def __init__(self):
        self.score = 0
        self.char = None

    def get_score(self):
        'returns the score of the player'
        return self.score
    
    def set_char(self, char):
        'sets the character that the player uses'
        self.char = char
    
    def get_char(self):
        'returns the char of the plauer'
        return self.char
    
    def increment_score(self):
        'increments the score of the player' 
        self.score += 1
    
    def reset(self):
        'resets the score to zero'
        self.score = 0
    
