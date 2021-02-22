    """
     A Sample Program to implement single function hashing with chaining as a method to handle collision detection
    """


class HashChain:
    def __init__(self,level):
        self.level=level
        self.chainlist=[ [] for i in range(level)]
    def insert(self,a):
        self.levelindex=a%self.level
        #print(self.levelindex)
        #print(self.chainlist)
        self.chainlist[self.levelindex].append(a)
    def display(self):
        #print(self.levelindex)
        #print(self.chainlist)
        return self.chainlist
    def retrieve(self,b):
        self.levelindex=b%self.level
        #return "The requested item is in:"+str(self.levelindex)+" "+str(self.chainlist[self.levelindex].index(b))
        if self.chainlist[self.levelindex].index(b) != -1:
            return True
        else:
            return False
        
    
    def delete(self,c):
        if self.retrieve(c):
            self.chainlist[self.levelindex].remove(c)
            return self.display()
            #return "Element is present!!!"
            #self.chainlist[self.levelindex].remove(c)

        

inputentrylength=6

h=HashChain(inputentrylength)

h.insert(10)
h.insert(20)
h.insert(33)
h.insert(43)
h.insert(53)
h.insert(64)

print(h.display())
print(h.retrieve(64))

print(h.delete(10))
print(h.delete(64))
#print(h.display())



