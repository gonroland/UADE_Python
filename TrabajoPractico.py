import random

def ingresaValidaRango(li, ls, texto, textoE):
    val = int(input(texto))

    while val < li or val > ls:
        val = int(input(textoE))
    return val

def id_verificacion(existing_ids):
    new_id = random.randint(0, 1000)
    while new_id in existing_ids:
        new_id = random.randint(0, 1000)
    return new_id

def menuVariable():
    marcas = []
    modelos = []
    precios = []
    kilometros = []
    existing_ids = []
    menu = 999
    while menu > 0:
        menu = ingresaValidaRango(-1, 2, "Ingrese un número de acuerdo a la opción deseada: 0. Volver Atrás 1. Autos 2. Informes -1. Terminar programa ", "Error, El número ingresado no corresponde ")
        if menu == 1:
            menu = opcion1(marcas, modelos, precios, kilometros, existing_ids)
        elif menu == 2:
            menu = informe_general(marcas, modelos, precios, kilometros, existing_ids)

    if menu == 0:
        menu = 999

    return menu

def opcion1(marcas, modelos, precios, kilometros, existing_ids):

    menu1 = 999
    while menu1 > 0:
        menu1 = ingresaValidaRango(-1, 3, "Ingrese un número de acuerdo a la opción deseada: 0. Volver Atrás 1. Ford 2. Chevrolet 3. Volkswagen -1. Terminar programa ", "Error, El número ingresado no corresponde ")
        if menu1 == 1:
            menu1 = seleccion1(marcas, modelos, precios, kilometros, existing_ids)
        elif menu1 == 2:
            menu1 = seleccion2(marcas, modelos, precios, kilometros, existing_ids)
        elif menu1 == 3:
            menu1 = seleccion3(marcas, modelos, precios, kilometros, existing_ids)

    if menu1 == 0:
        menu1 = 999

    return menu1

def seleccion1(marcas, modelos, precios, kilometros, existing_ids):
    modeloAutosFord = 999
    while modeloAutosFord > 0:
        modeloAutosFord = ingresaValidaRango(-1, 3, "Ingrese un número de acuerdo a la opción deseada: 0. Volver Atrás 1. Focus 2. Fiesta 3. Mustang ", "Error, El número ingresado no corresponde ")
        if modeloAutosFord == 1:
            modeloAutosFord = focus(marcas, modelos, precios, kilometros, existing_ids)
        elif modeloAutosFord == 2:
            modeloAutosFord = fiesta(marcas, modelos, precios, kilometros, existing_ids)
        elif modeloAutosFord == 3:
            modeloAutosFord = mustang(marcas, modelos, precios, kilometros, existing_ids)

    if modeloAutosFord == 0:
        modeloAutosFord = 999

    return modeloAutosFord

def seleccion2(marcas, modelos, precios, kilometros, existing_ids):
    modeloAutosChevrolet = 999
    while modeloAutosChevrolet > 0:
        modeloAutosChevrolet = ingresaValidaRango(-1, 3, "Ingrese un número de acuerdo a la opción deseada: 0. Volver Atrás 1. Cruze 2. Onix 3. Camaro ", "Error, El número ingresado no corresponde ")
        if modeloAutosChevrolet == 1:
            modeloAutosChevrolet = cruze(marcas, modelos, precios, kilometros, existing_ids)
        elif modeloAutosChevrolet == 2:
            modeloAutosChevrolet = onix(marcas, modelos, precios, kilometros, existing_ids)
        elif modeloAutosChevrolet == 3:
            modeloAutosChevrolet = camaro(marcas, modelos, precios, kilometros, existing_ids)

    if modeloAutosChevrolet == 0:
        modeloAutosChevrolet = 999

    return modeloAutosChevrolet

def seleccion3(marcas, modelos, precios, kilometros, existing_ids):
    modeloAutosVW = 999
    while modeloAutosVW > 0:
        modeloAutosVW = ingresaValidaRango(-1, 3, "Ingrese un número de acuerdo a la opción deseada: 0. Volver Atrás 1. UP! 2. Golf 3. Scirocco ", "Error, El número ingresado no corresponde ")
        if modeloAutosVW == 1:
            modeloAutosVW = up(marcas, modelos, precios, kilometros, existing_ids)
        elif modeloAutosVW == 2:
            modeloAutosVW = golf(marcas, modelos, precios, kilometros, existing_ids)
        elif modeloAutosVW == 3:
            modeloAutosVW = scirocco(marcas, modelos, precios, kilometros, existing_ids)
    
    if modeloAutosVW == 0:
        modeloAutosVW = 999

    return modeloAutosVW

