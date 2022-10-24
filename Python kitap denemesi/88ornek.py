import re
siir = """ sanma şahım herkesi sen sadıkane yar_olur herkesi
sen dost mu sandın belki ol ağyar_olur sadıkane belki ol alemde
serdar_olur yar olur ağyar olur serdar olur dildar_olur YAVUZ SULTAN SELİM"""

sonOlur = re.findall("\w+olur", siir) 
#sonu "olur" ile biten kelimeleri al
print(sonOlur)