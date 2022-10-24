N = 100
asal = 5
print("1,2,3,5,7")
for i in range(7, N+1, +2):
    if(i%3!=0 and i%5!=0 and i%7!=0):
        asal = asal + 1
        print(i, end="")
print("\nAsal sayi adedi: ", asal)