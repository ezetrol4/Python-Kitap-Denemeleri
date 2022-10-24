# Girilen bir sayıya (O ile N arası) kadar üçe bölünebilen sayıların ortalamasını bulan program gerçekleştiriniz.Örneğin klavyeden 16 sayısı girildiğinde ekrana (3+6+9+12+15)/5=9.0 yazacak.

sayac = 0
t = 0
n = int(input("Gir bir sayi.. :"))
x = n-(n % 3)
while x > 0:
    t = t + x
    x = x - 3
    sayac = sayac + 1
ort = t/sayac
print("Ortalama =", ort)