def focus(marcas, modelos, precios, kilometros, existing_ids):
    return modelo_vehiculo("Ford", "Focus", marcas, modelos, precios, kilometros, existing_ids)

def fiesta(marcas, modelos, precios, kilometros, existing_ids):
    return modelo_vehiculo("Ford", "Fiesta", marcas, modelos, precios, kilometros, existing_ids)

def mustang(marcas, modelos, precios, kilometros, existing_ids):
    return modelo_vehiculo("Ford", "Mustang", marcas, modelos, precios, kilometros, existing_ids)

def cruze(marcas, modelos, precios, kilometros, existing_ids):
    return modelo_vehiculo("Chevrolet", "Cruze", marcas, modelos, precios, kilometros, existing_ids)

def onix(marcas, modelos, precios, kilometros, existing_ids):
    return modelo_vehiculo("Chevrolet", "Onix", marcas, modelos, precios, kilometros, existing_ids)

def camaro(marcas, modelos, precios, kilometros, existing_ids):
    return modelo_vehiculo("Chevrolet", "Camaro", marcas, modelos, precios, kilometros, existing_ids)

def up(marcas, modelos, precios, kilometros, existing_ids):
    return modelo_vehiculo("Volkswagen", "Up", marcas, modelos, precios, kilometros, existing_ids)

def golf(marcas, modelos, precios, kilometros, existing_ids):
    return modelo_vehiculo("Volkswagen", "Golf", marcas, modelos, precios, kilometros, existing_ids)

def scirocco(marcas, modelos, precios, kilometros, existing_ids):
    return modelo_vehiculo("Volkswagen", "Scirocco", marcas, modelos, precios, kilometros, existing_ids)

def modelo_vehiculo(marca, modelo, marcas, modelos, precios, kilometros, existing_ids):
    menu = 999
    while menu  > 0:
        menu = ingresaValidaRango(-1, 2,
                                  "Ingrese un número de acuerdo a la opción deseada: 0. Volver Atrás 1. Compras 2. Ventas -1. Terminar programa ",
                                  "Error, El número ingresado no corresponde ")
        if menu == 1:
            menu = compra_vehiculo(marca, modelo, marcas, modelos, precios, kilometros, existing_ids)
        elif menu == 2:
            menu = venta_vehiculo(modelo, marcas, modelos, precios, kilometros, existing_ids)
    
    if menu == 0:
        menu = 999

    return menu

def compra_vehiculo(marca, modelo, marcas, modelos, precios, kilometros, existing_ids):
    new_id = id_verificacion(existing_ids)
    print("Agregar Nuevo Vehículo al Stock:")
    precio = int(input("Ingrese el precio del vehículo: "))
    kilometros_vehiculo = int(input("Ingrese los kilómetros del vehículo: "))

    marcas.append(marca)
    modelos.append(modelo)
    precios.append(precio)
    kilometros.append(kilometros_vehiculo)
    existing_ids.append(new_id)

    print("Vehículo agregado con éxito")

    return 1

def venta_vehiculo(modelo, marcas, modelos, precios, kilometros, existing_ids):
    print("Realizar Venta de Vehículo:")
    print("%-36s %-10s %-10s %-15s %-10s" % ('ID', 'Marca', 'Modelo', 'Precio', 'Kilómetros'))
    vehiculos_disponibles = False
    for i in range(len(modelos)):
        if modelos[i] == modelo:
            vehiculos_disponibles = True
            print("%-36s %-10s %-10s %-15s %-10s" % (existing_ids[i], marcas[i], modelos[i], precios[i], kilometros[i]))

    if not vehiculos_disponibles:
        print("No hay vehículos del modelo disponibles para la venta.")

    vehiculo_id = int(input("Ingrese el ID del vehículo que desea vender: "))
    vehiculo_encontrado = False
    i = 0
    while i < len(modelos):
        if existing_ids[i] == vehiculo_id:
            vehiculo_encontrado = True
            marcas.pop(i)
            modelos.pop(i)
            precios.pop(i)
            kilometros.pop(i)
            existing_ids.pop(i)
            print("Venta realizada con éxito.")
        i += 1

    if not vehiculo_encontrado:
        print("Vehículo no encontrado.")

    return 2

