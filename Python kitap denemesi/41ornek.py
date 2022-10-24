# Girilen iki pozitif tamsayının çarpımını,çarpma operatörü kullanılmadan hesaplayan programı for döngüsü ile kodlayınız.

carp = 0 # Gerçekte toplam değişkeni.
s1 = int(input("Sayi1.: "))
s2 = int(input("Sayi2.: "))
for x in range (s1):
    carp = carp + s2
#Döngü sonu
print(s1,"*" ,s2,"=" ,carp)