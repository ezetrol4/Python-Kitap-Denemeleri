# Bir tavan/üst sayısı girildikten sonra 1'den başlayan ve seçilen üst sayıya kadarki sayıların karesini ekrana yazan programı while döngüsü ile kodlayınız.Programın örnek çıktıısı;

i = 1
n = int(input("Tavan sayisini girin: "))

while i <= n:
    kare = i * i
    print(i,"İn karesi = ",kare)
    i = i + 1 
    