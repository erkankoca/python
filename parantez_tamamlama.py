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
def parantez(ifade):
    s=Stack()
    Liste=[]
    Liste=ifade.split()
    i=len(Liste)-2
    s.push(Liste[len(Liste)-1])
    while i>0:
        if Liste[i]==')':
                  k=0
                  while k<3:
                      s.push(Liste[i-k])
                      k=k+1
                  s.push('(')
		  s.push(Liste[i-k])
        elif Liste[i]=='*':
            s.push(Liste[i])
        i=i-1
    s.push('(')
    yazdir=[]
    while not s.isEmpty():
        yazdir.append(s.pop())
    return string.join(yazdir)
        
