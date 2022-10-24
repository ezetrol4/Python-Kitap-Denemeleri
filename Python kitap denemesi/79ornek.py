# Thue-Morse sırası/dizisi: "0,01,0110,01101001,..."  şeklinde devam eden bir dizidir. Bu sıranın/dizinin ilk 6 terimini veren python kodunu yazınız.

# Thue-Morse Uygulaması

m = "0"
print(m)
for i in range(0,5):
    m0=m
    m=m.replace("0","b")
    m=m.replace("1","0")
    m=m.replace("b","1")
    m=m0+m
    print(m)