def buscar_vehiculos_por_marca_modelo(marca, modelo, marcas, modelos, precios, kilometros, existing_ids):
    vehiculos_encontrados = False
    for i in range(len(modelos)):
        if marcas[i] == marca and modelos[i] == modelo:
            if not vehiculos_encontrados:
                print("Vehículos encontrados")
                print("%-36s %-10s %-10s %-15s %-10s" % ('ID', 'Marca', 'Modelo', 'Precio', 'Kilómetros'))
            vehiculos_encontrados = True
            print("%-36s %-10s %-10s %-15s %-10s" % (existing_ids[i], marcas[i], modelos[i], precios[i], kilometros[i]))
    
    if not vehiculos_encontrados:
        print("No se encontraron otros modelos")


def informe_general(marcas, modelos, precios, kilometros, existing_ids):
    menu = 999
    while menu  > 0:
        menu = ingresaValidaRango(-1, 2,
                                  "Ingrese un número de acuerdo a la opción deseada: 0. Volver Atrás 1. Informe General de Stock 2. Informes Específicos -1. Terminar programa ",
                                  "Error, El número ingresado no corresponde ")
        if menu == 1:
            menu = informe_stock(marcas, modelos, precios, kilometros, existing_ids)
        elif menu == 2:
            menu = informe_especifico(marcas, modelos, precios, kilometros, existing_ids)
    
    if menu == 0:
        menu = 999

    return menu

