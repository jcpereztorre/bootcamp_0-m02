from funciones1nivel import sumaTodos

'''doble = lambda x: x*2

triple = lambda x: x*3

print(sumaTodos(3, lambda x: doble))

Esto es lo mismo que los dos prints pero es mas correcto lo otro'''

print(sumaTodos(3, lambda x: x*2))
print(sumaTodos(100, lambda x: x*3))

