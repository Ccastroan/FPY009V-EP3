import os

registro_l =[]
nombre_u= []
fecha=[]
registro_c=[]
sku= []

'''nombre_u = input("Ingrese su nombre de usuario:")'''

def registro():
    try:
        titulo = input("Ingrese el Título del libro: ")
        autor = input("Ingrese el nombre del autor: ")
        año = int(input("Ingrese el Año de Publicación: "))
        sku = input("Ingrese el SKU del libro en formato: ")

        if titulo =="" or autor == "" or año <= 0 :
            print("Fallaron los datos ingresados")

        registro_l = {
            'titulo': titulo,
            'auto': autor,
            'año': año,
            'sku': sku,

        }
        registro_l.append(registro)
        print("registro realizado exitosamente")
    except ValueError:
        print("Dato mal ingresado")




def prestar_l():
    try:
        nombre_u = input("Ingrese Su Nombre:")
        sku = input ("Ingrese el SKU: ")
        fecha = input("Ingrese la fecha en la que estamos en formato(dd-mm-aa):")
        #valores a validar para poder imprimir 
        
    except ValueError:
        print("valor ingresado no se encuentra ")




def listar_l():
    print(" Titulo del Libro \t\t Autor del Libro \t\t Año de Publicación \t\t SKU")
    for registro in registro_l:
        print(f"{registro ['titulo']},{registro ['autor']}. {registro ['año']}, {registro ['sku']}")



def imprimir_r():
    try:
        op= input(f"Hola{nombre_u}, deseas imprimir el reporte de prestamos(Si/No): ")
        if op.lower == "si":
            with open ('plantilla_registro.txt', 'a') as archivo:
                archivo.write("Usuario\t\t Título del Libro \t\t Fecha del Prestamo")
                for registro in registro_l :
                    archivo.write(f"{registro['nombre_u']}\t\t,{registro['titulo']}\t\t,{registro['fecha']} ")
            print("Plantilla generada exitosamente en:",os.getcwd())
        elif op.lower == "no" :
            print("gracias por consultar")
    except ValueError:
        print("Dato mal ingresado, favor ingrese un dato valido")








def menu():
    while True:
        try:
            print("********Menú Ingreso********")
            print(" 1.-Registar libro\n 2.-Prestar Libro\n 3.-listar todos los libros\n 4.-Imprimir reporte de prestamos\n 5.-Salir del programa")
            op = int(input("Ingrese la opción a elegir: "))
        except ValueError:
                print("Valor Nulo")
        if op == 1:
            print("Ejemplo de SKU es las 6 primeras letras del título del libro, las 3 primeras letras del autor , año de publicación.")
            registro_l()
        elif op == 2:
            prestar_l()
        elif op == 3:
            listar_l()
        elif op == 4 :
            imprimir_r()
        elif op == 5:
            print("Programa finalizado\nDesarrollado por Cristián Castro\nRut:20.120.736-3")
            break
    
        else:
            print("La opción entrega esta fuera del rango, por favor intente nuevamente")