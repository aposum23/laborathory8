d = tuple('Hello') # d = ('H', 'e', 'l', 'l', 'o')

lst = [2, 'abc', 3.88]
e = tuple(lst) #e = (2, 'abc' ,3.88)
f = tuple((3, 2, 0, -5)) #f = (3, 2, 0, -5)




A = (0, 1, 2, 3)
item = A[0:2] #item = (0, 1)

A  = (2.5, ['abcd', True, 3.1415], 8, False, 'z')
item = A[1:3] #item = (['abcd', True, 3.1415], 8)

A = (3, 8, -11, 'program')
B = ('Python', A, True)
item = B[:3] #item = ('Python', (3, 8, -11, 'program'), True)
item = B[1:] #item = ((3, 8, -11, 'program'), True)



A = (1, 2, 3)
B = (4, 5, 6)
C = A + B #C = (1, 2, 3, 4, 5, 6)

D = (3, 'abc') + (-7.22, ['a', 5]) #D = (3, 'abc, -7.22, ['a', 5])

A = ('a', 'aa', 'aaa')
B = A +(1, 2) + (True, False) #B = ('a', 'aa', 'aaa', 1, 2, True, False)



A = (1, 2, 3) * 3 #A = (1, 2, 3, 1, 2, 3, 1, 2, 3)

B = ('ab', ['1', '12']) * 2 #A = ('ab', ['1', '12'], 'ab', ['1', '12'])




A = ('abc', 'abcd', 'bcd', 'cde')
for item in A:
    print(item)

A = (-1, 3, -8, 12, -20)
i = 0
k = 0
while i < len(A):
    if(A[i]<0):
        k = k +  1
    i = i + 1
print('k = ', k)

A = ('abc', 'ad', 'bcd')
B = [item * 2 for item in A]
print('A = ', A)
print('B = ', B)
'''
abc
abcd
bcd
cde
k = 3
A = ('abc', 'ad', 'bcd')
B = ['abcabc', 'adad', 'bcdbcd']
'''



A = ('abc', 'abcd', 'bcd', 'cde')
item = str(input('s ='))
if(item in A):
    print(item, ' in ', A, ' = True')
else:
    print(item, ' in ', A, ' = False')
'''
s = abc
abc in ('abc', 'abcd', 'bcd', 'cde') = True
'''
