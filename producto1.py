ciclo = 1  
clave=0 
dic={} 
while ciclo == 1:  
    print("********** PELUQUERIA PETS **********")  
    opcion=int(input("Seleccione una opción: \n1. Ingresar \n2. imprimir  \n3. Eliminar \n4. Editar \n5. Salir\n")) 
    if opcion == 1: 
        clave=clave+1 
        cliente=[None,None,None,None] 
        cliente[0]=input(("Ingrese el nombre del amo: ")) 
        cliente[1]=input(("Ingrese nombre de la mascota: ")) 
        cliente[2]=input(("Ingrese el tipo de la mascota: ")) 
        cliente[3]=input(("Ingrese la raza de la mascota: ")) 
        dic[clave]=cliente
    elif opcion ==2: 
        for clave in dic:
            print(f"-{clave} :{dic[clave]}")
    elif opcion==3: 
        eliminar=int(input("Ingrese el numero de lista a eliminar")) 
        dic.pop(eliminar) 
    elif opcion==5: 
        print("usted eligió salir") 
        ciclo=2   
        break 

print("Usted ha salido del sistema")  

print("")  