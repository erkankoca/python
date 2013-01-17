
def gcd(m,n):
    while m%n !=0:
        m,n=n,m%n
    return n
class kesir :
    def __init__(self,top,bottom):
        self.num= top
        self.den=bottom
    def show(self):
        print self.num , "/" ,self.den
    def __str__(self):
        return str(self.num)+"/"+str(self.den)
    def __add__(self,foo):
        newnum= self.num*foo.den + self.den*foo.num
        newden= self.den * foo.den
        a= gcd(newnum,newden)
        return Fraction(newnum/a,newden/a)
