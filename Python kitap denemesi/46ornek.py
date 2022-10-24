# Ekrana 1'den 7'den 1'e kadar "*" karakterlerinden oluşan dik üçgeni ve ters dik üçgeni çizen programı yazın.

for i in range(7):
    for j in range(i+1):
        print("*", end="")
    print("")