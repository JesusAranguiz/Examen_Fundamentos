#Jesus Aranguiz
import csv
import random

trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]   
empleados =[]


def menu():
    while True:
        try:
            print('''--------Menu--------
1) Asignar sueldos aleatorios
2) Clasificar sueldos
3) Ver estadisticas
4) Reporte de sueldos
5) Salir del programa
''')
            op = int(input("Seleccione una opcion: "))
            if op in [1,2,3,4,5]:
                return op
            else:
                print("seleccione una opcion valida.")
        
        except ValueError:
            print("opcion no valida")
            
            
def asignar_sueldos():
    for pepsi in trabajadores:
        pizza = {}
        sueldo = random.randint(300000,2500000)
        pizza = {"Nombre": pepsi,"Sueldo": sueldo,"Desc. Salud": int(sueldo * 0.07),"Desc. AFP": int(sueldo * 0.12),"Sueldo liquido": int(sueldo * 0.81)}
        empleados.append(pizza)
        
def Clasificar_sueldos():
    total=0
    menor=[i for i in empleados if i["Sueldo"]<=800000]
    mitad=[i for i in empleados if i["Sueldo"]>800000 and i["Sueldo"]<=2000000]
    mayor=[i for i in empleados if i["Sueldo"]>2000000]
    print(f"Sueldos menores a $800.000 TOTAL: {len(menor)}")
    print("Nombre\t\tSueldo")
    for pepsi in menor:
        print(f"{pepsi["Nombre"]}\t${pepsi["Sueldo"]:,}")
    print(f"Sueldos entre $800.000 y $2.000.000 Total:{len(mitad)}")
    print("Nombre\t\tSueldo")
    for pepsi in mitad:
        print(f"{pepsi["Nombre"]}\t${pepsi["Sueldo"]:,}")
    print(f"Sueldos superiores a $2.000.000 TOTAL{len(mayor)}")
    print("Nombre\t\tSueldo")
    for pepsi in mayor:
        print(f"{pepsi["Nombre"]}\t${pepsi["Sueldo"]:,}")
    for pepsi in empleados:
        total+=pepsi["Sueldo"]
    print(f"TOTAL SUELDOS: ${total:,}")

def reporte_sueldo():
    with open ("reporte_sueldo.csv", "w", newline="") as archivo:
        reporte = csv.writer(archivo)
        reporte.writerow(['Nombre empleado','Sueldo Base','Descuento Salud','Descuento AFP','Sueldo Liquido'])
        for pepsi in empleados:
            reporte.writerow([pepsi["Nombre"],pepsi["Sueldo"],pepsi["Desc. Salud"],pepsi["Desc. AFP"],pepsi["Sueldo liquido"]])
         
def estadisticas():
    mas_gana=max(empleados,key=lambda x: x["Sueldo"])
    menos_gana=min(empleados,key=lambda x: x["Sueldo"])
    print(f'El que gana mas es {mas_gana["Nombre"]} con un sueldo de ${mas_gana["Sueldo"]:,}')
    print(f'El que gana menos es {menos_gana["Nombre"]} con un sueldo de ${menos_gana["Sueldo"]:,}')
    total2=sum(pepsi['Sueldo'] for pepsi in empleados)
    total2=int(total2/10)
    print(f'El promedio de sueldos es de ${total2:,}')
                      
def menu_principal():
    while True:
        menu_def= menu()
        if menu_def == 1:
            asignar_sueldos()
            print("Sueldos asignados.")
        elif menu_def == 2:
            Clasificar_sueldos()
        elif menu_def == 3:
            estadisticas()
        elif menu_def == 4:
            reporte_sueldo()
        elif menu_def == 5:
            print("Finalizando programa...")
            print("Desarrollador por Jesus Aranguiz.")
            print("RUT 21.038.345-k")
            break
        else:
            print("seleccione una opcion valida.")
        
menu_principal()