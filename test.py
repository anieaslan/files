# def a():
#     return 10
# print(type(a))

# print(5//2)

# a = 7
# print(a.__str__())

print(set([1,2,1]) == set([1,2]))

a = {1:9, 2:8, 2:7, 4:6, 5:5}
print(a.get(6))

# def f():
#     f()
#     return 42
# f()

class test():
    id = 0
    def __init__(self, id):
        self.id = id
        id = 2
t = test(1)
t.id
