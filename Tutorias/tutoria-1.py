

lista = ["hola", 32, "a", 3.1416]
        # 0, 1, 2, 3, ... (depende de cuantos objetos se agrege en una lista)
lista2= [12, 1, 20, 34]
        # 0, 1, 2, 3, 
texto= "hola mundo"

print(lista.index(3.1416)) # buscar dentro de la lista el numero de indice del elemento

print(len(lista)) # contar elementos de una cadena de texto, lista o tupla

print(lista[lista2.index(max(lista2))]) # mandar a llamar de una lista el indice del dígito más alto en otra lista
print(lista[lista2.index(min(lista2))]) # Mandar a llamar de una lista el indice del dígito más bajo en otra lista

print(7//2) # division de piso, busca el multiplo más cercano del divisor es decir el multiplo de 2 más cercano a 7

print(texto.count("o")) # de la variable texto, cuenta cuantas o hay
#     Variable.count(elemento que se quiere contar) como trabaja la funcion

print(f"hol{lista[2]}") # f-string sirve para hacer operaciones dentro del texto 
print(f"{lista[3]:.2f}") # la funcion para colocar los decimales debe ir dentro de las llaves "{}"