def informe_stock(marcas, modelos, precios, kilometros, existing_ids):
    print("Informe General de Stock:")
    print("%-36s %-10s %-10s %-15s %-10s" % ('ID', 'Marca', 'Modelo', 'Precio', 'Kilómetros'))

    for i in range(len(modelos)):
        print("%-36s %-10s %-10s %-15s %-10s" % (existing_ids[i], marcas[i], modelos[i], precios[i], kilometros[i]))

    buscar = ingresaValidaRango(1, 2, "¿Desea buscar por marca/modelo? 1. Sí 2. No ", "Error, El número ingresado no corresponde ")
    if buscar == 1:
        marca = ingresaValidaRango(1, 3, "Ingrese la marca: 1. Ford 2. Chevrolet 3. Volkswagen ", "Error, El número ingresado no corresponde ")
        if marca == 1:
            marca_seleccionada = "Ford"
            for i in range(len(modelos)):
                if marcas[i] == marca_seleccionada:
                    print("%-36s %-10s %-10s %-15s %-10s" % (existing_ids[i], marcas[i], modelos[i], precios[i], kilometros[i]))
            
            modelo_seleccion = ingresaValidaRango(1, 3, "Ingrese el modelo: 1. Focus 2. Fiesta 3. Mustang ", "Error, El número ingresado no corresponde ")
            if modelo_seleccion == 1:
                modelos_seleccionados = "Focus"
                for i in range(len(modelos)):
                    if modelos[i] == modelos_seleccionados:
                        print("%-36s %-10s %-10s %-15s %-10s" % (existing_ids[i], marcas[i], modelos[i], precios[i], kilometros[i]))
            elif modelo_seleccion == 2:
                modelos_seleccionados = "Fiesta"
                for i in range(len(modelos)):
                    if modelos[i] == modelos_seleccionados:
                        print("%-36s %-10s %-10s %-15s %-10s" % (existing_ids[i], marcas[i], modelos[i], precios[i], kilometros[i]))
            elif modelo_seleccion == 3:
                modelos_seleccionados = "Mustang"
                for i in range(len(modelos)):
                    if modelos[i] == modelos_seleccionados:
                        print("%-36s %-10s %-10s %-15s %-10s" % (existing_ids[i], marcas[i], modelos[i], precios[i], kilometros[i]))                                                

        elif marca == 2:
            marca_seleccionada = "Chevrolet"
            for i in range(len(modelos)):
                if marcas[i] == marca_seleccionada:
                    print("%-36s %-10s %-10s %-15s %-10s" % (existing_ids[i], marcas[i], modelos[i], precios[i], kilometros[i]))
            
            modelo_seleccion = ingresaValidaRango(1, 3, "Ingrese el modelo: 1. Cruze 2. Onix 3. Camaro ", "Error, El número ingresado no corresponde ")
            if modelo_seleccion == 1:
                modelos_seleccionados = "Cruze"
                for i in range(len(modelos)):
                    if modelos[i] == modelos_seleccionados:
                        print("%-36s %-10s %-10s %-15s %-10s" % (existing_ids[i], marcas[i], modelos[i], precios[i], kilometros[i]))
            elif modelo_seleccion == 2:
                modelos_seleccionados = "Onix"
                for i in range(len(modelos)):
                    if modelos[i] == modelos_seleccionados:
                        print("%-36s %-10s %-10s %-15s %-10s" % (existing_ids[i], marcas[i], modelos[i], precios[i], kilometros[i]))
            elif modelo_seleccion == 3:
                modelos_seleccionados = "Camaro"
                for i in range(len(modelos)):
                    if modelos[i] == modelos_seleccionados:
                        print("%-36s %-10s %-10s %-15s %-10s" % (existing_ids[i], marcas[i], modelos[i], precios[i], kilometros[i]))  

        elif marca == 3:
            marca_seleccionada = "Volkswagen"
            for i in range(len(modelos)):
                if marcas[i] == marca_seleccionada:
                    print("%-36s %-10s %-10s %-15s %-10s" % (existing_ids[i], marcas[i], modelos[i], precios[i], kilometros[i]))

            modelo_seleccion = ingresaValidaRango(1, 3, "Ingrese el modelo: 1. UP! 2. Golf 3. Scirocco ", "Error, El número ingresado no corresponde ")
            if modelo_seleccion == 1:
                modelos_seleccionados = "Up"
                for i in range(len(modelos)):
                    if modelos[i] == modelos_seleccionados:
                        print("%-36s %-10s %-10s %-15s %-10s" % (existing_ids[i], marcas[i], modelos[i], precios[i], kilometros[i]))
            elif modelo_seleccion == 2:
                modelos_seleccionados = "Golf"
                for i in range(len(modelos)):
                    if modelos[i] == modelos_seleccionados:
                        print("%-36s %-10s %-10s %-15s %-10s" % (existing_ids[i], marcas[i], modelos[i], precios[i], kilometros[i]))
            elif modelo_seleccion == 3:
                modelos_seleccionados = "Scirocco"
                for i in range(len(modelos)):
                    if modelos[i] == modelos_seleccionados:
                        print("%-36s %-10s %-10s %-15s %-10s" % (existing_ids[i], marcas[i], modelos[i], precios[i], kilometros[i]))              

        for modelo in modelos_seleccionados:
            buscar_vehiculos_por_marca_modelo(marca_seleccionada, modelo, marcas, modelos, precios, kilometros, existing_ids)

    return 1



def informe_especifico(marcas, modelos, precios, kilometros, existing_ids):
    menu = 999
    while menu  > 0:
        menu = ingresaValidaRango(-1, 2, "Ingrese un número de acuerdo a la opción deseada: 0. Volver Atrás 1. Informes Kilómetros 2. Informes Precio -1. Terminar programa ", "Error, El número ingresado no corresponde ")
        if menu == 1:
            menu = informe_kms(marcas, modelos, precios, kilometros, existing_ids)
        elif menu == 2:
            menu = informe_precio(marcas, modelos, precios, kilometros, existing_ids)

    if menu == 0:
        menu = 999

    return menu

def informe_kms(marcas, modelos, precios, kilometros, existing_ids):
    menu = 999
    while menu > 0:
        menu = ingresaValidaRango(-1, 2, "Ingrese un número de acuerdo a la opción deseada: 0. Volver Atrás 1. Informes Kilómetros Máximos 2. Informes Kilómetros Mínimos -1. Terminar programa ", "Error, El número ingresado no corresponde ")
        if menu == 1:
            menu = informe_kms_maximo(marcas, modelos, precios, kilometros, existing_ids)
        elif menu == 2:
            menu = informe_kms_minimo(marcas, modelos, precios, kilometros, existing_ids)
    
    if menu == 0:
        menu = 999

    return menu

