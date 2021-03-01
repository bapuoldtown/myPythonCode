"""Added the Fnction to add at any position  of the linked list"""
class _Node:
    __slots__=['_element','_next']
    def __init__(self,element,next):
        self._element=element
        self._next=next

class linkedList:
    def __init__(self):
        self._head=None
        self._tail=None
        self._size=0
    
    def __len__(self):
        return self._size
    def isEmpty(self):
        return self._size == 0
    def addNode(self,e):
        newnode=_Node(e,None)
        if self.isEmpty():
            self._head=newnode
            self._tail=newnode              
        else:
            if self._head._next is None:
                    self._head._next=newnode
                    self._tail=newnode
            else:
                    self._tail._next=newnode
                    self._tail=newnode
        self._size+=1
    def firstPosition(self,e):
        newnode=_Node(e,None)
        newnode._next=self._head
        self._head=newnode
        self._size+=1


    def displayList(self):
        p=self._head
        while p:
            print(p._element,end="--->")
            p=p._next
        print("\n")
    def searchList(self,e):
        p=self._head
        index=0
        flag =0
        while(p):
            if p._element == e:
                print("{} is present at  position {} of the linked list".format(p._element,index+1))
                flag=1
                break
            p=p._next
            index+=1
        if flag == 0:
            print("Element could not be Found")
    def addAnyPosition(self,e,pos):
        if pos >= self._size:
            return "You are trying to insert an element in a position beyond its existing size"

        newnode=_Node(e,None)
        prev=self._head
        curr=prev._next
        idx=0
        while curr:
            if pos == idx+1:
                prev._next=newnode
                newnode._next=curr
            idx+=1
            prev=prev._next
            curr=curr._next
        self._size+=1
        return "Insertion successful"
    def deleteFirstNode(self):
        if self._head:
            p=self._head
            self._head=p._next
            p._next=None
            return "current First element has been deleted from the chain"
        return "There are no elements that need to be inserted into the linked list chain"

l=linkedList()
l.addNode(70)
l.addNode(80)
l.addNode(90)

l.displayList()
print(len(l))

l.searchList(8)

l.firstPosition(10)
print(len(l))

l.displayList()
print(l.addAnyPosition(100,2)) #Consider first position as 0 ,second as 1 like array
print(len(l))
l.displayList()

print(l.deleteFirstNode())
l.displayList()


