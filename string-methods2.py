Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#upper
a="codegnan"
a.upper()
'CODEGNAN'
b="HELLO"
b.lower()
'hello'
a="python course"
a.upper("p")
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a.upper("p")
TypeError: str.upper() takes no arguments (1 given)
a.captilize()
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    a.captilize()
AttributeError: 'str' object has no attribute 'captilize'. Did you mean: 'capitalize'?
a.capitalize()
'Python course'
a.title()
'Python Course'
b="i am in class"
b.title()
'I Am In Class'
b.capitalize()
'I am in class'
a
'python course'
a="code"
a.isupper()
False
a.islower()
True
a.isalpha()
True
b="code gnan"
b.isalpha()
False
c="codegnan"
c.isalpha()
True
a.startswith("c")
True
a.endswith("e")
True
a.isdigit()
False
b=2313141
b.isdigit()
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    b.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
c="233253454"
c.isdigit()
True
a="rakshith123"
a.isalnum()
True
b="rakshith@123"
b.isalnum()
False

#split()
a="python java c c++"
a.split()
['python', 'java', 'c', 'c++']
b="i am learning python"
b.split()
['i', 'am', 'learning', 'python']

#join()
a="vja","hyd","vzg"
"".join(a)
'vjahydvzg'
" ".join(a)
'vja hyd vzg'
",".join(a)
'vja,hyd,vzg'

#concatenation

a="python"
b="course"
print(a+b)
pythoncourse
print(a+" "+b)
python course
fname="rakshith"
lname="sajja"
print(fname+lname)
rakshithsajja
print(fname+" "+lname)
rakshith sajja
print(fname.title()+" "+lname.title())
Rakshith Sajja
print((fname+" "+lname).title())
Rakshith Sajja

#formating

a=2
b=7
print(a+b)
9
print("the sum is",a+b)
the sum is 9
print("the sum is,a+b")
the sum is,a+b
a="vijayawada"
print("the city name is",a)
the city name is vijayawada

.format()
SyntaxError: invalid syntax
#.format()

a="motu"
b="patlu"
print("hello {}{}".format(a,b))
hello motupatlu
print("hello {} {}".format(a,b))
hello motu patlu
print("hello {} hello {}".format(a,b))
hello motu hello patlu
print("hello {},hello {}".format(a,b))
hello motu,hello patlu
print("hello {}\nhello {}".format(a,b))
hello motu
hello patlu

#fstring
a="chota"
b="bheem"
print(f"hello {a}{b}")
hello chotabheem
print(f"hello {a} {b}")
hello chota bheem
print(f"hello {a} hello{b}")
hello chota hellobheem
print(f"hello {a} hello {b}")
hello chota hello bheem
print(f"hello {a} \nhello {b}")
hello chota 
hello bheem

a="2"
b="5"
print(a*b)
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    print(a*b)
TypeError: can't multiply sequence by non-int of type 'str'
print("the product is ",(a*b))
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    print("the product is ",(a*b))
TypeError: can't multiply sequence by non-int of type 'str'
int a ="2"
SyntaxError: invalid syntax
a=str"2"
SyntaxError: invalid syntax
a=2
b=3
print(a*b)
6
print("product is",(a*b))
product is 6
print("product {} {} is",(a*b).format(a,b))
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    print("product {} {} is",(a*b).format(a,b))
AttributeError: 'int' object has no attribute 'format'
print("product is",(a*b).format(a,b))
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    print("product is",(a*b).format(a,b))
AttributeError: 'int' object has no attribute 'format'
print("product is {a}{b}",.format(a,b))
SyntaxError: invalid syntax
print("product is {}{}",.format(a*b))
SyntaxError: invalid syntax
print("product is {}".format(a*b))
product is 6
print(f"product is {}")
SyntaxError: incomplete input
print(f"product is {a} {b}",(a*b))
product is 2 3 6
print(f"product is ",(a*b))
product is  6
print(f"product is {a*b}")
product is 6
a=4
b=4
c=a*b
print("the product is {}".format(c))
the product is 16
print(f"the product is {c}")
the product is 16
a=10
b=20
b=a
print(b)
10
a=b
print(a)
10
a=5
b=10
a=b
print(b)
10
pritn(a)
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    pritn(a)
NameError: name 'pritn' is not defined. Did you mean: 'print'?
print(a)
10
b=a
print(a)
10
print(b)
10
a=10
b=20
a,b=b,a
print(a,b)
20 10
a=4
>>> b=10
>>> a=temp
Traceback (most recent call last):
  File "<pyshell#143>", line 1, in <module>
    a=temp
NameError: name 'temp' is not defined
>>> temp=a
>>> b=temp
>>> print(a,b)
4 4
>>> temp=a
>>> a=b
>>> b=temp
>>> print(a,b)
4 4
>>> c=11
>>> b=12
>>> temp=a
>>> a=b
... 
>>> b=temp
>>> print(a,b)
12 4
>>> print(c,b)
11 4
