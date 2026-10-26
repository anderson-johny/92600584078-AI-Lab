"""
7. Implement Two Player Game - Tic-Tac-Toe (Using Heuristic Function).  
NAME: ANDERSON JOHNY GEORGE
ENROLLNO. : 92600584078
"""
# display board
def display(board):
    print()
    print(board[0],"|",board[1],"|",board[2])
    print("--+---+--")
    print(board[3],"|",board[4],"|",board[5])
    print("--+---+--")
    print(board[6],"|",board[7],"|",board[8])
    print()

# herisustic function
def heuristic(board):
    win=[
        (0,1,2),
        (3,4,5),
        (6,7,8),
        (1,4,7),
        (2,5,8),
        (0,4,8),
        (2,4,6)
    ]

    for a,b,c in win:
        if board[a]==board[b]==board[c]=="x":
            return 2
        elif board[a]==board[b]==board[c]=="o":
            return 4
    return 0

# main game
board=[" "]*9
player ="x"

for turn in range(9):
    display(board)
    print("player",player)

    position=int(input("enter the position (1-9) :"))-1
    if position<0 or position>8 or board[position]!= " ":
        print("invalid position")
        continue
    board[position]=player

    score=heuristic(board)

    if score==2:
        display(board)
        print("player X wins !!")
        break
    if score==4:
        display(board)
        print("player o wins !!")
        break
    #  change plyer
    if player=="x":
        player="o"
    else:
        player="x"
else:
    display(board)
    print("!! game draw !!")
