# Bilgayarın rastgele ürettiği 1-49 arasındaki 6 adet sayıyı sayısal loto çekiliş sonucu olarak ekrana yazan programı kodlayınız.

# sayisal loto
import random
def loto():
    for i in range(6):
        sL=random.randint(1,50)
        print(sL,end=" ")
#Ana program
print("Sayısal Loto Cekilisi \n")
loto()