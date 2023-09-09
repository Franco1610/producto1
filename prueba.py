ciclo = 1
lista = []

while ciclo == 1:
    print("")
    print("********** VETERINARIA PETS **********")
    opcion = int(input("Seleccione una opción: \n1. Ingresar \n2. Imprimir \n3. Eliminar \n4. Editar \n5. Salir"))
    print("")

    if opcion == 1:
        cliente = {"Dueno": "", "Mascota": "", "Animal": "", "Raza": ""}
        cliente["Dueno"] = input("Ingrese el nombre del amo: ").capitalize()
        cliente["Mascota"] = input("Ingrese nombre de la mascota: ").capitalize()
        cliente["Animal"] = input("Ingrese el tipo de la mascota: ").capitalize()
        cliente["Raza"] = input("Ingrese la raza de la mascota: ").capitalize()
        lista.append(cliente)
    elif opcion == 2:  # Imprimir
        for i, elemento in enumerate(lista, start=1):
            print(f"{i}. {elemento}")
    elif opcion == 3:  # Eliminar
        try:
            eliminar = int(input("Ingrese el número de lista a eliminar: "))
            if 1 <= eliminar <= len(lista):
                lista.pop(eliminar - 1)
                print("Cliente eliminado.")
            else:
                print("Número de lista no válido.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
    elif opcion == 4:
        for j, elemento in enumerate(lista, start=1):
            print(f"{j}. {elemento}")
        print('')
        opciondelistacliente = int(input("Ingrese el número de lista a editar: "))
        opcionedi2 = int(input("Seleccione cuál quiere editar: \n1. Amo \n2. Mascota  \n3. Animal\n4. Raza \n5. Salir\n"))
        if opcionedi2 < 1 or opcionedi2 > 5:
            print("Opción no válida")
        else:
            if opcionedi2 == 5:
                print("Usted eligió salir del sistema")
            else:
                nuevodato = input("Ingrese el nuevo dato: ")
                ubicacion = opciondelistacliente - 1
                clienteeditar = lista[ubicacion]
                if opcionedi2 == 1:
                    clienteeditar['Dueno'] = nuevodato
                    print("Dato actualizado!")
                elif opcionedi2 == 2:
                    clienteeditar['Mascota'] = nuevodato
                    print("Dato actualizado!")
                elif opcionedi2 == 3:
                    clienteeditar['Animal'] = nuevodato
                elif opcionedi2 == 4:
                    clienteeditar['Raza'] = nuevodato
                lista[ubicacion] = clienteeditar
                print(clienteeditar)
    elif opcion == 5:  # Salir
        print("Usted eligió salir")
        break

print("Usted ha salido del sistema")