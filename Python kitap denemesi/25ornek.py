# Girilen yaş değerlerine göre kişinin içinde bulunduğu yaşam evresini verilen tabloya göre ekranda gösteren programı kodlayın.Girilen değerlere göre istenen program çıktısı:

yas = int(input("Kisinin yasini giriniz: "))

if yas <= 2:
    print("Kisi bebeklik cagindadir.")
elif yas <= 13:
    print("Kisi cocukluk cagindadir.")
elif yas <= 21:
    print("Kisi ergenlik cagindadir.")
elif yas <= 63:
    print("Kisi yetiskinlik cagindadir.")
else:
    print("Kisi yaslilik evresindedir.")
    