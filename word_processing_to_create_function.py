"""
type in a function, using how many variables you want, in any location, able to use (,),*,/,^,+,- as operators
when running this program, defult is 1 variable, "x" which is set to 5.

getfunctionfrominput(str)->
gets a string and turns in into a function, can have multiple variables
spacing is unimportant

calculate(funct,varValues) ->
gets function as returned by getfunctionfrominput(), and list of variables
with corresponding values (in dictionary form) to return the answer

eg:
from word_processing_to_creat_function import *
varValues = {"x":25,"y":151,"z":231}
funct=getfunctionfrominput(" z ^ ( y  ^  x  ) ")
ans= calculate(funct,varValues)
print(ans)

"""
def digit(dd,pfct):
    if len(dd)>0:
        pfct.append(dd)
    dd=""
    return [dd,pfct]
def getfunctionfrominput(rfct):
    #get function from string, in the form of a list containing:
    #operations, variables,numbers,sub functions(or other lists)
    #this will be processed by 
    pfct = []
    dd="" #for grouping things into digits
    #print("----")
    i=0
    while i<len(rfct):
        #print(rfct[i])
        for d in range(10):
            if rfct[i]==str(d) or rfct[i]==".":
                dd+=rfct[i]
                rfct[i]=" "
                break
        else:
            [dd,pfct]=digit(dd,pfct)
        if rfct[i]=="(":
            #print("yeet")
            [subf,di] = getfunctionfrominput(rfct[i+1:])
            #print([subf,di])
            pfct.append(subf)
            #print(pfct)
            i+=di
            #print(i)
            #print("(->"+rfct[i])
        elif rfct[i]==")":
            #print("yoot")
            #print(pfct)
            return [pfct,i+1]
        elif rfct[i]!=" ":
            pfct.append(rfct[i])
        i+=1
    [dd,pfct]=digit(dd,pfct)
    
    return pfct
                    




def calculate(funct, varValues):
    #first for loop finds the value of each "piece"
    #second loop finds the overall answer
    print("calc initiated")
    
    for i in list(range(len(funct)))[::2]:
        #item 2k+1 allways associates with a value
        if type(funct[i]) != list:
            try:
                funct[i]=float(funct[i])
            except:
                funct[i]=varValues[funct[i]]
        else:
            funct[i]=calculate(funct[i],varValues)
            print(funct)
        


    print()
    #item 2k allways associates with an operation (+,-,*,/,^)
    for i in list(range(len(funct)-1))[::-2]:
        if funct[i]=="^":
            funct[i-1]=funct[i-1]**funct[i+1]
            funct.pop(i+1)
            funct.pop(i)
    for i in list(range(len(funct)-1))[::-2]:
        if funct[i]=="*":
            funct[i-1]=funct[i-1]*funct[i+1]
            funct.pop(i+1)
            funct.pop(i)
    for i in list(range(len(funct)-1))[::-2]:
        if funct[i]=="/":
            funct[i-1]=funct[i-1]/funct[i+1]
            funct.pop(i+1)
            funct.pop(i)
    for i in list(range(len(funct)-1))[::-2]:
        if funct[i]=="-":
            funct[i-1]=funct[i-1]-funct[i+1]
            funct.pop(i+1)
            funct.pop(i)
    for i in list(range(len(funct)-1))[::-2]:
        if funct[i]=="+":
            funct[i-1]=funct[i-1]+funct[i+1]
            funct.pop(i+1)
            funct.pop(i)
            print(funct)
    
    
    return(funct[0])
    
    
k=getfunctionfrominput(list(input("type in function:")))
print(k)
print(calculate(k,{"x":5}))
