# 1. En referencia a las comidas rápidas:
# ● Mostrar las existentes.
# ▪ Agregar una nueva.
# ▪ Modificar los datos existentes.
# ▪ Borrar una seleccionada.

import json 
from colorama import Fore, init
init()

def cargar_datos():
    with open('comidas_rapidas.json',"r") as contenido:
        return json.load(contenido )
        
comidas = cargar_datos()

def agregar_datos():
    with open('comidas_rapidas.json',"w") as contenido:
        return json.dump(comidas, contenido )



def mostrar_comidas():
    print(Fore.BLACK + 'Mostrar comidas rapidas')
    print('Las comidas existentes son:')
    for comida in comidas:
        print(f'Id: {comida["id"]}')
        print(f'Descripción: {comida["descripcion"]}')
        print(f'Ingredientes: {comida["ingredientes"]}')
        print(f'Tiempo de elaboración (en minutos): {comida["tiempo"]}')
        print(f'Precio: {comida["precio"]}')
        print(f'Calorias: {comida["calorias"]}')
        if (comida["vegana"] == True):
            print('Vegana : si')
        elif(comida["vegana"] == False):
            print('Vegana : no')
        print('--------------------------------')
    return menu()

def agregar_comida():
    print(Fore.BLACK + 'Agregar comida rapida')
    Id =  len(comidas)+1
    Descripcion = input('Ingrese el nombre de la comida: ')
    Ingredientes = input('Ingrese los ingredientes de la comida de a uno, al finalizar escribir "listo": ')
    ingre=[]
    while(Ingredientes != "listo"):
        ingre.append(Ingredientes)
        Ingredientes = input('Ingrese los ingredientes de la comida de a uno, al finalizar escribir "listo": ')
    Tiempo = int(input('Ingrese el tiempo de elaboración (en minutos): '))
    Precio = int(input('Ingrese el precio en Pesos Argentinos: $'))
    Calorias = int(input('Ingrese las calorias en gramos: '))
    Vegana = input('Indique si es vegana (si/no): ').lower()
    if (Vegana == "si"):
        Vegana = True
    elif(Vegana == "no"):
        Vegana = False
    comida= { "id": Id, 
            "descripcion": Descripcion,
            "ingredientes": ingre, 
            "tiempo": Tiempo, 
            "precio": Precio,
            "calorias": Calorias,
            "vegana": Vegana
            }
    comidas.append(comida)
    print('Su comida fue agregada')
    agregar_datos() 
    return menu()


def modificar_comida():
    print(Fore.BLACK + 'Las comidas a modificar son:')
    for comida in comidas:
        print(comida['descripcion'],"-", end=" ")
    print(' ')
    seleccionada= input('Ingrese la comida a ser modificada: ').lower().strip()
    for comida in comidas:
        if(comida['descripcion'].lower() == seleccionada):
            comida_nueva = input('Ingrese la nueva comida : ').lower().strip() 
            comida['descripcion'] = comida_nueva
            ingredientes_nuevos = input('Ingrese los ingredientes nuevos de la comida de a uno, al finalizar escribir "listo": ')
            ingre = comida['ingredientes'] =[]
            while(ingredientes_nuevos != "listo"):
                ingre.append(ingredientes_nuevos)
                ingredientes_nuevos = input('Ingrese los ingredientes de la comida de a uno, al finalizar escribir "listo": ')
            tiempo_nuevo = int(input('Ingrese el tiempo de coccion en minutos: ').lower().strip())
            comida['tiempo'] = tiempo_nuevo
            precio_nuevo = int(input('Ingrese el nuevo precio en $: ').lower().strip())
            comida['precio'] = precio_nuevo
            calorias_nuevas = int(input('Ingrese las calorias en gramos: ').lower().strip())
            comida['calorias'] = calorias_nuevas
            vegano_nuevo = input('Es vegano (si/no): ').lower().strip()
            if (vegano_nuevo == "si"):
                comida['vegana'] = True
            else:
                comida['vegana'] = False
            print('Su comida fue modificada')
            agregar_datos()
            return menu()

                
def borrar_comida():
    print(Fore.BLACK + 'Las comidas a eliminar son:')
    for comida in comidas:
        print(comida['descripcion'],"-", end=" ")
    print(' ')
    seleccionada= input('Ingrese la comida a eliminar: ').lower().strip()
    for comida in comidas:
        if(comida['descripcion'].lower() == seleccionada):
            print(comida)
            indice= comidas.index(comida)
            comidas.pop(indice)
    agregar_datos()
    print(f"{comida['descripcion']} fue eliminada/o")
    menu()

# 2. Funciones de búsqueda de comidas rápidas a partir de los siguientes criterios:
# ▪ Buscar por ingrediente.
# ▪ Buscar por precio.
# ▪ Buscar por calorías.
# ▪ Las comidas veganas disponibles.

def buscar_ingrediente():
    print(Fore.BLACK + 'Buscar por precio:')
    seleccionada= input('Ingrese un ingrediente por el cual desea buscar: ').lower().strip()
    for comida in comidas:
        for elemento in comida['ingredientes']:
            if (elemento == seleccionada):
                print(f'Descripción: {comida["descripcion"]}')
                print(f'Ingredientes: {comida["ingredientes"]}')
                print(f'Tiempo de elaboración (en minutos): {comida["tiempo"]}')
                print(f'Precio: {comida["precio"]}')
                print(f'Calorias: {comida["calorias"]}')
                if(comida['vegana'] == True):
                    print(f'Vegana: si')
                else:
                    print(f'Vegana: no')
                print('--------------------------------')
    menu()
            


