Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#String methods

#len
a="python"
len(a)
6
b="Python Course"
len(b)
13
c=""
len(c)
0
d=" "
len(d)
1

#count()
a="Twinkle twinkle little star"
count(a)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    count(a)
NameError: name 'count' is not defined. Did you mean: 'round'?
a.count("twinkle")
1
a="twinkle twinkle little star"
a.count("twinkle")
2
a.count("k")
2
a.count("t")
5
a.count(" ")
3
a.count("a")
1
a.count("e")
3
a.count("i")
3

#find a string

a="python"
a[2]
't'
a.find("o")
4
b="hello"
b.find("1")
-1
b.find("l")
2
a[2:4]
'th'
b[2:4]
'll'

#escape sequences

#\n->new line
#\t->tab space
a="name\nmobileno\tmailid"
print(a)
name
mobileno	mailid
b="name:Rakshith\nmobileno:9063506162\tmailid:sajjarakshith123@gmail.com"
print(b)
name:Rakshith
mobileno:9063506162	mailid:sajjarakshith123@gmail.com
print("name:Rakshith\nmobileno:9063506162\tmailid:sajjarakshith123@gmail.com")
name:Rakshith
mobileno:9063506162	mailid:sajjarakshith123@gmail.com
>>> 
>>> #replace
>>> #replace()
>>> 
>>> a="wait until you succeed"
>>> a.replace("wait","work")
'work until you succeed'
>>> b="wait wait unti you succeed"
>>> b.replace("wait","work")
'work work unti you succeed'
>>> b.replace("wait","work",1)
'work wait unti you succeed'
>>> 
>>> #strip()
>>> 
>>> #lstrip(),rstrip()
>>> 
>>> a="               rakshith                     "
>>> a.strip()
'rakshith'
>>> a.lstrip()
'rakshith                     '
>>> a.rstrip()
'               rakshith'
