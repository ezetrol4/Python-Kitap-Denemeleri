# n sayısının faktoriyelini hem normal hem de ozyinemeli fonksiyonla kodlayınız.

# faktöriyel fonksyiyonu
def fakt(n):
    f = 1
    for n in range(n,0,-1):
        f = f * n
    return f

# Ana program

n = int(input("Faktoriyel sayisi.:"))
print(n,"!=", fakt(n))