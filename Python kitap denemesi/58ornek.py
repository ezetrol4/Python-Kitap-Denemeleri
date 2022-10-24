# 1'den 20'ye kadarki sayıların içerisinde çift olanları filtreleyip listeleyen programı kodlayınız.

def ciftS(sayi):
    return sayi%2==0
liste = range(1,20)
f_liste = filter(ciftS,liste)
print(list(f_liste))
