# fibonacci serisi: Her eleman kendisinden önceki iki elemanın toplam seklinde ifade edilen fibonacci serisinin eleman degerlerini ozyinelemeli fonksiyon ile  bulup,
# ekrana yazdiran programi yaziniz.

def fib(n):
    a, b = 0 , 1
    while a < n:
        print(a, end=" ")
        a , b = b , a + b 
# Ana program
fib(1000)
