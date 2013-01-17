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
def fonk(n):
    s=Stack()
    denge=True
    i=0
    while i<len(n) and denge:
        k=n[i]
        if k in "({[":
            s.push(k)
        else:
            if s.isEmpty():
                denge=False
            else:
                eleman=s.pop()
                if not olaylar_olaylar(eleman,k):
                    denge=False
        i=i+1
    if s.isEmpty() and denge:
        return True
    else:
        return False
def olaylar_olaylar(ismail_abi,erdal_bakkal):
    mecnun="({["
    iskender=")}]"
    return mecnun.index(ismail_abi)==iskender.index(erdal_bakkal)

