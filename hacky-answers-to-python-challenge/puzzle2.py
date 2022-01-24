txt=open("puzzle_new.txt", "r").read()

new=txt.replace("\n", "")

new2=" ".join(new).split()


a=[]
for i in new2:
    if i not in a:
        a.append(i)
    else:
        pass

http://www.pythonchallenge.com/pc/def/equality.html
http://wiki.pythonchallenge.com/index.php?title=Level2:Main_Page
