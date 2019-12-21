
# the board class

class Board(object):

    def __init__(self):
        self.board = [[0 for i in range(3)] for j in range(3)]

    def insert(self, tile):
        t_row = int(tile[0])
        t_col = int(tile[1])
        bok = tile[2]
        if self.board[t_row][t_col] != 0:
            return -1
        else:
            self.board[t_row][t_col] = bok

    def validate(self):
        zero_count = 0
        # check for rows
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2]:
                if self.board[i][0] != 0:
                    return self.board[i][0] 
                else:
                    zero_count += 1
        
        for j in range(3):
            if self.board[0][j] == self.board[1][j] == self.board[2][j]:
                if self.board[0][j] != 0:
                    return self.board[0][j] 
                else:
                    zero_count += 1
        
        if self.board[0][0] == self.board[1][1] == self.board[2][2]:
            if self.board[0][0] != 0:
                return self.board[0][0]
            else:
                zero_count += 1
        
        if self.board[0][2] == self.board[1][1] == self.board[2][0]:
            if self.board[0][2] != 0:
                return self.board[0][2]
            else:
                zero_count += 1
        
        if zero_count == 0:
            return -1
        else:
            return 0
        
                
    
# test = Board()
# t = test.validate()
# while t == -1:
#     x = input("enter the cord").split(" ")
#     x[0] = int(x[0])
#     x[1] = int(x[1])
#     test.insert(x)
#     t = test.validate()
