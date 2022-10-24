# Girilen bir metnin Palindrom olup olmadığını bulan programı yazınız.

s = input("Bir metin gir.:")
if s == '' .join(reversed(s)):
    print(s, ":palindron")
else:
    print(s, ":palindron değil")