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
def infixtoprefix(infix):
    prec= {}
    prec["*"]= 3
    prec["/"]= 3
    prec["+"]= 2
    prec["-"]= 2
    prec[")"]= 1
    s= Stack()
    prefixlist= []
    liste=(infix.split())
    k=len(liste)-1
    while k>=0:
        if liste[k] in string.uppercase:
            prefixlist.append(liste[k])
            k=k-1
        elif liste[k]==')':
            s.push(liste[k])
            k=k-1
        elif liste[k]=='(':
            topk=s.pop()
            while topk !=')':
                prefixlist.append(topk)
                topk=s.pop()
            k=k-1
        else:
            while (not s.isEmpty()) and (prec[s.peek()]>=prec[liste[k]]):
                prefixlist.append(s.pop())
            s.push(liste[k])
            k=k-1
    while not s.isEmpty():
        prefixlist.append(s.pop())
    prefixlist.reverse()
    return string.join(prefixlist)
