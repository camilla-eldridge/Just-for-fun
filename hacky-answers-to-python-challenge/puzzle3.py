text=open("python-test-3", "r").read()
A=text.replace("\n", "")

import re
#search=re.compile('[A-Z]+')

#print search.findall(Z)

# One small letter, surrounded by EXACTLY three big bodyguards on each of its sides.  #

# Look for lower and three upper each side... how!? 

# use re #


#alphabet=list(map(chr, range(97, 123)))
# 
# #Z="aBcdefg36485C62dhdh"
# for i in alphabet:
#     for j in A:#Z:
#         if i.upper() == j:
#             #Z=Z.replace(i.upper(), ".")
#             A=A.replace(i.upper(), ".")
#         else:
#             pass

#print A#Z


def replace_multiple(replace_in):
    replace_in=replace_in
    alphabet=list(map(chr, range(97, 123)))
    for i in alphabet:
        for j in replace_in:
            if i.upper() == j:
                replace_in=replace_in.replace(i.upper(), ".")
            else:
                pass
    return replace_in

            
f=replace_multiple(A)
#print f


#searchi=re.compile(r'\...[a-z]\...')
searchi=re.compile(r'[a-z]\.{3}[a-z]{1}\.{3}[a-z]')

test="agtvsHTS...a...hsycsb..h...gstshs...g...hjtfyw....q..."


s=searchi.search(test)
#print s.group()

aa=searchi.findall(f)
print aa
#search=re.compile('[A-Z]+')

#http://www.pythonchallenge.com/pc/def/linkedlist.php


