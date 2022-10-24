# Bilgisayarın rastgele ürettiği iki sayı (a,b) arasındaki tek sayıları listeleyen ve bu tek sayıların adedini veren programını yazınız.

def Tek(s1,s2):
    sayac=0
    if s1%2 !=0:
        for i in range(s1,s2+1,+2):
            print(i,end="")
            sayac+=1
        else:
            for i in range(s1+1,s2+1,+2):
                print(i,end="")
                sayac+=1
        return sayac
#Ana program.

import random
a=random.randint(1,100)
b=random.randint(1,100)
print("s1=",a,"\ns2=",b)
if a>b:
    a,b=b,a
print("\nAdedi.:",Tek(a,b))
