# Girilen bir cumledeki harflerin ve kelimelerin sayisini veren programini yaziniz.

cumle = input("Cumle giriniz: ")
ksay = cumle.count(" ")
hsay = len(cumle)-ksay
print("Kelime sayisi..:", ksay + 1)
print("Harf sayisi..:", hsay)