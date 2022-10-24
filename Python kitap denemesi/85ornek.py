import re
s = "bir ol iri ol diri ol"
ara = re.match("ol", s)
print(ara)

ara2 = re.match("bir ol", s)
print(ara2)

ara3 = re.fullmatch("bir ol", s)
print(ara3)
