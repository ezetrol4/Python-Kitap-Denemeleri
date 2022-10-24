# Dört işlem (toplama çıkarma ve bölme ) yapan bir hesap makinesi programını kodlayınız.(Sayı girişi ve işlem operatörü klavyeden girilecek.)

s1 = int(input("ilk sayiyi giriniz = "))
s2 = int(input("İkinci sayiyi giriniz = "))
op = input("İslemi Giriniz : ")

if (op == "+"):
    S = s1 + s2
elif (op == "-"):
    S = s1 - s2
elif (op == "*"):
    S = s1 * s2
elif (op == "/"):
    S = s1 / s2
else :
    print ("Hatali Secim")
print("Sonuc = ", S)