def informe_kms_minimo(marcas, modelos, precios, kilometros, existing_ids):
    for i in range(len(kilometros)):
        for j in range(i+1, len(kilometros)):
            if kilometros[i] > kilometros[j]:
                marcas[i], marcas[j] = marcas[j], marcas[i]
                modelos[i], modelos[j] = modelos[j], modelos[i]
                kilometros[i], kilometros[j] = kilometros[j], kilometros[i]
                precios[i], precios[i] = precios[j], precios[i]
                existing_ids[i], existing_ids[j] = existing_ids[j], existing_ids[i]


    print("%-36s %-10s %-15s %-10s %-10s" % ('ID','Marca', 'Modelo', 'Precios', 'Kilómetros'))
    for i in range(len(marcas)):
        print("%-36s %-10s %-15s %-10s %-10s" % (existing_ids[i], marcas[i], modelos[i], precios[i], kilometros[i]))

    return 1


def informe_kms_maximo(marcas, modelos, precios, kilometros, existing_ids):
    for i in range(len(kilometros)):
        for j in range(i+1, len(kilometros)):
            if kilometros[i] < kilometros[j]:
                marcas[i], marcas[j] = marcas[j], marcas[i]
                modelos[i], modelos[j] = modelos[j], modelos[i]
                kilometros[i], kilometros[j] = kilometros[j], kilometros[i]
                precios[i], precios[i] = precios[j], precios[i]
                existing_ids[i], existing_ids[j] = existing_ids[j], existing_ids[i]


    print("%-36s %-10s %-15s %-10s %-10s" % ('ID','Marca', 'Modelo', 'Precios', 'Kilómetros'))
    for i in range(len(marcas)):
        print("%-36s %-10s %-15s %-10s %-10s" % (existing_ids[i], marcas[i], modelos[i], precios[i], kilometros[i]))

    return 1


def informe_precio(marcas, modelos, precios, kilometros, existing_ids):
    menu = 999
    while menu  > 0:
        menu = ingresaValidaRango(-1, 2, "Ingrese un número de acuerdo a la opción deseada: 0. Volver Atrás 1. Informes Precio Máximos 2. Informes Precio Mínimos -1. Terminar programa ", "Error, El número ingresado no corresponde ")
        if menu == 1:
            menu = informe_precio_maximo(marcas, modelos, precios, kilometros, existing_ids)
        elif menu == 2:
            menu = informe_precio_minimo(marcas, modelos, precios, kilometros, existing_ids)

    if menu == 0:
        menu = 999

    return menu

def informe_precio_minimo(marcas, modelos, precios, kilometros, existing_ids):
    for i in range(len(precios)):
        for j in range(i+1, len(precios)):
            if precios[i] > precios[j]:
                marcas[i], marcas[j] = marcas[j], marcas[i]
                modelos[i], modelos[j] = modelos[j], modelos[i]
                kilometros[i], kilometros[j] = kilometros[j], kilometros[i]
                precios[i], precios[j] = precios[j], precios[i]
                existing_ids[i], existing_ids[j] = existing_ids[j], existing_ids[i]


    print("%-36s %-10s %-15s %-10s %-10s" % ('ID','Marca', 'Modelo', 'Precios', 'Kilómetros'))
    for i in range(len(marcas)):
        print("%-36s %-10s %-15s %-10s %-10s" % (existing_ids[i], marcas[i], modelos[i], precios[i], kilometros[i]))

    return 1


def informe_precio_maximo(marcas, modelos, precios, kilometros, existing_ids):
    for i in range(len(precios)):
        for j in range(i+1, len(precios)):
            if precios[i] < precios[j]:
                marcas[i], marcas[j] = marcas[j], marcas[i]
                modelos[i], modelos[j] = modelos[j], modelos[i]
                kilometros[i], kilometros[j] = kilometros[j], kilometros[i]
                precios[i], precios[j] = precios[j], precios[i]
                existing_ids[i], existing_ids[j] = existing_ids[j], existing_ids[i]


    print("%-36s %-10s %-15s %-10s %-10s" % ('ID','Marca', 'Modelo', 'Precios', 'Kilómetros'))
    for i in range(len(marcas)):
        print("%-36s %-10s %-15s %-10s %-10s" % (existing_ids[i], marcas[i], modelos[i], precios[i], kilometros[i]))

    return 1



def main():
    menuVariable()

if __name__ == "__main__":
    main()
