#A tuple is a collection which is ordered and unchangeable 
#    and allow duplicate.

#create a tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#tuple allow duplicate
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#len():
thistuple = tuple(("apple", "banana", "cherry"))
print(len(thistuple))

#One item tuple, remember the comma:
thistuple = ("apple",)
print(type(thistuple)) #tuple

#NOT a tuple
thistuple = ("apple")
print(type(thistuple)) #str


#Tuple items can be of any data type:
#String, int and boolean data types:

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

print(tuple1)
print(tuple2)
print(tuple3)

#A tuple can contain different data types:

tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)

#What is the data type of a tuple?
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))



# the tuple() constructor 
#Using the tuple() method to make a tuple:
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)

#practice #practice #practice
#create tuple
# allow duplicate 
#len()
# one item tuple
# data type: int,str,boolean in tuple
# different data_type in one tuple
#tuple() constructor     



Tuple=('A','B','C','D','E','F')
print(Tuple)


Tuple=('A','B','C',"C",'D','E','F','F')
print(Tuple)

Tuple=('A','B','C',"C",'D','E','F','F')
print(len(Tuple))


Tuple=('A',)
print(Tuple) #tuple


Tule=('A')
print(Tuple) #string


Tuple=('A','B','C','D','E','F')
print(Tuple)


Tuple=(100,200,300,500,700)
print(Tuple)

Tuple=(0,1,1,0)
print(Tuple)

Tuple=(True,True,False,)
print(Tuple)

Tuple=('A','BBBB',300, True)
print(Tuple)


Tuple=tuple(('a','d','t',500,True))
print(Tuple)


