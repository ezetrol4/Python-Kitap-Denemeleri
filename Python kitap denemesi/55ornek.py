# Ana programda(main fonksiyonda) girilen Fahrenhayt sıcaklığını (F) cevir isimli fonksiyonla Dereceye (C) ceviren ve çevrim sonucunu ana programda gösteren programı yazınız.

#cevir fonksiyonu

def cevir(f):
    return((f-32)/1.8)

#Ana program

f=float(input("Fahrenayt degeri:"))
C = cevir(f)
print(C ," derecedir")