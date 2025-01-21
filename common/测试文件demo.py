import copy

a = [1,2,"hello",['python', 'C++']]

b = copy.copy(a)

a.append(4)
print(a)
print(b)