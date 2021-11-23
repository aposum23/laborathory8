lst = [1, 2, 3, 4, 5]
print(type(lst))
#<class 'list'>
print(lst)
#[1, 2, 3, 4, 5]
tpl = tuple(lst)
print(type(tpl))
#<class 'tuple'>
print(tpl)
#(1, 2, 3, 4, 5)

tpl = (2, 4, 6, 8, 10)
print(type(tpl))
#<class 'type'>
print(tpl)
#(2, 4, 6, 8, 10)
lst = list(tpl)
print(type(lst))
#<class 'list'>
print(lst)
#[2, 4, 6, 8, 10]