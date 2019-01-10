def INPUT(string,vartype):
    while True:
        try:
            k=0 #potentially remove
            if vartype == "LI":   #list with ints
                k= list(map(int,input(string).split()))
            elif vartype == "I": #int
                k=int(input(string))
            elif vartype == "2D":
                k=list(input(string))
                k=k[:2]
            elif vartype == "LI2":
                k= list(map(int,input(string).split()))
                if len(k) != 2:
                    print("--ANSWER FORM INCORRECT TRY AGAIN--")
                    k = INPUT()
                
            return k

        except:
            print("--ANSWER FORM INCORRECT TRY AGAIN--")

def CONTAINS (array,item): #outputs true or false depending if item is in array
    try: #supposed to be faster method compared to standard implementation
        b=array.index(item)
    except ValueError:
        pass
    else:
        return True
    return False


def printBoard(board):
    print("   "+" ".join(list(map(str,list(range(len(board[0])))))))
    
    for i, row in enumerate(board):
        print (str(i)+"| "+"|".join(row))


def playerToXO (player):
    if player==True:
        player="X"
        print("it is X's turn")
    elif player==False:
        player="O"
        print("it is O's turn")
    return player


def checksurroundings (loc, coordinates,streak,winCond,d):
    if d==0: d=[[0,1],[1,1],[1,0],[1,-1]]
    for dx,dy in d:
        if CONTAINS(loc,[coordinates[0]+dx,coordinates[1]+dy]):
            if streak==winCond-1:
                return True
            else:
                return checksurroundings(loc, [coordinates[0]+dx,coordinates[1]+dy],streak+1,winCond,d)
    else:
        return False
    
    
def checkWin(loc,player,winCond):
    #loc[player] is the collection of all places where the player has moved
    for i in loc[player]:
        if checksurroundings(loc[player],i,1,winCond,0)== True:
            print(player+" wins")
            return True
    else:
        return False
        
def intro():
    print("hello humans")
    print("this is an attempt to create an more advanced game of tictaktoe")
    print("of course, no user interface is utilized")
    print("but...")
    print("this game has the option to change board size")
    print("in addition to changing the amount of consecutive tiles")
    
    print("in addition to playing against a perfect AI, which tells you the expected and inevitable result of the game")
    print("this is my first time in python creating something this large, from scratch")
    print("this requires extensive usage of functions")

   
        
        
def init(): #initiation of run function, or of a game
    play = input("would you like to play? (\"Y\")")
    #manOrMachine = input("decide which player is an AI.(HH,AA,AH,HA)")
    manOrMachine = "HH"
    boardSize = INPUT("input board size: (\"width length\")","LI")
    winCond = int(input("how much consecutuve tiles to win? (int)"))
    return play, manOrMachine, boardSize,winCond



def run():
    play, manOrMachine, boardSize,winCond = init()
    #play="Y"
    #boardSize = [5,5] #remove after testing
    #winCond= 3

    
    if play != "Y":
        return False
    else:
        turn = 1 #it is player 1's turn if true, else p2's turn
        board = []
        loc = {"X":[],"O":[]}
        for x in range(boardSize[0]):
            print()
            board.append(["_"] * boardSize[1])
        printBoard(board)

        run = True
        
        while run:

            player= playerToXO (bool(turn%2))
                
            board,loc = humanplay(board, player,loc)
            printBoard(board)
            run = (not checkWin(loc,player,winCond))
            
            turn+=1
            





        
        return False #only 1 game

def game():
    playing = True
    #intro()
    while playing:
        playing = run()




def humanplay(board,player,loc):
    move = INPUT("input move: (\"x y\")","LI2")

    #check move is valid, and updates the board
    if (0<=move[1] and move[1]<len(board) ):
        if board[move[1]][move[0]]=="_":
            board[move[1]][move[0]]=player
            loc[player].append(move)
            return board,loc
        else:
            print("this spot is full try again")
            return humanplay(board,player,loc)
    else:
        print("this spot is invalid")
        return humanplay(board,player,loc)




    
def machineplay(boardSize,board,player,loc):
    pass

