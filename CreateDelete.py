#CREATE TUPLES
a = ()
print(type(a))
#<class 'tuple'>
b = tuple()
print(type(b))
#<class 'tuple'>

a = (1, 2, 3, 4, 5)
print(type(a))
#<class 'tuple'>
print(a)
#(1, 2, 3, 4, 5)

a = tuple([1, 2, 3, 4])
print(a)
#(1, 2, 3, 4)

not_a_tuple = (42)

tuple = (42,)


#GET ELEMENTS
a = (1, 2, 3, 4, 5)
print(a[0])
#1
print(a[1:3])
#(2, 3)
a[1] = 3
#Traceback (most recent call last)...

#DELET TUPLES
a = (1, 2, 3, 4, 5)
del a[0]
#Traceback (most recent call last)...
del a
print(a)
#Traceback (most recent call last)...