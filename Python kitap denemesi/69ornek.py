def hanoi(n, A, C, B):
    global s
    if n >0:
        hanoi(n - 1, A, B, C)
        print(s,".adim:",A,"-->",C)
        s = s + 1
        hanoi(n - 1, B, C, A)
        return
# ana program
n = int(input("n degerini.:"))
s = 1
# hanoi(n, "kaynak", "hedef", "yedek")
hanoi(n, "A", "C", "B")
