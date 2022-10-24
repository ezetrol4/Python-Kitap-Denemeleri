# üç kenar uzunluğu verilen bir üçgenin alanını hesaplayan programı kodlayınız.

a = int(input("1. Kenarının degerini giriniz: "))
b = int(input("2. Kenarının degerini giriniz: "))
c = int(input("3. Kenarının degerini giriniz: "))

#üçgenin yarı çevresi

u = (a+b+c)/2

# Alanı

alan = (u*(u-a)*(u-b)*(u-c))**0.5
print("Alan =", alan)
