# 0-24 arasındaki çift sayıları listeleyen ve toplamını gösteren programı yazınız.

L = []
T = 0
for i in range (24):
    if i %2 ==0:
        L.append(i)
        T = T + i
        print(L)
print("Toplam=",T)