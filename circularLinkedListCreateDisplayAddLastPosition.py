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

    def createCircularList(self,e):
        newnode=_Node(e,None)
        if self._size == 0:
            self._head=newnode
            print("The List was updated with a node with value{}".format(e))
        elif self._size == 1:
            self._head._next=newnode
            self._tail=newnode
            self._tail._next=self._head
            print("The List was updated with a node with value{}".format(e))
        else:
            self._tail._next=newnode
            self._tail=newnode
            self._tail._next=self._head
            print("The List was updated with a node with value{}".format(e))
        self._size+=1
        
    def displayCircularList(self):
        p=self._head
        length=1
        print(self._size)
        if self._size !=0 :
            while length <= self._size :
                print(p._element,end="---->")
                p=p._next
                length+=1
            self.displayLastNode()
        else:
            print("The Circular List is Empty")
    def displayLastNode(self):
        p=self._head
        length = 1
        if self._size != 0:
            while length <= self._size :
                length+=1
            print(p._element)
    '''Adding Last Position Insertion Operation'''
    def addLastPosition(self,e):
        newnode=_Node(e,None)
        if self._size > 0:
                self._tail._next=newnode
                newnode._next=self._head
                self._size+=1
        else:
            print("The Circular List is Empty")



l=linkedList()
l.createCircularList(10)
l.displayCircularList()

l.createCircularList(20)
l.addLastPosition(500)
l.displayCircularList()

    
    
