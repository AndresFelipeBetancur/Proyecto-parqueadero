
def ingresar_vehiculo(consecutivo):
    vehiculo = []

    bandera = False
    tipo = input("Digite su tipo de vehículo (a : automóvil, m: moto, b: bicicleta ): >")
    if tipo != a:
        if tipo != m:
            if tipo != b:
                bandera = True

    placa = consecutivo

    if tipo == a:
        placa = input("Digite número de la placa (auto:3 letras seguidas de 3 números, moto: tres letras: >")

    elif tipo == m:
        placa = input("Digite número de la placa (auto:3 letras seguidas de 3 números, moto: tres letras seguida de dos números, seguida de una letra): >")

    hora = int(input("Hora (el formato de 24 horas: hhmm ): >"))
    fecha = int(input("Fecha (ddmmyyyy): >"))
    nombre = input("Nombre del cliente: >")



def dias_en_mes(mes,bisiesto):
    if mes == 2:
        if bisiesto == True:
            dias = 29
        else:
            dias = 28

    else:
        if mes == 4:
            dias = 30
        elif mes == 6:
            dias = 30
        elif mes == 9:
            dias = 30
        elif mes == 11:
            dias = 30
        else:
            dias = 31

    return dias

def fecha_vigencia(ingreso):
    bandera = False

    dia = ingreso // 1000000
    if dia > 31:
        bandera = True

    mes = (ingreso // 10000) % 100
    if mes > 12:
        bandera = True

    año = ingreso % 10000

    if bandera == False:
        if año % 4 == 0:
            if año % 100 != 0:
                bisiesto = True
            else:
                if año % 400 == 0:
                    bisiesto = True
                else:
                    bisiesto = False
        else:
            bisiesto = False

        cantidad_dias = dias_en_mes(mes,bisiesto)

        dia = dia + 30

        if dia <= cantidad_dias:
            vigencia = (dia * 1000000) + (mes * 10000) + año
        else:
            dia = dia - cantidad_dias
            mes = mes + 1
            if mes > 12:
                año = año + 1
                mes = 1
            vigencia = (dia * 1000000) + (mes * 10000) + año

        return vigencia

    else:
        print("Fecha ingresada incorrecta")


def registrar_mensualidad(mensualidades, tarifas):
    if len(mensualidades) < 1:
        num = 1
    else:
        num = mensualidades[-1][0] + 1

    mensualidad = []

    placa = input("Ingrese el número de la placa (auto:3 letras seguidas de 3 números): >")

    ingreso = int(input("Ingrese la fecha de entrada (ddmmyyyy): >"))

    vigencia = fecha_vigencia(ingreso)
    cliente = input("Ingrese el nombre del cliente: >")

    total = tarifas[3]

    mensualidad.append(num)
    mensualidad.append(placa)
    mensualidad.append(ingreso)
    mensualidad.append(vigencia)
    mensualidad.append(cliente)
    mensualidad.append(total)

    return mensualidad



def modificar_tarifas(lista):
    opc = 0
    while opc != 5:
        print("----------------------------------------------------------------------")
        print("""1. Modificar Tarifa Automóvil
2. Modificar Tarifa Motocicleta
3. Modificar Tarifa Bicicleta
4. Modificar Mensualidad para Autos
5. Regresar al sub Menú Tarifas""")
        opc = int(input("Ingrese una opcion: >"))

        if opc == 1:
            tarifa = int(input("Ingrese la tarifa por minuto para Automoviles. >"))
            print("----------------------------------------------------------------------")
            lista[0] = tarifa
        if opc == 2:
            tarifa = int(input("Ingrese la tarifa por minuto para Motocicletas. >"))
            print("----------------------------------------------------------------------")
            lista[1] = tarifa
        if opc == 3:
            tarifa = int(input("Ingrese la tarifa por minuto para Bicicletas. >"))
            print("----------------------------------------------------------------------")
            lista[2] = tarifa
        if opc == 4:
            tarifa = int(input("Ingrese la tarifa mensual para Automoviles. >"))
            print("----------------------------------------------------------------------")
            lista[3] = tarifa

    return lista

def mostrar_tarifas(lista):
    print("----------------------------------------------------------------------")
    print("1. Tarifa de Automóvil", lista[0])
    print("2. Tarifa de Motocicleta", lista[1])
    print("3. Tarifa de Bicicleta", lista[2])
    print("4. Tarifa de Mensualidad para Autos", lista[3])



def ingresar_tarifas(lista):
    opc = 0
    while opc != 5:
        print("----------------------------------------------------------------------")
        print("""1. Ingresar Tarifa de Automóvil
2. Ingresar Tarifa de Motocicleta
3. Ingresar Tarifa de Bicicleta
4. Ingresar Tarifa de Mensualidad para Autos
5. Regresar al sub Menú Tarifas""")
        opc = int(input("Ingrese una opcion: >"))
        if opc == 1:
            tarifa = int(input("Ingrese la tarifa por minuto para Automoviles. "))
            print("----------------------------------------------------------------------")
            lista[0] = tarifa

        if opc == 2:
            tarifa = int(input("Ingrese la tarifa por minuto para Motocicletas. "))
            print("----------------------------------------------------------------------")
            lista[1] = tarifa

        if opc == 3:
            tarifa = int(input("Ingrese la tarifa por minuto para Bicicletas. "))
            print("----------------------------------------------------------------------")
            lista[2] = tarifa

        if opc == 4:
            tarifa = int(input("Ingrese la tarifa mensual para Automoviles. "))
            print("----------------------------------------------------------------------")
            lista[3] = tarifa

    return lista


def tarifas(lista):
    opc = 0
    while opc != 4:
        print("----------------------------------------------------------------------")
        print("""1. Ingresar Tarifas
2. Mostrar Tarifas
3. Modificar Tarifas
4. Regresar al Menú principal""")
        opc = int(input("Ingrese una opcion: >"))
        if opc == 1:
            lista = ingresar_tarifas(lista)
        if opc == 2:
            mostrar_tarifas(lista)
        if opc == 3:
            lista = modificar_tarifas(lista)

    return lista

def menu():
    opc = 0
    lista_tarifas = [0,0,0,0]
    mensualidades = []
    vehiculos = []
    consecutivo_ciclas = 1
    while opc != 10:
        print("""Menú Principal
1. Tarifas
2. Registrar mensualidad
3. Ingresar vehículo
4. Buscar vehículo
5. Mostrar Registros
6. Mostrar Mensualidades
7. Salida vehículo
8. Buscar Factura
9. Cuadre de Caja
10. Salir""")
        opc = int(input("Ingrese una opcion: >"))
        if opc == 1:
            print("----------------------------------------------------------------------")
            lista_tarifas = tarifas(lista_tarifas)
        if opc == 2:
            print("----------------------------------------------------------------------")
            mensualidades.append(registrar_mensualidad(mensualidades,lista_tarifas))
        if opc == 3:
            vehiculos.append(ingresar_vehiculo(consecutivo))
            consecutivo = consecutivo + 1


menu()
