print("hello world")
#this is a string
# IN PYTHON ANYTHING IN A QUOTE IS A STRING
# a variable is a container that hold data 
man = 5
number = 30
print(number)
#dos and dont when naming variable
#1. must start with letter or underscorecharacter
_age = 1
print(_age)
#2. cannot start with a number
#7=49
#3 a variable name can only contain aiphanumeric character and underscore
#4. variable are case sensitive
age = 20 
Age = 30
AGE = 40
print(AGE)
#5. a variable name cannot be any of the python keyword
# string concatination
first_name ="emmanuel"
last_name = "peter"

# string interpolation
# interpolation is a method of embedding expression or variable with srtings.
   





   # common string methhods
   #python has a lot of built-in methods that we can use on strings. and all string method return new values,i.e they dont change the original string.
   #capitalize()- convert the first letter of the string to upper case
club = 'manchester united'
fruit = "banana"
print(club.capitalize())
print("chelsea is the best club".capitalize)
#.title() will capitalize the first letter of each word
print(club.title())
#count()  - count how many times a particular string appear in the whole string or variable 
print(club.count("e"))
print(fruit.count("na"))
#startswith() -
print(fruit.startswith("b"))
#endswith()-
print(fruit.endswith("a"))
print(fruit.endswith("na"))
#Find()
print(fruit.find("a"))
print(fruit.find("f"))
#format()- formats specified values in a string using placeholder
print('{} is {}'.format (club,fruit))
print('{0} {1} {0}'.format ("home","sweet"))
print("the value of pi to 2 d.p is {0:.2f}".format(3.14159))
#index()
print(fruit.index("a"))
#islower()
print(fruit.islower())
print(club.islower())
#isupper
#lower()

#upper()
print(fruit.upper())
#lsri()-remov
print("hello".rstrip("o"))
#rstrip()- remove
# replace -replace all occurrence of a substring with another substracting
print(fruit.replace("na","ma"))
#string.split()method - split a string into a list where every item is a list item
txt ="hello, my name is peter,i am 29 years old"
print(txt.split(","))
print(txt.split(",",1))
#.join()
mytuple =("misheal","samson","Emmanuel")
print(type(mytuple))
y ="".join(mytuple)
print(y)
print(type(y))
#assingnment


first_name = "john"
last_name = "doe"
full_name = first_name + " " + last_name
print(full_name)


name = "Alice"
message = "hello,"
full_message = f"{message} {name}"
print(full_message)




text = "lazy dog"
capitalized_text = text.capitalize()
print(capitalized_text)




book_title = "to kill a mockingbird"
capitalized_title = book_title.title()
print(capitalized_title)




text = "hello world"
count_o = text.count('o')
print(count_o)




filename = "document.txt"
starts_with_doc = filename.startswith("doc")
print(starts_with_doc)



url = "https://www.example.com"
ends_with_com = url.endswith(".com")
print(ends_with_com)



phrase = "find the needle in the haystack"
position = phrase.find("needle")
print(position)

index = "python"
print(index[0])
print(index[5])




#third class
