frutas = ["manzana", "banana", "cereza"]

print("Frutas disponibles:")
for fruta in frutas:
    print(fruta)


alumnos =[]

alumno1 = input("Ingrese el nombre del alumno 1: ")
alumno2 = input("Ingrese el nombre del alumno 2: ")
alumno3 = input("Ingrese el nombre del alumno 3: ")
alumno4 = input("Ingrese el nombre del alumno 4: ")
alumno5 = input("Ingrese el nombre del alumno 5: ")

alumnos.append(alumno1)
alumnos.append(alumno2)
alumnos.append(alumno3)
alumnos.append(alumno4)
alumnos.append(alumno5)

print("Lista de alumnos:" )
print(alumnos)

alumnos.insert( 2, input("Ingrese el nombre del alumno que desea agregar en la posición 3: "))
print(alumnos)

alumnos.pop(2) 

print("Lista de alumnos actualizada:")

print(alumnos)

