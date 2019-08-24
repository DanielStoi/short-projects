"""
solves n^2-n^2 sodoku. No number can be in the same row, column or n-n box

test cases:
2
1 2 3 4
3 4 2 0
2 1 4 3
0 0 0 0

2
1 2 3 4
3 4 0 0
0 0 0 0
0 0 0 0

3
0 0 0 5 0 0 6 0 0
0 7 0 6 0 9 0 2 0
2 0 0 8 0 0 4 0 0
0 0 0 0 7 0 1 6 0
0 0 0 1 0 2 0 0 0
0 1 9 0 6 0 0 0 0
0 0 5 0 0 6 0 0 8
0 9 0 7 0 8 0 5 0
0 0 6 0 0 4 0 0 0

3
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0

4
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
"""


def get_game(inp):
    if(inp=="input"):
        x = int(input("Type in the size of the game,n so that the size of the game is n^2 by n^2 numbers: "))
        print("Now type in the numbers.")
        print("Seperate each number by a space, and represent the blank numbers as 0.")
        print("For each new row, start a new line.")
        board=[]
        for i in range(x**2):
            try: 
                board.append(list(map(int,input().split())))
            except:
                print("ERROR IN GET GAME by input")
                return(False)
            for k in board[i]:
                if not(0<= k <= x**2):
                    #print("ERROR IN GET GAME by input")
                    return(False)
            if(len(board[i]) != x**2):
                #print("ERROR IN GET GAME by input")
                return(False)
        return x,board

def prune_space(size,x,y):#place where no other of the same digit can be
    k=[]
    for i in range(size**2):
        k.append([y,i])
        k.append([i,x])
        sx=(x//size)*size
        sy=(y//size)*size
        k.append([int(sy+(i//size)),int(sx+(i%size))])
    return k

def copy_board(board):
    k=[]
    for y in board:
        k.append([])
        for x in y:
            if (type(x)==list):
                k[-1].append([])
                for i in x:
                    k[-1][-1].append(i)
            else:
                k[-1].append(x)
    return k

def print_board(board):
    #print(board)
    for y in board:
        s=[]
        #print(y)
        for i in y:
            if (type(i)==int):
                s.append(str(i))
            else:
                s.append("0")
        print(" ".join(s))

class game(object):
    past_game=False
    board=[]
    size=0
    def __init__(self,size,board):
        self.size=size
        poss=[]
        for y in board:
            poss.append([])
            for x in y:
                if (x==0):
                    w=list(range(1,size**2+1))
                    poss[-1].append(list(range(1,size**2+1)))
                else:
                    poss[-1].append(x)
        self.board=poss
    def p(self):
        print("size",self.size)
        print("board",self.board)
    def prune(self):#removes elements from probability space
        board=self.board
        size=self.size**2
        c=0
        c2=False
        for y in range(size):
            for x in range(size):
                if(type(board[y][x])==int):
                    t=board[y][x]
                    c+=1
                    for iy, ix in prune_space(self.size,x,y):
                        if(iy != y or ix != x):
                            if (type(board[iy][ix])==list):
                                if (t in board[iy][ix]):
                                    board[iy][ix].remove(t)
                                    c2=True
                            else:
                                if (t==board[iy][ix]):
                                    #print("ERROR WITHIN GAME CLASS by prune")
                                    #print("error by (y, x,iy,ix)",y,x,iy,ix)
                                    #print_board(board)
                                    return -1

        if(c==size**2):#game is completed
            return 2
        elif(c2): #at least 1 change has been made
            return 1
        return 0 # no changes have been made
                            

    def process(self):#checks if valid and adds certain outcomes to the game
        #print("PROCESS")
        board=self.board
        size=self.size
        for y in range(size**2):
            for x in range(size**2):
                if (type(board[y][x])==list):
                    if(len(board[y][x])==1):
                        board[y][x]=board[y][x][0]
                        #print("processed:",y,x)
                    elif(len(board[y][x])==0):
                        return False
        return True
                    
    def guess(self):#makes a guess
        board=self.board
        new_board = copy_board(board)
        #print("-----guess",new_board)
        #print(new_board==board)
        for y in range(self.size**2):
            for x in range(self.size**2):
                if(type(board[y][x])==list):
                    board[y][x]= board[y][x][0]
                    #print(new_board==board)
                    #print("YOOOOOOOOOOOOOo",new_board[y][x])
                    new_board[y][x].pop(0)
                    #print(new_board)
                    if(len(new_board[y][x])==1):
                        new_board[y][x]=new_board[y][x][0]
                    #print("V2",new_board)
                    PG= self.past_game
                    self.past_game=game(self.size,new_board)
                    self.past_game.past_game = PG
                    return True

                    
    def revert_guess(self):
        #print("-------revert guess")
        if(self.past_game==False):
            #print("ERROR WITHIN REVERT GUESS")
            return False
        #del(self.board)
        past_game=self.past_game
        self.board=past_game.board
        PG=past_game.past_game
        #del(self.past_game)
        self.past_game=PG
        return True
        
    def solve(self):
        c=1
        k=1
        while (c==1 and k<2000):
            k+=1
            #print("PRUNE")
            c=self.prune()
            if (c==-1):
                if (self.revert_guess()):
                    c=1
                    #print("guess reversed")
            
            while(not self.process()):
                #print("PROCESS MISTAKE")
                if not (self.revert_guess()):
                    c=-1
            if (c==0):
                #print("GUESS")
                self.guess()
                #print("FINISHED GUESS")
                c=1
                if(self.prune()==-1):
                    #print("PROCESS MISTAKE")
                    if not (self.revert_guess()):
                        c=-1
                
                
        if(c==2):
            board=self.board
            print("WIN")
            print_board(board)
        else:
            print("ERROR, wasn't solved")
            print(k)
            print(c)
x,board=get_game("input")
k=game(x,board)
k.solve()
