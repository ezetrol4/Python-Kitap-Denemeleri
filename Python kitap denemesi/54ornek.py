# Girilen üç sayı içerisinden en büyük ve en küçük olanları bulup ekranda gösteren programı yazın.

a, b, c = 3, 15, 9
def enb(x,y,z):
    return max(max(x,y),z)
def enk(x,y,z):
    return min(min(x,y),z)
print("En buyugu:",enb(a,b,c))
print("En kucuk:",enk(a,b,c))