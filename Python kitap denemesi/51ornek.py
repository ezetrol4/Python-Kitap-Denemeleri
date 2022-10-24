# ilk 100 sayı içerisindeki asal sayıları bulan, asal olmayanları ise çarpanlarına ayırarak gösteren program kodunu yazınız.

for n in range(2, 100):
    for x in range(2,n):
        if n % x == 0:
            print(n, "=" , x, "*", n//x)
            break
    else:
        print(n, "asal sayidir.")