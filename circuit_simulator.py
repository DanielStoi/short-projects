"""
documentation:
simulates logic gates, in layers, where each logic gate
in a layer can get its input from output of previous layer
layers are run one by one

a layer is a collection of logic gates

*logic gate in layer format:
[[loc of input1],[loc of input 2],"operation"]

[loc of input1]-> [which layer, which item in layer]

"operation"-> "0101"
-first and second char is a not gate for input of logic gate
-3rd char is either 0,1,2 deciding if it's a and,or,xor gate overall
-4th bool char is weither to apply not gate to output

*logicGate_simulator class structure:
    -commands that change composition
    -commands that runs
    -command that outputs composition
    -all in one class


*runnining:
-gets input as first layer of neutral network
-perpetually runs next layer, using the bool output of the previous layers


*at the end of the program an example is run
"""
def logic(v1,v2,operation):
    p1,p2,op,p3=map(int,list(operation))
    i1=v1^p1
    i2=v2^p2
    ans=0
    if op==0: #and
        ans=(i1 and i2)
    elif op==1: #or
        ans= (i1 or i2)
    elif op==2: #xor
        ans= (i1 ^ i2)
    return ans^p3

class logicGate_neutralNetwork ():
    layercount=0
    layer=[]
    def init(self,layercount,inpnumb,outpnumb): #initiate or reset 
        self.layercount=layercount
        layer=[[]]*(layercount+2)
        layer[0]=[[]]*inpnumb
        layer[layercount+1]=[[]]*outpnumb
        
        self.layer=layer
    def setlayer(self,layernumb,info):
        self.layer[layernumb]=info
        return self.layer
    def run(self,inp):#debug run
        layervalues=[[]]*(self.layercount+2)
        layervalues[0]=inp
        for L in range(1,self.layercount+2):#L=layer
            curlayer=self.layer[L]
            Lval=[]
            for v in range(len(curlayer)):#v=each logic gate inside L
                loc1,loc2,operation=curlayer[v]
                #loc = [layer of output,numb]
                v1=layervalues[loc1[0]][loc1[1]]
                v2=layervalues[loc2[0]][loc2[1]]
                Lval.append(logic(v1,v2,operation))
            #update this current layer's output overall
            layervalues[L]=Lval
        return layervalues[self.layercount+1] #returns final layer output



    def printcontent(self):
        print("layer count: "+ str(self.layercount))
        print("layer information: "+ str(self.layer))
        print("read documentation to understand how layer information is set out")

#creating neural network
firstnet = logicGate_neutralNetwork()
firstnet.init(0,2,2)#layercount,inpnumb,outnumb
firstnet.setlayer(1,[ [[0,0],[0,1],"0000"], [[0,1],[0,0],"0020"]])

#running neural network, with input
print(firstnet.run([1,0]))

