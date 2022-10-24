# Girilen rakam degerine gore yilin kacinci ayi oldugunu hesaplayip ekranda gosterilen programi yaziniz[Ay degerleri 1 ile 12 arasinda girilmezse kullaniciya uyari mesajı
# verilecektir] 

L = ["Ocak","Subat","Mart","Nisan","Mayis","Haziran","Temmuz","Agustos","Eylul","Ekim","Kasim","Aralik"]

ay = int(input("Kacinci ay..:"))
if ay > 0 and ay <= 12:
    print(ay,".ay..:"+ L[ay-1])
else:
    print("Hatali ay numarasi!")