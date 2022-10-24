# 1'den 100'e kadar olan sayılar, sırasıyla ekrana yazdırılacak fakat program; eğer sayı 3 veya 3'ün katıysa , sayı yerine "Fizz" veya 5 veya 5 'in katıysa , sayı yerine
#"Buzz"; eğer sayı hem 3'ün hem de 5'in katıysa , sayı yerine "FizzBuzz" yazmalıdır.

#FizzBuzz Oyunu


for x in range(1, 101):
    if x % 15 ==0:
        print("FizzBuzz" ,end=",")
    elif x % 3 ==0:
        print("Fizz" ,end=",")
    elif x % 5 ==0:
        print("Buzz")
    else:
        print(x,end=",")

print(x)