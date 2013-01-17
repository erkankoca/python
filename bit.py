class Stack:
    def __init__(self):
         self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
import string
def bit_ayirma(n):
    i=0
    s=Stack()
    k=[]
    while n>1:
        s.push(n%2)
        n=n/2
    s.push(n)
    while not s.isEmpty():
        k.append(s.pop)
    return string.join(k)
