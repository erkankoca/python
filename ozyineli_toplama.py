def topla (dizi=[]):
    if len(dizi)==1:
        return dizi[0]
    else:
        return dizi[0]+topla(dizi[1:])
