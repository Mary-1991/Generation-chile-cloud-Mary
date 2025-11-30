nombre = input("Introduce tu nombre: ")
lugar = input("Introduce un lugar: ")
apellido = input("Introduce tu apellido: ")
nombre_completo = nombre + " " + apellido

mensaje = "Hola " + nombre_completo + ", bienvenido a " + lugar + "."

print(mensaje)

print(f"Hola {nombre_completo}, bienvenido a {lugar}.")

print(type(mensaje))
print(nombre.upper())
print(nombre.lower())


