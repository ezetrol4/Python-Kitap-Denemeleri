# Hesap makinesinin devamı

while True :
    s1 = int(input("s1.. :"))
    s2 = int(input("s2.. :"))
    op = input("islem..:")
    if (op=="+"):
        S = s1 + s2
    elif (op == "-"):
        S = s1 - s2
    elif (op == "*"):
        S = s1 * s2
    elif (op == "/"):
        S = s1 / s2
    else:
        ("Hatali Secim")
    print("Sonuc=", S)
    cvp = input("Devam etmek istiyor musunuz (e/h) ?")
    if cvp == "h":
        break
    else:
        continue
print("Hesap makinesi kapandi")