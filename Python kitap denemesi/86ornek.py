# Verilen listeden adı "a" veya "b" ile başlayan ve "e" ile biten isimleri gösteren uygulamayı gerçekleştiriniz.

import re

liste = ["ali","ayşe","bade","sare","can"]
#adi a veya b ile baslayan ve e ile biten isimleri göster.

for isim in liste:
    if re.search("^[ab].*e$", isim):
        print(isim)