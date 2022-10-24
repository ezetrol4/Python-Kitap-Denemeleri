import re
tekerleme = """ kartal kalkar, dal sarkar, dal sarkar, kartal kalkar. """
degistir = re.sub("sarkar", "kalkar", tekerleme)
print(degistir)