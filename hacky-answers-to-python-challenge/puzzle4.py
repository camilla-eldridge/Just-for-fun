import urllib2

#base_url="http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
#number=the_page.split("nothing is ")[1]
#req = urllib2.Request('ftp://example.com/')

## replace url number with new number  ( do it 400 times) 


#req = urllib2.Request('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345')

req = urllib2.Request('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345')
#req=urllib2.Request('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=63579')
response = urllib2.urlopen(req)
the_page = response.read()

# base_url="http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
# number=the_page.split("nothing is ")[1]
# req=urllib2.Request(base_url + str(number))
# response = urllib2.urlopen(req)
# the_page = response.read()


for i in range(400):
    base_url="http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
    req=req
    response=urllib2.urlopen(req)
    the_page=response.read()
    print the_page
    if "Divide" not in the_page:
        number=the_page.split("nothing is ")[1]
        next_url=base_url + str(number)
        req=urllib2.Request(next_url)
    else:
    #print the_page
        number=int(str(number))/2
        next_url=base_url + str(number)
        req=urllib2.Request(next_url)
#There maybe misleading numbers in the text. One example is 82683. Look only for the next nothing and the next nothing is 63579  #    


