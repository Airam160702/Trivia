puntaje=0
print ("Welcome to Taylor Swift trivia! Pondremos a prueba tus conocimientos.")
print ("Tienes", puntaje, " puntos.")
nombre=input("Ingresa tu nombre: ")
print("\n Hola", nombre, "responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n")
#Question 1 
print ("1. ¿Cuándo nació TS?")
print ("a. 13/12/1989")
print ("b. 12/12/1998")
print ("c. 11/12/1989")
print ("d. 14/12/1998")
answ_1 = input("\nTu respuesta: ")
while answ_1 not in ("a", "b", "c", "d"):
  answ_1 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

if answ_1 == "a":
  print ("Muy bien", nombre,"!")
  puntaje+=20
else:
  print("Incorrecto!")

#Question 2
print ("2. ¿Cuál es el último album?")
print ("a. Lover")
print ("b. Folklore")
print ("c. Evermore")
print ("d. Red Taylor's Version")
answ_2 = input("\nTu respuesta: ")
while answ_2 not in ("a", "b", "c", "d"):
  answ_2 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

if answ_2 == "a":
  print("Incorrecto", nombre,". Ese no es el último álbum")
elif answ_2 == "b":
  print("Incorrecto", nombre,". Ese no es el último álbuma")
elif answ_2 == "d":
  print("Incorrecto", nombre,". Ese no es el último álbum")
else:
  print("Muy bien", nombre, "!")
  puntaje+=20


#Question 3
print ("3. ¿Cuándo sale el nuevo album?")
print ("a. 20/09/2022")
print ("b. 21/09/2022")
print ("c. 22/10/2022")
print ("d. 21/10/2022")
answ_3 = input("\nTu respuesta: ")
while answ_3 not in ("a", "b", "c", "d"):
  answ_3 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

if answ_3 == "a":
  print("Incorrecto", nombre,". Taylor no nació ese día")
elif answ_3 == "b":
  print("Incorrecto", nombre,". Taylor no nació ese día")
elif answ_3 == "c":
  print("Incorrecto", nombre,". Taylor no nació ese día")
else:
  print("Muy bien", nombre, "!")
  puntaje+=10

print("Gracias por jugar", nombre,". Tu puntaje es de ",puntaje," .")