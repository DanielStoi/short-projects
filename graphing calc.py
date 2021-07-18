
def calculator(text):
    vals = []
    operations = []
    operators = ["/","*","+","-"]
    i = 0
    depth = 0
    start_depth = -1
    while i < len(text):
        if text[i] == '(':
            depth+=1
            if start_depth == -1:
                start_depth = i+1
            i+=1
        
        if depth == 0:
            if text[i].isnumeric() or (text[i]=='-'):

                valid = False
                if i == 0:
                    valid = True
                else:
                    if text[i-1] in operators:
                        valid = True
                
                if valid:
                    start = i
                    i+=1
                    while i < len(text):
                        if text[i].isnumeric():
                            i+=1
                        else:
                            break
                    vals.append(''.join(text[start:i]))
                else:
                    operations.append(text[i])
                    i+=1

            elif text[i] in operators:
                operations.append(text[i])
                i+=1


        elif text[i] == ')':
            depth-=1
            if depth == 0:
                vals.append(''.join(text[start_depth:i]))
                start_depth = -1
            i+=1
        else:
            i+=1


    
    
    if not operations:
        if vals[0].isnumeric() or (vals[0][0] == '-' and vals[0][1:].isnumeric()):
            return int(vals[0])
        else:
            return calculator[vals[0]]



    i = len(operations)-1
    while i >= 0:
        if operations[i] in ['/']:
            vals[i] = str(calculator(vals[i])/calculator(vals[i+1]))
            vals.pop(i+1)
            operations.pop(i)
        i-=1

    i = len(operations)-1
    while i >= 0:
        if operations[i] in ['*']:
            vals[i] = str(calculator(vals[i])*calculator(vals[i+1]))
            vals.pop(i+1)
            operations.pop(i)
        i-=1

    

    i = len(operations)-1
    while i >= 0:
        if len(operations)==1 and len(vals) == 1:
            return calculator(vals[0])*-1
        
        if operations[i] in ['-']:
            vals[i] = str(calculator(vals[i])-calculator(vals[i+1]))
            vals.pop(i+1)
            operations.pop(i)
        i-=1

    i = len(operations)-1
    while i >= 0:
        if operations[i] in ['+']:
            vals[i] = str(calculator(vals[i])+calculator(vals[i+1]))
            vals.pop(i+1)
            operations.pop(i)
        i-=1
        
    return int(vals[0])


def calculate_x(text, x_val):
    i = 0
    while i < len(text):
        if text[i] == 'x':
            
            text = text[:i]+str(x_val)+text[i+1:]
        i+=1

    return calculator(text)




def graph(text, x1, x2, y1,y2):
    x_vals = [x1,x2]
    y_vals = [y1,y2]
    board = []
    for i in range(y_vals[0],y_vals[1]):
        y = list()
        for w in range(x_vals[0],x_vals[1]):
            y.append(' ')
        board.append(y)
    
    for x_val in range(x_vals[0],x_vals[1]):
        y = calculate_x(text,x_val)
        y = min(y,y_vals[1])
        y = max(y,y_vals[0])
        board[y-y_vals[0]-1][x_val-x_vals[0]-1]= '*'
    for line in board[::-1]:
        print(''.join(line))
    





print("please type in the function")
while (True):
    function = input("please type in the function: ")
    print("please but in a space between the following numbers")
    metrics = input("please type in the  lower x, upper x,  lower y, upper y:")
    m = list(map(int, metrics.split()))
    graph(function,m[0],m[1],m[2],m[3])
