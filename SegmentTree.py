"""
utilises lazy propogation, as to allow for the setting and retrevial of
key values within O(logn) time instead of O(n) on a normal list
takes O(n logn) space instead of O(n) space


uses the following operations:
-initiate segment tree with certain given (O(n log n) time and space)
-set a range of values
-increment a range of values by some number

queries:
-get minimum value or maximum within a given range


"""

class SegTree:
    A : list
    lower_bound : int
    upper_bound : int
    min_val : int
    set_to = False
    increment = 0
    L: "SegTree"
    R: "SegTree"
    
    def __init__(self,A : list,lower_bound : int,upper_bound : int):
        self.A = A
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

        if lower_bound != upper_bound:
            mid = (lower_bound+upper_bound)//2
            self.L = SegTree(A,lower_bound, mid)
            self.R = SegTree(A,mid+1,upper_bound)
            self.min_val = min(self.L.min_val,self.R.min_val)
        else:
            self.min_val = A[lower_bound]
            

    def incr(self,low,up,i):
        l = self.lower_bound
        u = self.upper_bound
        
        if self.set_to: # propagate change dowards
            self.L.set(l,u,self.min_val)
            self.R.set(l,u,self.min_val)
            self.set_to = False

        if low <=l and up >= u: #covers
            self.increment += i
        elif not (l > up or low > u):#touches but isn't disjoint
            self.L.incr(low,up,i)
            self.R.incr(low,up,i)
            self.min_val = min(self.R.get_min(), self.L.get_min())
            
            
        
        
            
    def set(self,low,up,i):
        l = self.lower_bound
        u = self.upper_bound
        if low <=l and up >= u: #covers
            self.set_to = True
            self.min_val = i
            self.increment = 0
        elif not (l > up or low > u): # touches but isn't disjoint
            self.L.set(low,up,i)
            self.R.set(low,up,i)
            self.min_val = min(self.R.get_min(),self.L.get_min())
            
        
        
        
    def get_min(self):
        if self.set_to:
            return self.min_val
        return self.min_val+self.increment
        
                
                
"""     
testing           
a = SegTree([5,4,4,2,1,7],0,5)
print(a.A)
print("min: ",a.get_min()) # ans is 1
a.set(4,5,7)
print("min: ",a.get_min()) # ans is 2
a.set(3,5,7)
print("min: ",a.get_min()) # ans is 4

a = SegTree([5,4,4,2,1,7],0,5)
print(a.A)
print("min: ",a.get_min()) # ans is 1
a.incr(0,5,1)
print("min: ",a.get_min()) # ans is 2
a.set(4,5,7)
print("min: ",a.get_min()) # ans is 3
a.incr(3,5,-1)
print("min: ",a.get_min()) # ans is 2
a.set(3,5,7)
print("min: ",a.get_min()) # ans is 4
"""

