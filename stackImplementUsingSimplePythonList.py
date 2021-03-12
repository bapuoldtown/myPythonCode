class _Stack:
    def __init__(self):
        self._data=list()
        self._size=0
        self._head=None
        self._tail=None
    def _length(self):
        return len(self._data)
            
    def _isEmpty(self):
        if self._length() > 0:
            return True
        return False
    def _push(self,e):
        if self._length() > 0:
            if self._length() == 1:
                self._data.append(e)
                self._tail=self._data[self._length()-1]
            else:
                self._data.append(e)
                self._tail=self._data[self._length()-1]
        else:
            self._data.append(e)
            self._head=self._data[0]
            self._tail=self._data[0]
        print("After Push size is {}".format(self._length()))

    def _top(self):
        if self._tail:
            return self._tail
        else:
            return "Stack is Empty"
    def _pop(self):
        if self._length() > 0:
            ele=self._data.pop()
            self._tail=self._data[self._length()-1]
            return "{} Popped, The size after the pop operation is {}".format(ele,self._length())
        else:
            return "Stack is Empty"
        
s=_Stack()

s._push(10)
s._push(20)

print("The top most element is {}".format(s._top()))

s._pop()
print("The top most element is {}".format(s._top()))


s._push(30)
print("The top most element is {}".format(s._top()))
s._push(40)
print("The top most element is {}".format(s._top()))
s._push(50)
print("The top most element is {}".format(s._top()))

s._pop()
print(s._pop())

print("The top most element is {}".format(s._top()))


