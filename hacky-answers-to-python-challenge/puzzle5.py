# -*- coding: utf-8 -*-
def soundex(name, len=4):
    """ soundex module conforming to Odell-Russell algorithm """

    # digits holds the soundex values for the alphabet
    soundex_digits = '01230120022455012623010202'
    sndx = ''
    fc = ''

    # Translate letters in name to soundex digits
    for c in name.upper(  ):
        if c.isalpha(  ):
            if not fc: fc = c   # Remember first letter
            d = soundex_digits[ord(c)-ord('A')]
            # Duplicate consecutive soundex digits are skipped
            if not sndx or (d != sndx[-1]):
                sndx += d

    # Replace first digit with first letter
    sndx = fc + sndx[1:]

    # Remove all 0s from the soundex code
    sndx = sndx.replace('0', '')

    # Return soundex code truncated or 0-padded to len characters
    return (sndx + (len * '0'))[:len]
    

S=soundex("peakhell")

# gives the soundex code , then search dictionary ....used  https://www.litscape.com/word_tools/soundex_match.php

from nltk.corpus import words
word_list = words.words()
# prints 236736
print len(word_list)


import nltk
nltk.download('words')

word_list = words.words()


F=[]
for name in word_list:
    d=soundex(str(name))
    if d == S:
        F.append(name)
print F




import urllib2

req = urllib2.Request('http://www.pythonchallenge.com/pc/def/peak.html')
response = urllib2.urlopen(req)
the_page = response.read()
    

for i in F:
    print i
    try:
        base_url="http://www.pythonchallenge.com/pc/def/"
        req=req
        response=urllib2.urlopen(req)
        the_page=response.read()
    except:
        # urllib2.HTTPError = True
        urllib2.URLError = True
        next_url=base_url + i + ".html"
        req=urllib2.Request(next_url)
        print the_page



# then did interrupt kernal and got bannar.p ???????




# 
import pickle
import urllib


# 
#     
# #  then went back and found src = banner.p so did 
# 
# 
# pickle_file=pickle.load(open("/home/milly/Dropbox/EVERYTHING_ELSE/Other_stuff/PYTHON_puzzle/banner.p", "rb"))



with open("/home/milly/Dropbox/EVERYTHING_ELSE/Other_stuff/PYTHON_puzzle/banner.p", "rb") as f:
    dest_object_name = pickle.load(f.readlines())  

#  doesnt work!


# # https://medium.com/better-programming/dont-fear-the-pickle-using-pickle-dump-and-pickle-load-5212f23dbbce
# 
# 
# 
# with pickle.load(urllib.urlopen("http://www.pythonchallenge.com/pc/def/banner.p", "wb")) as f:
#     pickle.dump(pickle_file2, f)
# 
# 
# with open(pickle_file, ‘rb’) as f:
#     dest_object_name = pickle.load(f)
# 
# # link="http://www.pythonchallenge.com/pc/def/pickle.html"
# # q= pickle.load(urllib.urlopen(link))
# 
# 
# 
# 
# import pickle
# 
# filename = 'test'
# outfile = open(filename,'wb')




# view-source:http://www.pythonchallenge.com/pc/def/pickle.htmls
