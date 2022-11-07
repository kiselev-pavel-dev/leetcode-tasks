some_list = [1, 2, 3, 4, 5]


class MyIter:
    def __init__(self, value):
        self.value = value
        self.temp = None

    def __next__(self):
        if self.temp is None:
            self.temp = 0
        else:
            self.temp += 1
        return self.value[self.temp]

    def __iter__(self):
        return self


some_dic = {}
some_dic[(1)] = 5
an = lambda x, y, z, f, g: x + y
print(an(1, 3, 4, 5, 6))

it = iter(some_list)
it_iter = iter(some_list)
# for item in it_iter:
#     print(item)
# print(next(it_iter))
# print(next(it_iter))
# print(next(it_iter))
# print(next(it_iter))
# print(next(it_iter))
# list

# gen = (i**2 for i in some_list)
def gen(val):
    while val > 0:
        yield val
        val -= 1
    return 'Конец цикла'


g = gen(6)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
