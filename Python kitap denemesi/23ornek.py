s1 = int(input("1. Sayiyi girin: "))
s2 = int(input("2. Sayiyi girin: "))
s3 = int(input("3. Sayiyi girin: "))

enb = s1

if s2 > enb :
    enb = s2
if s3 > enb:
    enb = s3
print("En büyük sayi :", enb)