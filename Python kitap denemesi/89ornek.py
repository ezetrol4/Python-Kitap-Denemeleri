import re
email = input("e-mail adresini gir:")
rMailkontrol = r"^[\w\.\+\-]+\@[\w]+\.[a-z]{a-z}$"
# e mail kontrol stringi
m = re.search(rMailkontrol, email)

if m:
    print("gecerli bir adres:", m.group())
else:
    print("gecersiz bir adres, lutfen yeniden giriniz!!")
    