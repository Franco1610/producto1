ciclo = 1  
lista=[]
while ciclo == 1:  
    print("") 
    print("********** VETERINARIA PETS **********")  
    opcion=int(input("Seleccione una opción: \n1. Ingresar \n2. imprimir  \n3. Eliminar \n4. Editar \n5. Salir\n")) 
    if opcion == 1:  
        cliente={"Dueno":"","Mascota":"","Animal":"","Raza":""}
        cliente["Dueno"]= input(("Ingrese el nombre del amo: ")).capitalize() 
        cliente["Mascota"]=input(("Ingrese nombre de la mascota: ")).capitalize()
        cliente["Animal"]=input(("Ingrese el tipo de la mascota: ")).capitalize() 
        cliente["Raza"]=input(("Ingrese la raza de la mascota: ")).capitalize()
        lista.append(cliente)
    elif opcion ==2: 
        for i, lista in enumerate(lista, start=1):
            print(f"{i}. {lista}")
    elif opcion==3: 
        eliminar=int(input("Ingrese el numero de lista a eliminar")) 
        lista.pop(eliminar) 
        print("Cliente eliminado. ")     
    elif opcion==5: 
        print("usted eligió salir") 
        ciclo=2   
        break 

print("Usted ha salido del sistema")  

print("")