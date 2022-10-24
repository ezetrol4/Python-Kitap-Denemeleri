# Fibonacci serisinin ilk 13 değerlerini veren ve altın oranı hesaplayan programı yazın.

yenis1 = 1
yenis2 = 1
eskiS = 0; sayac = 0
print("Fibonacci Serisi..:")
while True:
    print(yenis2)
    yenis2 = eskiS + yenis1
    eskiS = yenis1
    yenis1 = yenis2
    sayac = sayac + 1
    if sayac == 13: break
print("Altin Oran.: ",yenis1/eskiS)