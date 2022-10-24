# Sayı tahmin oyunu

import random
def tahmin(a):
    sayac,puan=0,100
    print("ilk tahmininiz..:");
    while True:
        tahmin =int(input())
        sayac+=1
        if tahmin == a:
            print("Bravo!", sayac," .de",a,"i bildiniz")
            break
        elif tahmin < a:
            print("Daha buyuk bir sayi gir!")
        else:
            print("Daha kucuk bir sayi gir!")
        puan-=10
    print("Puaniniz..:", puan)

# Ana program

tut = random.randint(1,100)
tahmin(tut)
