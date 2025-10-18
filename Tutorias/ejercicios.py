"""#ejercicio 1 - correo electronico

correo=input() # donde escribis el correo

con1=correo.count("@")>=1
con2=(len(correo[:correo.index("@")])>=3) and (len(correo[correo.index("@"):])>=3)
#len() = contrando cuantos caracteres tiene el texto
con3=correo.count(".")==1
con4=correo.count(" ")==0
con5=(correo[0]!=".") and (correo[-1]!=".")

condiciones=(con1, con2, con3, con4, con5)
print(condiciones.count(True)==5) 
"""

"""#ejercicio 2 - dragon durmiendo

cadena=input()
print(cadena.lower().count("z"))
"""

"""#ejercicio 3 - contraseña OOF

num=int(input())
text1=input()
text2=input()

impre_a = len(text1)//num 
impre_b = len(text2)//num 

print(f"{text1[:impre_a]}{text2[-impre_b:]}")
"""

"""#ejercicio 5 - Reporte de Alvin

nota1=float(input())
nota2=float(input())
nota3=float(input())
nota4=float(input())
nota5=float(input())
nota6=float(input())

listado=[nota1, nota2, nota3, nota4, nota5, nota6]

print(f"Maximo: {max(listado):.2f}")
print(f"Minimo: {min(listado):.2f}")
print(f"Diferencia: {max(listado)-min(listado):.2f}")
print(f"Suma: {(nota1+nota2+nota3+nota4+nota5+nota6):.2f}")
print(f"Promedio: {(nota1+nota2+nota3+nota4+nota5+nota6)/6:.2f}")
"""

"""#ejercicio 6 - El jurado de la copa

pun1=int(input())
pun2=int(input())
pun3=int(input())
pun4=int(input())
pun5=int(input())

per1=float(input())
per2=float(input())
per3=float(input())
per4=float(input())
per5=float(input())

suma= (pun1*per1)+(pun2*per2)+(pun3*per3)+(pun4*per4)+(pun5*per5)

print(f"{suma:.0f}")
"""

"""#ejercicio 7 - Identificador C3

nombre=input()
apellido=input()

nick=f"{nombre.lower()[0:5]}{apellido.lower()[0]}"
print(f"Nick: {nick}")
pin=(len(nombre)*1000+len(apellido))%10000 #recordatorio len(x)=cuenta el numero de indices(caracteres/elementos) de la variable
print(f"Pin: {pin}")
print(f"ID: C3-{nick}-{pin}")
"""

"""#ejercicio 8 - Formato de fechas

fecha=input()

#basandome en la fecha inicial DD/MM/YYYY
#contas el orden de cada uno de 0 en adelante para saber que poner entre los corchetes "[]"
print(f"{fecha[6:]}/{fecha[3:5]}/{fecha[:2]}")
"""

"""#ejercicio 9 - La cena de Alvin

platos=("Hamburguesa", "Pizza", "Tacos", "Pupusas", "Hotdog")
complementos=("Papas fritas", "Alitas de pollo", "Ensalada", "Sopa", "Lasaña")

orden1=int(input())
orden2=int(input())

print(f"El pedido de Alvin es: {platos[orden1-1]} con {complementos[orden2-1]}") 
                                # se resta uno para que el numero ingresado sea igual al de las ordenes
"""

"""#ejercicio 10 - El mayor hater de los bucles

numero=int(input())

print(f"{(numero*(numero+1))/2:.0f}") # operacion que piden
"""