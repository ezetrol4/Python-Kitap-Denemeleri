ST = 0
sqn=+1
n=int(input("Terim sayisi.: "))
for x in range(1, n + 1):
    ST = ST+(1/x)*sqn
    sqn =-sqn
print("Toplam=",ST)