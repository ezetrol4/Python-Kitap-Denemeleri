# Basit bir şifre/password sorgulaması yapan programı yazınız.(şifre elma olucak ve 3 kere yanlış girilirse bloke olucak)

sayac = 0
while True:
    sifre = input("password giriniz..:")
    if sifre == "elma":
        print("sifre dogru")
        break
    sayac+=1
    if sayac>=3:
        print("hakkiniz doldu")
        break