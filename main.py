from game import Game
from random import randint

# init the game
game = Game()
# set the players to place
game.set_players("x", "o")
# game logic to test the game
p = 2
while True:
    if p == 2:
        print("enter where you want to place your char")
        x = input().split(" ")
        game.insert(p, x)
        game.update_scores()
        w = game.check_winner()
        if w == 0:
            print("1 wins")
            game.reset_game()
        if w == 1:
            print("2 wins")
            game.reset_game()
        p = 1
    else:
        r = randint(0,2)
        c = randint(0,2)
        q = game.insert(p, [r, c])
        while q == -1:
            r = randint(0,2)
            c = randint(0,2)
            q = game.insert(p, [r, c])
        
        game.update_scores()
        w = game.check_winner()
        if w == 0:
            print("1 wins")
            game.reset_game()
        if w == 1:
            print("2 wins")
            game.reset_game()
        p = 2



    







