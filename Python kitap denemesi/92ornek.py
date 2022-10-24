#Girilen para miktarını şuanda kullanılmakta olan para kupurlerine "200-100-50-20-10-5-1-0.5" göre en az sayıda kupur ile ödemek için bir veznedara yardımcı olucak program yazınız.

kupur = [200,100,50,20,10,5,1,0.5]
para = float(input("Para miktari..:"))
for i in range(8):
    sayi=float(para)//kupur[i]
    if sayi !=0:
        print(sayi,"adet",kupur[i])
        para = para - sayi * kupur[i]
        
