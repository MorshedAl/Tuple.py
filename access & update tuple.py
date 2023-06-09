
#access tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# last item of tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

# range of indexes 
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])


"""
Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.

But there is a workaround.
You can convert the tuple into a list,
change the list, and convert the list back into a tuple.

"""

# change tuple item:
#tuple>list>change>back tuple again.
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

#practice
Tuple=("a","b","d","e","f")
List=list(Tuple) #convert into list
List[2]="xxxxxx" #change
Tuple2=tuple(List) #again tuple

print(Tuple2) #updated



# add item in tuple
#way-1:Convert into a list

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

#practice
Tuple=('a','b','c',"d",)
List=list(Tuple)
List.append('e')
Tuple=tuple(List)
print(Tuple)


#way-2:Add tuple to a tuple
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)


#practice 
Tuple=('a','b','c',"d",)
Tuple2=('e',)
Tuple=Tuple+Tuple2
print(Tuple)


#Remove item
#Tuples are unchangeable, so cannot remove items from it.but another way.

Tuple=('a','b','c',"d",)
List=list(Tuple)
List.remove('c')
Tuple=tuple(List)
print(Tuple)

#The 'del' keyword can delete the tuple completely:

Tuple=('a','b','c',"d",)
del Tuple
print(Tuple) # get an error



















