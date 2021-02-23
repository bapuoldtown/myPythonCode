class myHashOpenAddress:
    def __init__(self,size):
        self.size=size
        self.listlevel=[None for _ in range(self.size)]
    def isEmpty(self):
        for j in self.listlevel:
            if j is None or j == id(self.listlevel):
                return True
        return False
    
    def insert(self,a):
        if self.isEmpty():
            if a > 0:
                hash=a%self.size
            else:
                hash=-(a)%self.size
            if self.listlevel[hash] is None or self.listlevel[hash] == id(self.listlevel):
                self.listlevel[hash]=a
            else:
                if hash == len(self.listlevel)-1:
                    for i in range(len(self.listlevel)):
                        if self.listlevel[i] is None or self.listlevel[i] == id(self.listlevel):
                            self.listlevel[i]=a
                            break
                else:
                    for i in range(hash,len(self.listlevel)):
                        if self.listlevel[i] is None or self.listlevel[i] == id(self.listlevel):
                            self.listlevel[i]=a
                            break
        return False
    def search(self,a):
        for i in self.listlevel:
            if i == a:
                return True
        return False
    
    def display(self):
        return self.listlevel
    
    def delete(self,a):
        for i in range(len(self.listlevel)):
            if self.listlevel[i] == a:
                self.listlevel[i]=id(self.listlevel)
                break
        return False

'''Instantiate the class'''
h=myHashOpenAddress(7)

'''Perform Serach,insert,delete,display operations on a hash table by implementing open addressing as the collision detection handler'''
print(h.display())

h.insert(10)
h.insert(49)
h.insert(56)

h.insert(52)
h.insert(72)
h.insert(69)
h.insert(83)


print(h.display())

print(h.search(-1))
print(h.search(83))

print(h.display())

print(h.delete(10))


print(h.display())

h.insert(-2)

print(h.display())
h.delete(-2)
h.delete(52)
h.insert(-1)

print(h.display())