def buscar_precio():
    print(Fore.BLACK + 'Buscar por precio:')
    seleccionada= int(input('Ingrese el precio por el cual desea buscar: $').lower().strip())
    for comida in comidas:
        if(comida['precio'] == seleccionada):
            print(f'Descripción: {comida["descripcion"]}')
            print(f'Ingredientes: {comida["ingredientes"]}')
            print(f'Tiempo de elaboración (en minutos): {comida["tiempo"]}')
            print(f'Precio: {comida["precio"]}')
            print(f'Calorias: {comida["calorias"]}')
            if(comida['vegana'] == True):
                print(f'Vegana: si')
            else:
                print(f'Vegana: no')
            print('--------------------------------')
    menu()

def buscar_calorias():
    print(Fore.BLACK +'Buscar por calorias:')
    seleccionada= int(input('Ingrese las calorias en gramos por las cuales desea buscar: ').lower().strip())
    for comida in comidas:
        if comida['calorias'] == seleccionada:
            print(f'Descripción: {comida["descripcion"]}')
            print(f'Ingredientes: {comida["ingredientes"]}')
            print(f'Tiempo de elaboración (en minutos): {comida["tiempo"]}')
            print(f'Precio: {comida["precio"]}')
            print(f'Calorias: {comida["calorias"]}')
            if(comida['vegana'] == True):
                print(f'Vegana: si')
            else:
                print(f'Vegana: no')
            print('--------------------------------')
    menu()

def buscar_veganas():
    print(Fore.BLACK + 'Buscar comidas veganas o no veganas:')
    seleccionada= input('La comida es vegana? si/no : ').lower().strip()
    if(seleccionada == 'si'):
        seleccionada = True
    else:
        seleccionada = False
    for comida in comidas:
        if comida['vegana'] == seleccionada:
            print(f'Descripción: {comida["descripcion"]}')
            print(f'Ingredientes: {comida["ingredientes"]}')
            print(f'Tiempo de elaboración (en minutos): {comida["tiempo"]}')
            print(f'Precio: {comida["precio"]}')
            print(f'Calorias: {comida["calorias"]}')
            if(comida['vegana'] == True):
                print(f'Vegana: si')
            else:
                print(f'Vegana: no')
            print('--------------------------------')
    menu()

# 3. Generar un mecanismo para agregar a la información existente los pasos para la elaboración de una o varias comidas del menú.

def agregar_receta():
    print(Fore.BLACK + 'Las comidas para agregar eleboracion son:')
    for comida in comidas:
        print(comida['descripcion'],"-", end=" ")
    print(' ')
    seleccionada= input('Ingrese la comida para agregar eleboracion: ').lower().strip()
    for comida in comidas:
        if(comida['descripcion'].lower() == seleccionada):
            receta_nueva = input('Ingrese los pasos de a uno para la receta, al finalizar escribir "listo": ')
            receta = comida['receta'] =[]
            while(receta_nueva != "listo"):
                receta.append(receta_nueva)
                receta_nueva = input('Ingrese los pasos de a uno para la receta, al finalizar escribir "listo": ')
            print('La receta fue agregada')
            print(f'Descripción: {comida["descripcion"]}')
            print(f'Ingredientes: {comida["ingredientes"]}')
            print(f'Tiempo de elaboración (en minutos): {comida["tiempo"]}')
            print(f'Precio: {comida["precio"]}')
            print(f'Calorias: {comida["calorias"]}')
            if (comida["vegana"] == True):
                print('Vegana = si')
            elif(comida["vegana"] == False):
                print('Vegana = no')
            print(f"Receta= {comida['receta']}")
            agregar_datos()
            return menu()


def menu():
        print('--------------------------------')
        print(Fore.GREEN + 'Elija una opcion')
        print('1) Mostrar comidas rapidas')
        print('2) Agregar comida rapida')
        print('3) Modificar comida rapida')
        print('4) Borrar comida rapida')
        print('5) Buscador de comida')
        print('6) Agregar receta')
        print('0) salir')
        print('--------------------------------')
        opcion = int(input('Opcion elegida: '))
        match opcion:
            case 1:
                mostrar_comidas()
            case 2:
                agregar_comida()
            case 3:
                modificar_comida()
            case 4:
                borrar_comida()
            case 5:
                buscador()
            case 6:
                agregar_receta()
            case 0:
                print('Hasta la proxima')

def buscador():
    print('--------------------------------')
    print(Fore.BLUE + 'Elija una manera de buscar')
    print('1) Buscar por ingrediente.')
    print('2) Buscar por precio.')
    print('3) Buscar por calorías.')
    print('4) Buscar comidas veganas disponibles')
    print('0) Volver al menu principal')
    print('--------------------------------')
    opcion = int(input('Opcion elegida: '))
    match opcion:
        case 1:
            buscar_ingrediente()
        case 2:
            buscar_precio()
        case 3:
            buscar_calorias()
        case 4:
            buscar_veganas()
        case 0:
            menu()
    
menu()