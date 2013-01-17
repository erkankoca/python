#kullanıcıdan tek veya cok secmelı soru ısteyen program
class Soru:
    def __init__(self):
        self.soru=raw_input("Soru cumlesi:")
class Secenek:
    def __init__(self):
        self.secenek1=raw_input("Secenek 1 :")
        A = raw_input("doðrumu E\H :" )
        self.dogru=[]
        if A =="E" :
            self.dogru.append("A")
        self.secenek2=raw_input("Secenek 2 :")
        B = raw_input("doðrumu E\H :" )
        if B =="E" :
            self.dogru.append("B")
        self.secenek3=raw_input("Secenek 3 :")
        C = raw_input("doðrumu E\H :" )
        if C =="E" :
            self.dogru.append("C")
        self.secenek4=raw_input("Secenek 4 :")
        D = raw_input("doðrumu E\H :" )
        if D=="E" :
            self.dogru.append("D")
        self.secenek5=raw_input("Secenek 5 :")
        E = raw_input("doðrumu E\H :" )
        if E =="E" :
            self.dogru.append("E")
class Dogru:
    def __init__(self):
        cvp = raw_input ("Cevabiniz =")
        if cvp in self.dogru:
            print("dogru cevap")
        else:
            print("yanlis zaa")
       
class SoruCTS(Soru,Secenek,Dogru):
# çoktan tek seçmeli soru sınıfı
    def __init__(self):
        Soru.__init__(self)
        Secenek.__init__(self)
        
    def sor(self):
        print self.soru
        print "A) ",self.secenek1
        print "B) ",self.secenek2
        print "C) ",self.secenek3
        print "D) ",self.secenek4
        print "E) ",self.secenek5
        Dogru.__init__(self)

class SoruCCS(Soru,Secenek,Dogru):
#çoktan çok seçmeli soru sınıfı
    def __init__(self):
        Soru.__init__(self)
        Secenek.__init__(self)     
                
    def sor(self):
        print self.soru
        print "A) ",self.secenek1
        print "B) ",self.secenek2
        print "C) ",self.secenek3
        print "D) ",self.secenek4
        print "E) ",self.secenek5
        Dogru.__init__(self)

