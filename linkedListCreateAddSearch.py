'''My Structre of a linked list node'''
class _Node:
    __slots__=['_element','_next']

    def __init__(self,element,next):
        self._element=element
        self._next=next
'''The centralized class that has metjods to implement functions to add a node in the linked list,Search a node,Diaplay entire list,Disp;ay length of Linked List'''
'''The Node addition happens in a appending manner like A--->B--->C respectively'''
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
