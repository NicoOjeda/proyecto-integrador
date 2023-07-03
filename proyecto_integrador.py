# 1. En referencia a las comidas rápidas:
# ● Mostrar las existentes.
# ▪ Agregar una nueva.
# ▪ Modificar los datos existentes.
# ▪ Borrar una seleccionada.
# 2. Funciones de búsqueda de comidas rápidas a partir de los siguientes criterios:
# ▪ Buscar por ingrediente.
# ▪ Buscar por precio.
# ▪ Buscar por calorías.
# ▪ Las comidas veganas disponibles.
import json 

def cargar_datos():
    with open('comidas_rapidas.json',"r") as contenido:
        return json.load(contenido )
        
comidas = cargar_datos()

def agregar_datos():
    with open('comidas_rapidas.json',"w") as contenido:
        return json.dump(comidas, contenido )



def mostrar_comidas():
    print('Mostrar comidas rapidas')
    print('Las comidas existentes son:')
    for i in comidas:
        print(i['descripcion'] )
    return menu()

def agregar_comida():
    print('Agregar comida rapida')
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
    return agregar_datos()


def modificar_comida():
    print('Las comidas a modificar son:')
    for comida in comidas:
        print(comida['descripcion'],"-", end=" ")
    print(' ')
    seleccionada= input('Ingrese la comida a ser modificada: ').lower().strip()
    for comida in comidas:
        if(comida['descripcion'] == seleccionada):
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
    print('Las comidas a eliminar son:')
    for comida in comidas:
        print(comida['descripcion'],"-", end=" ")
    print(' ')
    seleccionada= input('Ingrese la comida a eliminar: ').lower().strip()
    for comida in comidas:
        if(comida['descripcion'] == seleccionada):
            print(comida)
            print(comidas.index(comida))
            indice= comidas.index(comida)
            comidas.pop(indice)
    agregar_datos()
    print(comida, 'Su comida fue eliminada')
    menu()
            
            
    
    
def menu():
        print('--------------------------------')
        print('Elija una opcion')
        print('1) Mostrar comidas rapidas')
        print('2) Agregar comida rapida')
        print('3) Modificar comida rapida')
        print('4) Borrar comida rapida')
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
menu()