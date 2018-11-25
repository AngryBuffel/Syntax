# VDLS - Sentdex Python3 YT Tutorial - 11/15/18

game = [[0,0,0],[0,0,0],[0,0,0]]


def game_board(player=0, row=0, column=0):
    print("   a  b  c")
    game[row][column] = player
    for count, row in enumerate(game):
        print(count,row)

