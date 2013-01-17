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
def prefixeval(infix):
    s=Stack()
    liste=infix.split()
    k=len(liste)-1
    while k>=0:
        if liste[k] in "0123456789":
            s.push(int(liste[k]))
            k=k-1
        else:
            islenen2=s.pop()
            islenen1=s.pop()
            sonuc=islem(liste[k],islenen1,islenen2)
            s.push(sonuc)
            k=k-1
    return s.pop()
def islem(op,op1,op2):
    if op =="*":
        return op1*op2
    elif op =="/":
        if op1>op2:
            return op1/op2
        else:
            return op2/op1
    elif op =="+":
        return op1+op2
    else:
        return op1-op2
    
