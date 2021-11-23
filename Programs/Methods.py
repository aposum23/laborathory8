A = ('sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat')
day = str(input('Enter day: '))
if day in A:
    num = A.index(day)
    print('Number of day = ', num + 1)
else:
    num = -1
    print('Wrong day')
'''
d = 1
'''



A = ('ab', 'ac', 'ab', 'ab', 'ca', 'ad', 'jklmn')
d1 = A.count('ab')
d2 = A.count('jprst')
d3 = A.count('ca')

print('d1 = ', d1)
print('d2 = ', d2)
print('d3 = ', d3)
'''
d1 = 3
d2 = 0
d3 = 1
'''



import sys

if __name__ == '__main__':
    A = tuple(map(int, input().split()))
    if len(A) != 10:
        print('Неверный размер кортежа', file=sys.stderr)
        exit(1)
    s = 0
    for item in A:
        if abs(item) < 5:
            s += item
    print(s)



import sys

if __name__ == '__main__':
    A = list(map(int, input().split()))
    if len(A) != 10:
        print('Неверный размер кортежа', file=sys.stderr)
        exit(1)
    s = sum(a for a in A if abs(a) < 5)
    print(s)