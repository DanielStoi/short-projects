"""
isn't functional as of yet, while the basic framework of the program has been completed

what is it?
"each of a set of units in a mathematical model which have simple rules
governing their replication and destruction, used to model complex systems
composed of simple units such as living things or parallel processors."
-this will happen in a grid shape, with units representing the squares

aims to create a system that does this, with the ability to update frames
and to update the contents of the units manually.

automaton theory relates to cellular automaton andsounds interesting
which is somthing i might look into eventually.

max screen size is 80-80, although it can process more units (outside screen)




There are different types of commands, relating to:
-rendering/drawing=D  (sets focus if simulation is larger than what can fit inside a screen)
-running simulation=R (updates simulation, chooses how much times)
-Edit=E (following up statements can either update properties of the cells or change composition of simulation)
-Help=H (gives general info or specified information)    


Cells:
-choose conditions in which cells live or die.
-each cell looks different, but is a character
-charID

format of unitInfo:
unit of conditions= (U)
=> ([chars],countdiagonal?,countsides?,[rangeOfValuesThatActivates])

Cells=(C):
=>      "name":
        ([(U),(U),...],                      #multiply conditions,
        [ActivateIfMultCondNotMet?,(U),(U) ] #death conditions
        )       

unitInfo contains a list of cells:
=>unitInfo = {(C),(C)}
"""
class UI():
    def render(self,board,focus=[0,0]):
        print("   "+" ".join(list(map(str,list(range(focus[0],len(board[0])))))))
        for i, row in enumerate(board[focus[1]:]):
            print (str(i+focus[1])+"| "+"|".join(row[focus[0]:]))
    def getinput(self,text):
        while True:
            try:
                k= list(map(int,input(string).split()))
                if len(k)!=0:
                    print("wrong input format")
                    k=getinput(text)
                return k
            
            except:
                print("wrong input format")
                return getinput(text)
    def print(text):
        print(text)


    def printcellinfo(unitInfo):
        UI=UI()
        UI.print("current Cells:")
            pre="-"
            for cell in unitInfo: #this loop prints cell info
                UI.print("CELL: "+cell)
                UI.print(pre+"properties:")
                pre+="-"
                UI.print(pre+"multiply properties:")
                pre+="-"
                for U in unitInfo[cell][0]:
                    UI.print(str(pre+"applicable cells:"+str(U[0])+"countDiagonals?:"+str(int(U[1]))+"countSides?:"+str(int(U[2]))+"range of values"+str(U[4])))
                    pre+="-"
                pre="--"
                UI.print(pre+"death properties:")
                pre+="-"
                UI.print("dies if multiply condition false: "+ str(unitInfo[cell][1][0]))
                for U in unitInfo[cell][1][1:]:
                    UI.print(str(pre+"applicable cells:"+str(U[0])+"countDiagonals?:"+str(int(U[1]))+"countSides?:"+str(int(U[2]))+"range of values"+str(U[4])))




class Engine():
    UI = UI()
    unitInfo = {}
    board = []
    def __init__(self):
        x,y = self.UI.getinput("gamesize (\"width height\"):")
        x=int(x)
        y=int(y)
        UI.print("remember to type \"H\" for information, if u do not know how to play")
        for i in range(y):   #creates game
            self.board.append(["_"] * x)
            print(self.board)#for debug
            
            
    def processCommand(self):
        #different commands: R = draw current squares with a current focus,U=update n times,
        I=self.UI.getinput("next command:")
        if I[0]=="D": #draw/render
            self.UI.render(I[1:])
                
        if I[0]=="R": #run a stage in simulation
            pass
        if I[0]=="E": #edit
            edit(I[1:])
        if I[0]=="H": #help
            if len(I)>2:
                self.UI.print("wrong input format")
                processCommand()

    def checksurroundings(self,board,coord,info): # U = [chars],countdiagonal?,countsides?,[rangeOfValuesThatActivates]
        x=coord[0]
        y=coord[1]
        for U in info:
            c=0
            d=[]#,[dx,dy],...
            if U[1]==True:
                d.append([1,1])
                d.append([-1,1])
                d.append([1,-1])
                d.append([-1,-1])
            if U[2]==True:
                d.append([1,0])
                d.append([-1,0])
                d.append([0,1])
                d.append([0,-1])
            for dx,dy in d:
                try:
                    for potentialChar in U[0]:
                        if board[y+dy][x+dx]==potentialChar:
                            c+=1
                except:
                    pass
            for i in U[3]:
                if c==i:
                    return True
        return False
                
        

    def runSim(self,board,unitInfo):
        newboard=board
        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x]=="_": #check if square can be occupied
                    for key in unitInfo:
                        if checksurroundings(board,[x,y],unitInfo[key][0]):
                            newboard[y][x]=key
                            break

                else:#check for remove condition
                    change=False
                    if (unitInfo[board[y][x]][1][0]):
                        if not (checksurroundings(board,[x,y], unitInfo[board[y][x]][0]) ):
                            newboard[y][x]="_"
                            change=True
                    if change:
                        if checksurroundings(board,[x,y], unitInfo[board[y][x]][1][1:]):
                            newboard[y][x]="_"
        return newboard
                    
                
        
    def edit(self,I,unitInfo,board):
        if len(I)==0:
            self.UI.print("you are now in edit mode")
            I.append(self.UI.getinput("type \'cell\'or\'board\' to edit each respectivly"))
        if I[0]=="cell":
            self.UI.printcellinfo(unitInfo)
        elif I[0]=="board":
            


    
def RUN():
    playing=True
    while playing:
        game = Engine()
        running=True
        while running:
            game.processCommand()
        ask = UI.getinput("would you like to play again: (\'Y\')")
        if ask !="Y":
            playing=False
