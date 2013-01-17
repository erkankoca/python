def Sirala(dizi = []):

    if len(dizi)<=1:

        return dizi

    else:

        mihenk = dizi[0]

        enKucuk = []

        enBuyuk = []

        for i in dizi[1:]:

                if i<=mihenk:

                        enKucuk.append(i)      

                else:

                        enBuyuk.append(i)                  

        return Sirala(enKucuk) + [mihenk] + Sirala(enBuyuk)
