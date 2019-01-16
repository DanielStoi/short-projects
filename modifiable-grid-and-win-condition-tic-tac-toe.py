#basic setup functions
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





#mechanics 
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
    dx, dy = d
    if CONTAINS(loc,[coordinates[0]+dx,coordinates[1]+dy]):
        print(str([coordinates[0]+dx,coordinates[1]+dy,streak,d]))#debugging
        if streak==winCond-1:
            return True
        else:
            return checksurroundings(loc, [coordinates[0]+dx,coordinates[1]+dy],streak+1,winCond,d)
    else:
        return False

    
    
def checkWin(loc,player,winCond):
    #loc[player] is the collection of all places where the player has moved
    for i in loc[player]:
        for d in [[0,1],[1,1],[1,0],[1,-1]]:
            if checksurroundings(loc[player],i,1,winCond,d)== True:
                print(player+" wins")
                return True
    else:
        return False


def humanplay(board,player,loc):
    move = INPUT("input move: (\"x y\")","LI2")

    #check move is valid, and updates the board
    if (0<=move[1] and move[1]<len(board) ) and (0<=move[0] and move[0]<len(board[0])):
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


  
def machineplay(boardSize,board,player,loc): #does nothing yet
    pass







#game     
def intro():
    print("hello humans")
    print("this is an attempt to create an more advanced game of tictaktoe")
    print("of course, no user interface is utilized")
    print("but...")
    print("this game has the option to change board size")
    print("in addition to changing the amount of consecutive tiles")
    print("-------------------------------------------------------")

   
        
        
def init(): #initiation of run function, or of a game
    print("-------------------------------------------------------")
    play = input("would you like to play? (\"Y\")")
    manOrMachine = "HH"
    if play == "Y":
        boardSize = INPUT("input board size: (\"width length\")","LI")
        winCond = INPUT("how much consecutuve tiles to win? (int)","I")
        return play,boardSize,winCond
    return play,0,0



def run():
    play, boardSize,winCond = init()
    #play="Y"
    #boardSize = [5,5] #remove after testing
    #winCond= 3

    
    if play != "Y":
        return False
    else:
        turn = 1 #it is player 1's turn if true, else p2's turn
        board = []
        loc = {"X":[],"O":[]}
        
        for x in range(boardSize[1]):   #creates board
            board.append(["_"] * boardSize[0])
        printBoard(board)

        run = True
        
        while run:

            player= playerToXO (bool(turn%2))
                
            board,loc = humanplay(board, player,loc)
            printBoard(board)
            run = (not checkWin(loc,player,winCond))
            
            turn+=1
            
        
        return True



def game():
    playing = True
    intro()
    while playing:
        playing = run()

