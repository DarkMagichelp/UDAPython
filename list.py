lenguajes = ['python', 'kotlin', 'java', 'javascript']

print(lenguajes)

#los arrays (list) comienzan en la posicion "0"
print(lenguajes[0]) # python

#ordenar los elementos
lenguajes.sort()
print(lenguajes)

#acceder a un elemento dentro de un texto
aprendiendo = f'estoy aprendiendo {lenguajes[3]} '
print(aprendiendo)

#modificando valores de un arreglo (list)
lenguajes[2] = 'PHP'
print(lenguajes)

#AGREGAR ELEMENTOS
lenguajes.append('RUBY')
print(lenguajes)

#ELIMINAR
del lenguajes[1]
print(lenguajes)

#eliminar de un arreglo (list)
lenguajes.pop()
print(lenguajes)

#eliminar con pop una posicion en especifico
lenguajes.pop(0)
print(lenguajes)

#eliminar por nombre
lenguajes.remove('PHP')
print(lenguajes)