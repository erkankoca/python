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
def infixtopostfix(infix):
    prec= {}
    prec["*"]= 3
    prec["/"]= 3
    prec["+"]= 2
    prec["-"]= 2
    prec["("]= 1
    s= Stack()
    postfixlist= []
    liste= infix.split()
    for i in liste:
        if i in string.uppercase:
            postfixlist.append(i)
        elif i=='(':
            s.push(i)
        elif i==')':
            topi=s.pop()
            while topi !='(':
                postfixlist.append(topi)
                topi=s.pop()
        else:
            while (not s.isEmpty()) and (prec[s.peek()]>=prec[i]):
                postfixlist.append(s.pop())
            s.push(i)
    while not s.isEmpty():
        postfixlist.append(s.pop())
    return string.join(postfixlist)


