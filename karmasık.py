class Karmasik:
    def __init__(self,sayi,imaj):
        self.n=sayi
        self.m=imaj
    def __str__(self):
        return str(self.n)+"+"+str(self.m)+"i"
    def show(self):
        print self.n,"+",self.m,"i"
    def __add__(self,foo):
        newn= self.n+foo.n
        newm= self.m+foo.m
        return Karmasik(newn,newm)
    def __sub__(self,foo):
        newn=self.n-foo.n
        newm=self.m-foo.m
        return Karmasik(newn,newm)
    def __mul__(self,foo):
        newn=self.n*foo.n+self.m*foo.m
        newm=self.n*foo.m+self.m*foo.n
        return Kearmasik(newn,newm)
    def __div__(self,foo):
        newn=(self.n*foo.n+self.m*foo.m)/((foo.n)**2+(foo.m)**2)
        newm=(self.n*foo.m-self.m*foo.n)/((foo.n)**2+(foo.m)**2)
        return Karmasik(newn,newm)
   def Mutlak(self,foo):
        z=((self.n-foo.n)**2+(self.m-foo.m)**2)**0.5
        return z
    
