# Bilgisayarın rastgele ürettiği iki sayının (m,n) OBEB'ini hesaplayan programını yazın.

def obeb(m,n):
    while m%n !=0:
        eskiM = m
        eskiN = n

        m = eskiN
        n = eskiM % eskiN
    return n
# Ana program
import random
m = random.randint(1,100)
n = random.randint(1,100)
print("OBEB({},{})={}".
format(m,n,obeb(m,n)))