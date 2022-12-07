# some_list = [1, 2, 3, 4, 5]


# class MyIter:
#     def __init__(self, value):
#         self.value = value
#         self.temp = None

#     def __next__(self):
#         if self.temp is None:
#             self.temp = 0
#         else:
#             self.temp += 1
#         return self.value[self.temp]

#     def __iter__(self):
#         return self


# some_dic = {}
# some_dic[(1)] = 5
# an = lambda x, y, z, f, g: x + y
# print(an(1, 3, 4, 5, 6))

# it = iter(some_list)
# it_iter = iter(some_list)
# # for item in it_iter:
# #     print(item)
# # print(next(it_iter))
# # print(next(it_iter))
# # print(next(it_iter))
# # print(next(it_iter))
# # print(next(it_iter))
list

# # gen = (i**2 for i in some_list)
# def gen(val):
#     while val > 0:
#         yield val
#         val -= 1
#     return 'Конец цикла'


# g = gen(6)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# # print(next(gen))
# # print(next(gen))
# # print(next(gen))
# # print(next(gen))
# a = [1,2,3]
# print(id(a))
# a+=[4]
# print(id(a))
# tup = (1,2,[30,40])
# hash(tup)
# print(tup)
# dis.dis('s[a]+=[50]')
# # print(tup)
# set_1 = {1,3,4,2,7}
# set_1.add(None)
# print({1,3} in set_1)
# some_dict = {'1': 'setup.py'}
# match some_dict:
#     case {'1':name}:
# #         return name
# d = dict(record='new', cost=234, category='noutbu', name='s')
# match d:
#     case {'category': 'tv', **extra}:
#         print(extra)
#     case {'category': 'noutbuk'}:
#         raise KeyError('...')
#     case _:
#         print('Dict не корректный')

# class MyDict(dict):

#     def __missing__(self, key):
#         if key in self.keys():
#             return 'Есть ключ'
#         return 'Нет такого ключа'


# d = MyDict({2: 'Temp'})
# print(d[2])
