# 1'den 10'a kadarki sayıların karesini alan programı map fonksiyonunu kullanarak kodlayınız.

def kare(a):
    return  a**2
sayi = range(1,10)
map_cikti = map(kare, sayi)
print(list(map_cikti))