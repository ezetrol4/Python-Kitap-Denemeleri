# Klavyeden girilen her bir karakteri(sayı içermeyecek) alfabede kendisinden sonra gelen 13. karakter ile değiştiren (gerektiğinde "z" den "a" ya atlayacak şekilde) basit bir
# bir şifreleme programını yazınız.

# -+- coding: UTF-8 -*-

# Türkçe ROT13 fonksiyonu

def rot13(s):
    tKar = "ABCÇDEFGĞHİIJKLMNOÖPRSŞTUÜVYZ"
    donus = tKar[13:] + tKar[:13]
    rotKar = lambda c: donus[tKar.find(c)] if tKar.find(c) >-1 else c
    return '' .join(rotKar(c) for c in s)

# Ana program 

s = input("Metni giriniz..: ")
print(rot13(s.upper()))