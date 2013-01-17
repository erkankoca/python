class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self):
        self.items.insert(0,item)
    def pop(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)
def tabandegis(sayi,taban):
    degerler = "0123456789ABCDEF"
    stack = Stack()
    while sayi > 0:
        rem = sayi % taban
        stack.push(rem)
        sayi = sayi / taban
    string = ""
    while not stack.isEmpty():
        string = string + degerler[stack.pop()]
    return string

