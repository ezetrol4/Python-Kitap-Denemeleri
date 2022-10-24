i = 1
n = int(input("Tavan sayisi: "))
while i <= n:
    if i % 2 ==0:
        kup = i * i * i
        print(i,"Deger :",kup)
        i = i + 1
    else:
        kare = i * i
        print(i,"Deger :",kare)
        i = i + 1