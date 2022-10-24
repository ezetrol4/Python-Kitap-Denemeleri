# Cok hizli bir sekilde ic ice buyuyen Ackermann fonksiyonu python dilin kodlayınız.

def ackermann(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))

# Ana program

import random
m = random.randint(0,3)
n = random.randint(0,5)
print("")