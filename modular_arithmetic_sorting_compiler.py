"""
How do you sort a bunch of integers from input using only the opperations:
%,/,+,*,-
without any loops, or conditional staitments (if, else, ect)?

This python program generates code in C that is capable of sorting
n numbers from input. Just enter the amount of integers it will be sorting
and the code will be generated.

The C program itself gets input through the function Scanf and prints using
printf
"""
def setUp(VarNum):
    #sets up the integers being entered as in, where n is the order in addition
    #to initializing the sorted variables
    ans=""
    for i in range(VarNum):
        ans+="int "+"i"+str(i)+";"+"\n"
        ans+="printf(\"Enter integer:\");\n"
        ans+= "scanf(\"%d\", &i"+str(i)+");\n"
        ans+="int sort"+str(i)+"; \n"
    ans+="int i"+str(VarNum)+"; \n"
    ans+="int check = 1;\n"
    return ans

def G(a,b):
    ans= "(1%(((i"+str(a)+" + 1) / (i"+str(b)+" + 1))+1))"
    return (ans)
def greatestCheckStr(VarNum,f):#expression that returns 0 if a number is the greatest
    ans="1"
    for i in range(VarNum):
        if i !=f:
            ans+="*"+G(f,i)
    return ans
#everything correct as of yet

def getgreatestStr(VarNum):
    ans="0"
    for i in range(VarNum):
        ans+= " + (i"+str(i)+"*"+"("+str(greatestCheckStr(VarNum,i))+")"+")"
    return ans
#works
def greatestamountStr(VarNum):#gets expression that finds the amount of biggest functions
    ans="0"
    for i in range(VarNum):
        ans+= "+"+str(greatestCheckStr(VarNum,i))
        
    return ans



def Step (VarNum,current):#finds the next largest number and assigns it to int sorkn
    ans="sort"+str(current)+" = "+"("+getgreatestStr(VarNum)+")"+"/"+"("+str(greatestamountStr(VarNum))+")"+"; \n"
    ans+="i"+str(VarNum)+"= sort"+str(current)+"; \n"
    ans+="check = 1; \n"
    for i in range(VarNum):
        ans += "i"+str(i)+"="+" i"+str(i)+"*(1-("+str(greatestCheckStr(VarNum+1,i))+"*check));\n"
        ans+= "check = check * (1-"+str(greatestCheckStr(VarNum+1,i))+");\n"
    return ans                                                         
           

def Body(VarNum):
    ans=""
    ans+=setUp(VarNum)
    for i in range(VarNum):
        ans+=Step(VarNum,i)
    ans+="printf(\""+(" %d"*VarNum)+"\""
    for i in range(VarNum):
        ans+= ", sort"+str(i)
        

    ans+=");\n"



    return ans

def GenerateFullProgram(VarNum):
    ans="#include <stdio.h>\nint main (void) { \n"
    ans+=Body(VarNum)
    ans+="\n}"
    return ans
k=int(input("how many integers do you want the generated program to sort?:"))
print(GenerateFullProgram(k))
    
        
