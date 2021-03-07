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
    '''Adding Any Position Insertion Operation (works well for insertion at the end too!!! '''
    def addAnyPosition(self,e,pos):
        newnode=_Node(e,None)
        length=1
        ref=None
        p=self._head
        if self._size > 0:
            while length <= self._size:
                if length+1 == pos:
                    ref=p._next
                    p._next=newnode
                    newnode._next=ref
                    print("The Node has been added at the position :{}".format(pos))
                p=p._next
                length+=1
            self._size+=1
        else:
            print("The Circular Linked List is Empty")



l=linkedList()
l.createCircularList(10)

l.createCircularList(20)
l.createCircularList(500)
l.displayCircularList()

l.addAnyPosition(300,2)
l.displayCircularList()

    
    
