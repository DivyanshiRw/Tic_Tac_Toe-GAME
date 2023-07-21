# Project on TIC TAC TOE Game

def printBoard(xst, zst):
    zero='X' if xst[0] else ('O' if zst[0] else 0)
    one='X' if xst[1] else ('O' if zst[1] else 1)
    two='X' if xst[2] else ('O' if zst[2] else 2)
    three='X' if xst[3] else ('O' if zst[3] else 3)
    four='X' if xst[4] else ('O' if zst[4] else 4)
    five='X' if xst[5] else ('O' if zst[5] else 5)
    six='X' if xst[6] else ('O' if zst[6] else 6)
    seven='X' if xst[7] else ('O' if zst[7] else 7)
    eight='X' if xst[8] else ('O' if zst[8] else 8)

    print(f" {zero} | {one} | {two} ")
    print(f"---|---|---")
    print(f" {three} | {four} | {five} ")
    print(f"---|---|---")
    print(f" {six} | {seven} | {eight} ")

def sum(a,b,c):
    return a+b+c

def checkWinner(xst, zst):
    win=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]] 
    for w in win:

        #If Player 1 wins
        if (sum(xst[w[0]], xst[w[1]], xst[w[2]])==3):
            printBoard(xst, zst)
            print(a," won !!")
            return 1
        
        #If Player 2 wins
        if (sum(zst[w[0]], zst[w[1]], zst[w[2]])==3):
            printBoard(xst, zst)
            print(b," won !!")
            return 0
        
        # If there is a draw in the game
        if all(xst[i] == 1 or zst[i] == 1 for i in range(9)):
            printBoard(xst, zst)
            print("It's a draw !!")
            return -1

    # If no winner or draw, the game is still ongoing
    return None

  
if __name__=="__main__":
    xst=[0,0,0,0,0,0,0,0,0]
    zst=[0,0,0,0,0,0,0,0,0]
    turn=1            # 1 for X and 0 for O

    a=input("Enter name of player 1 :  ")
    b=input("Enter name of player 2 :  ")

    print("-----Welcome to TIC TAC TOE Game----- ")

    while (True):
        printBoard(xst,zst)
        if (turn==1):
            print(a,"'s turn...")
            val=int(input("Enter value from the available values.. : "))
            xst[val]=1
        else:
            print(b,"'s turn...")
            val=int(input("Enter value from the available values.. : "))
            zst[val]=1

        c=checkWinner(xst, zst)
        if (c!= None):
            break
            
        turn=1-turn







        



