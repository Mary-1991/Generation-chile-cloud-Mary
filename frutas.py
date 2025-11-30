frutas = ["manzana", "banana", "cereza"]

for fruta in frutas:
    print(fruta)


frutas = [
    {"nombre": "manzana", "precio": 0.5, "cantidad": 10},
    {"nombre": "banana", "precio": 0.3, "cantidad": 5},
    {"nombre": "cereza", "precio": 0.2, "cantidad": 20}
]
fruta

total_ventas = 0.0
for fruta in frutas:
    total_ventas += fruta["precio"] * fruta["cantidad"]
    print(fruta["nombre"])

print("Calculando el total de ventas...")
print("Total de ventas: $", total_ventas)


frutas = []
while (True):
    nombre = input("Escribe 'salir' para terminar el bucle: ")
    if nombre.lower() == "salir":
        print("Saliendo del bucle...")
        break
    else:
        print("Has escrito:", nombre)

    precio = float(input("Ingresa el precio de la fruta: "))
    print("Has ingresado:", nombre)
    print("Precio:", precio)


    fruta = {"nombre": nombre, "precio": precio}
    frutas.append(fruta)   

print("Ticket de compra ")
for fruta in frutas:
    print("Producto:", fruta["nombre"], "- Precio:", fruta["precio"]) 
