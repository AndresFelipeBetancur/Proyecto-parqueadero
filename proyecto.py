

def mostrar_registros(facturas,mensualidades):
    opc = 0
   
    while opc != 4:
        print("""1. Mostrar todos los automóviles .
2. Mostrar todas las motocicletas.
3. Mostrar todas las bicicletas
4. Regresar al menú principal.""")
        print("")
        opc = int(input("Ingrese una opcion: >"))
        print("")
        print("----------------------------------------------------------------------")
        if opc != 4:
            tipo = 0
            if opc == 1:
                tipo = "a"
                nombre_vehiculo = "Automoviles"

            if opc == 2:
                tipo = "m"
                nombre_vehiculo = "Motocicletas"

            if opc == 3:
                tipo = "b"
                nombre_vehiculo = "Bicicletas"

            if tipo != 0:
                print("Tipo de busqueda:", nombre_vehiculo)
                if tipo == "a":
                    print("FACTURA  PLACA        FECHA       INGRESO    SALIDA    MINUTOS  TOTAL    OBSERVACIÓN")
                else:
                    print("FACTURA  PLACA        FECHA       INGRESO    SALIDA    MINUTOS  TOTAL      ")


                for i in range(0, len(facturas)):
                    if facturas[i][2] == tipo:
                        mensualidad = buscar_mensualidad(facturas[i][1],mensualidades,facturas[i][3])
                        print()

                        for j in range(0, len(facturas[i])):
                            if j != 2:
                                if j != 6:
                                    if facturas[i][5] != 0:
                                        print(facturas[i][j], end="       ")
                                        
                                    else:
                                        salida = " "
                                        if j == 5:
                                            print(salida, end="       ")
                                        elif j ==7:
                                            print(salida, end="       ")
                                        elif j ==8:
                                            print(salida, end="       ")
                                        else:
                                            print(facturas[i][j], end="       ")
                                            

                        if tipo == "a":
                            if mensualidad:
                                print(" ","MENSUALIDAD VIGENTE.")
            else:
                print("Opcion no valida. ")

        print()
        print("----------------------------------------------------------------------")



def buscar_vehiculo(facturas):
    opc = 0
    placa = False

    while opc != 4:
        print("""1. Buscar motos
2. Buscar automóviles
3. Buscar bicicletas
4. Regresar al menú principal""")
        print("")
        opc = int(input("Digite su opcion: >"))
        print("")
        if opc != 4:
            
            if opc == 1:
                placa = input("Ingrese la placa de la moto: (tres letras seguida de dos números, seguida de una letra) >")
                nombre_vehiculo = "Moto"
            if opc == 2:
                placa = input("Ingrese la placa del automovil: (3 letras seguidas de 3 números) >")
                nombre_vehiculo = "Automóvil"
            if opc == 3:
                placa = input("Ingrese el consecutivo de la bicicleta: >")
                nombre_vehiculo = "Bicicleta"
            print("----------------------------------------------------------------------")

            if placa != False:
                encontrada = False
                for i in range(0,len(facturas)):
                    if facturas[i][1] == placa:
                        print("Factura No: ", facturas[i][0])
                        print("Num Placa:: ", facturas[i][1])
                        print("Vehículo tipo: ", nombre_vehiculo)
                        print("Fecha de ingreso: ", facturas[i][3])
                        print("Hora de ingreso: ", facturas[i][4])

                        if facturas[i][5] == 0:
                            print("Hora de salida: ", "")
                            print("Nombre: ", facturas[i][6])
                            print("Numero minutos: ", "")
                            print("Total: ", "")

                        else:
                            print("Hora de salida: ", facturas[i][5])
                            print("Nombre: ", facturas[i][6])
                            print("Numero minutos: ", facturas[i][7])
                            print("Total: ", facturas[i][8])

                        encontrada = True
                        print("----------------------------------------------------------------------")

            if placa != False:
                if encontrada == False:
                    print("Vehículo no encontrado. ")
                    print("----------------------------------------------------------------------")



def buscar_placa(placa, facturas):
    bandera = False
    for i in range(0, len(facturas)):
        if placa == facturas[i][1]:
            if facturas[i][5] == 0:
                bandera = True
    return bandera


def buscar_mensualidad(placa, mensualidades, fecha):
    mensualidad = False
    vigencia = 0
    for i in range(0, len(mensualidades)):
        if placa == mensualidades[i][1]:
            mensualidad = True
            vigencia = mensualidades[i][3]

    if mensualidad == False:
        return False

    dia_vigencia = vigencia // 1000000
    mes_vigencia = (vigencia // 10000) % 100
    año_vigencia = vigencia % 10000

    dia_fecha = fecha // 1000000
    mes_fecha = (fecha // 10000) % 100
    año_fecha = fecha % 10000

    if año_fecha > año_vigencia:
        mensualidad = False
    else:
        if año_fecha == año_vigencia:
            if mes_fecha > mes_vigencia:
                mensualidad = False
            else:
                if mes_fecha == mes_vigencia:
                    if dia_fecha > dia_vigencia:
                        mensualidad = False
    return mensualidad




def validar_placa_auto(placa):
    
    letras_permitidas = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    numeros_permitidos = ["0","1","2","3","4","5","6","7","8","9"]
    
    letras = placa[0:3]
    numeros = placa[3:6]

    contador_letras = 0
    contador_numeros = 0

    for i in range(0, len(letras)):
       for j in range(0, len(letras_permitidas)):
           if letras[i] == letras_permitidas[j]:
               contador_letras = contador_letras +1 
    
    for i in range(0, len(numeros)):
        for j in range(0, len(numeros_permitidos)):
            if numeros[i] == numeros_permitidos[j]:
               contador_numeros = contador_numeros +1 

    if contador_letras == 3:
        if contador_numeros == 3:
            return True
        else:
            return False
    else:
        return False





def validar_placa_moto(placa):
    letras_permitidas = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    numeros_permitidos = ["0","1","2","3","4","5","6","7","8","9"]
    
    letras = placa[0:3]
    numeros = placa[3:6]

    contador_letras = 0
    contador_numeros = 0

    letras = placa[0:3]
    numeros = placa[3:5]
    letra_final = placa[5]
    
    for i in range(0, len(letras)):
       for j in range(0, len(letras_permitidas)):
           if letras[i] == letras_permitidas[j]:
               contador_letras = contador_letras +1 
    
    for i in range(0, len(numeros)):
        for j in range(0, len(numeros_permitidos)):
            if numeros[i] == numeros_permitidos[j]:
               contador_numeros = contador_numeros +1 
    
    for i in range(0,len(letras_permitidas)):
        if letra_final == letras_permitidas[i]:
            letra_final = True
            
    if contador_letras == 3:
        if contador_numeros == 2:
            if letra_final == True:
                return True
            else:
                return False
        else:
            return False
    else:
        return False





def ingresar_vehiculo(consecutivo_cicla, consecutivo_vehiculos, mensualidades, tarifas, consecutivo_facturas, vehiculos,facturas):
    vehiculo = []
    factura = []
    bandera = False

    tipo = input("Digite su tipo de vehículo (a : automóvil, m: moto, b: bicicleta ): >")
    print("")

    if tipo == "a":
        cobro = tarifas[0]
    else:
        if tipo == "m":
            cobro = tarifas[1]
        else:
            if tipo == "b":
                cobro = tarifas[2]
            else:
                bandera = True
                cobro = 0

    placa = str(consecutivo_cicla)

    if tipo == "a":
        placa = input("Digite número de la placa (auto:3 letras seguidas de 3 números): >")
    
    elif tipo == "m":
        placa = input("Digite número de la placa (moto: tres letras seguida de dos números, seguida de una letra): >")
    
    else:
        if tipo != "b":
            print("opcion no valida. ")
            return False
        
    if placa != consecutivo_cicla:
        if len(placa) != 6:
            bandera = True


    
    if tipo == "a":
        validez = validar_placa_auto(placa)
        if validez == False:
            bandera = True
            
    if tipo == "m":
        validez = validar_placa_moto(placa)
        if validez == False:
            bandera = True
    
       
    if bandera == True:
        print("¡Vehiculo no ingresado!")
        print("Verifique el orden de la placa.")
        print("Recuerde tambien que la placa debe estar en mayúsculas. ")
        return False

    esta_registrado = buscar_placa(placa, facturas)

    if esta_registrado:
        print("")
        print("La placa ya está registrada. ")
        print("")
        return False
    else:
        horas = int(input("Hora (el formato de 24 horas: hhmm ): >"))

        hora = horas // 100
        minutos = horas % 100

        if hora > 23:
            bandera = True
        if minutos > 59:
            bandera = True

        fecha = int(input("Fecha (ddmmyyyy): >"))

        dia = fecha // 1000000
        if dia <= 0:
            bandera = True
        if dia > 31:
            bandera = True

        mes = (fecha // 10000) % 100
        if mes <= 0:
            bandera = True
        if mes > 12:
            bandera = True

        

        mensualidad = buscar_mensualidad(placa, mensualidades, fecha)

        if mensualidad:
            cobro = 0

        if bandera == False:
            nombre = input("Nombre del cliente: >")
            print("")

            vehiculo.append(placa)
            vehiculo.append(tipo)
            vehiculo.append(horas)
            vehiculo.append(fecha)
            vehiculo.append(nombre)

            factura.append(consecutivo_facturas)
            factura.append(placa)
            factura.append(tipo)
            factura.append(fecha)
            factura.append(horas)
            factura.append(0)
            factura.append(nombre)
            factura.append(0)
            factura.append(cobro)
            retorno = [vehiculo, factura]
            print("")
            print("¡Vehiculo ingresado con exito! ")
            if tipo == "b":
                print("El consecutivo de la bicicleta es: ", consecutivo_cicla)
            print("----------------------------------------------------------------------")

        else:
            
            print("Ingreso no valido (Revise la fecha). ")
            retorno = False
    print("----------------------------------------------------------------------")
    return retorno


def dias_en_mes(mes, bisiesto):
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


def fecha_vigencia(ingreso, bisiesto):
    dia = ingreso // 1000000
    mes = (ingreso // 10000) % 100
    año = ingreso % 10000

    dia = dia + 30

    cantidad_dias = dias_en_mes(mes, bisiesto)

    while dia > cantidad_dias:
        dia = dia - cantidad_dias
        mes = mes + 1

        if mes > 12:
            mes = 1
            año = año + 1

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

        cantidad_dias = dias_en_mes(mes, bisiesto)

    vigencia = (dia * 1000000) + (mes * 10000) + año
    return vigencia


def registrar_mensualidad(mensualidades, tarifas):
    bandera = False
    while bandera == False:
        bandera = True

        if len(mensualidades) < 1:
            num = 1
        else:
            num = mensualidades[-1][0] + 1

        mensualidad = []
        print("")
        placa = input("Ingrese el número de la placa (auto:3 letras seguidas de 3 números): >")
        if len(placa) != 6:
            bandera = False
            

        validez = validar_placa_auto(placa)
        if validez == False:
            bandera = False
            
        if bandera == True:
            print("")
            ingreso = int(input("Ingrese la fecha de entrada (ddmmyyyy): >"))
            print("")
            dia = ingreso // 1000000
            mes = (ingreso // 10000) % 100
            año = ingreso % 10000

            if mes > 12:
                bandera = False
            if mes <= 0:
                bandera = False

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

            if año <= 0:
                bandera = False

            dias_supuestos = dias_en_mes(mes, bisiesto)
            if dia > dias_supuestos:
                bandera = False
            if dia <= 0:
                bandera = False

            if bandera == True:
                vigencia = fecha_vigencia(ingreso, bisiesto)
                cliente = input("Ingrese el nombre del cliente: >")
                print("")
                total = tarifas[3]

                mensualidad.append(num)
                mensualidad.append(placa)
                mensualidad.append(ingreso)
                mensualidad.append(vigencia)
                mensualidad.append(cliente)
                mensualidad.append(total)

                print("Mensualidad registrada con exito. ")
                print("----------------------------------------------------------------------")
                print("Factura de Mensualidad No: ", num)
                print("Num Placa del Auto:", placa)
                print("Fecha ingreso:", ingreso)
                print("Vigencia hasta:", vigencia)   
                print("Nombre:", cliente)
                print("Total:", total)
                print("----------------------------------------------------------------------")
            else:
                print("Fecha ingresada no valida. ")
        else:
            print("Placa no valida. ")

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
        print("")
        opc = int(input("Ingrese una opcion: >"))
        print("")

        if opc == 1:
            tarifa = int(input("Ingrese la tarifa por minuto para Automoviles. "))
            if tarifa > 0:
                lista[0] = tarifa
            else:
                print("La tarifa debe ser mayor a 0.")

        if opc == 2:
            tarifa = int(input("Ingrese la tarifa por minuto para Motocicletas. "))
            if tarifa > 0:
                lista[1] = tarifa
            else:
                print("La tarifa debe ser mayor a 0.")

        if opc == 3:
            tarifa = int(input("Ingrese la tarifa por minuto para Bicicletas. "))
            if tarifa > 0:
                lista[2] = tarifa
            else:
                print("La tarifa debe ser mayor a 0.")
        if opc == 4:
            tarifa = int(input("Ingrese la tarifa mensual para Automoviles. "))
            if tarifa > 0:
                lista[3] = tarifa
            else:
                print("La tarifa debe ser mayor a 0.")

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
        print("")
        opc = int(input("Ingrese una opcion: >"))
        print("")
        if opc == 1:
            tarifa = int(input("Ingrese la tarifa por minuto para Automoviles. "))
            if tarifa > 0:
                lista[0] = tarifa
            else:
                print("La tarifa debe ser mayor a 0.")

        if opc == 2:
            tarifa = int(input("Ingrese la tarifa por minuto para Motocicletas. "))
            if tarifa > 0:
                lista[1] = tarifa
            else:
                print("La tarifa debe ser mayor a 0.")

        if opc == 3:
            tarifa = int(input("Ingrese la tarifa por minuto para Bicicletas. "))
            if tarifa > 0:
                lista[2] = tarifa
            else:
                print("La tarifa debe ser mayor a 0.")
        if opc == 4:
            tarifa = int(input("Ingrese la tarifa mensual para Automoviles. "))
            if tarifa > 0:
                lista[3] = tarifa
            else:
                print("La tarifa debe ser mayor a 0.")

    return lista


def tarifas(lista):
    opc = 0
    while opc != 4:
        print("----------------------------------------------------------------------")
        print("""1. Ingresar Tarifas
2. Mostrar Tarifas
3. Modificar Tarifas
4. Regresar al Menú principal""")
        print("")
        opc = int(input("Ingrese una opcion: >"))
        print("")
        if opc == 1:
            lista = ingresar_tarifas(lista)
        if opc == 2:
            mostrar_tarifas(lista)
        if opc == 3:
            lista = modificar_tarifas(lista)

    return lista

def mostrar_mensualidades(mensualidades):
    print("----------------------------------------------------------------------")
    print("MENSUALIDADES")
    print("NUM   PLACA        CLIENTE      DESDE       HASTA       TOTAL")

    for i in range(0,len(mensualidades)):

        num = str(mensualidades[i][0])
        placa = str(mensualidades[i][1])
        cliente = str(mensualidades[i][4])
        desde = str(mensualidades[i][2])
        hasta = str(mensualidades[i][3])
        total = str(mensualidades[i][5])

        print(
            num, "   ",
            placa, "      ",
            cliente, "     ",
            desde, "   ",
            hasta, "   ",
            total
        )

    print("----------------------------------------------------------------------")

def salida_vehiculo(facturas, lista_tarifas):
    bandera = False

    while bandera == False:
        bandera = True
        print("1. Salida Moto.")
        print("2. Salida Automóvil.")
        print("3. Salida Bicicleta.")
        print("4. Regresar al menú principal.")
        opc = int(input("Ingrese una opcion: >"))

        if opc == 4:
            return facturas
        if opc == 1:
            tipo = "m"
        else:
            if opc == 2:
                tipo = "a"
            else:
                if opc == 3:
                    tipo = "b"
                else:
                    print("Opción inválida.")
                    bandera = False

        if bandera == True:
            encontrado = False
            pos = -1

            if tipo == "b":
                print("")
                print("Bicicletas registradas:")
                for i in range(0,len(facturas)):
                    if facturas[i][2]=="b":
                        print(facturas[i][1])
                print("")
                consecutivo = input("Ingrese el consecutivo de la bicicleta: >")
                i = 0

                while i < len(facturas):
                    if facturas[i][2] == "b":
                        if str(facturas[i][1]) == str(consecutivo):
                            if facturas[i][5] == 0:
                                encontrado = True
                                pos = i
                                i = len(facturas)
                                i = i + 0
                            else:
                                i = i + 1
                        else:
                            i = i + 1
                    else:
                        i = i + 1
            else:
                print("")
                print("Vehiculos Registrados:")
                for i in range(0,len(facturas)):
                    if facturas[i][2]=="a":
                        print(facturas[i][1])

                    if facturas[i][2]=="m":
                        print(facturas[i][1])
                print("")
                placa = input("Ingrese la placa: >")
                i = 0
                while i < len(facturas):
                    if facturas[i][2] == tipo:
                        if facturas[i][1] == placa:
                            if facturas[i][5] == 0:
                                encontrado = True
                                pos = i
                                i = len(facturas)
                                i = i + 0
                            else:
                                i = i + 1
                        else:
                            i = i + 1
                    else:
                        i = i + 1

            if encontrado == False:
                print("Vehículo no registrado o ya tiene salida.")
                print("----------------------------------------------------------------------")
                bandera = False

        if bandera == True:
            hora_s = int(input("Hora de salida (hhmm): >"))
            hs = hora_s // 100
            ms = hora_s % 100

            if hs > 23:
                print("Hora inválida.")
                print("----------------------------------------------------------------------")
                bandera = False

            if ms > 59:
                print("Hora inválida.")
                print("----------------------------------------------------------------------")
                bandera = False
            if hora_s == facturas[pos][4]:
                print("La Hora de salida no debe ser igual a la Hora de entrada.")
                print("----------------------------------------------------------------------")
                bandera = False

        if bandera == True:
            hora_ing = facturas[pos][4]
            hi = hora_ing // 100
            mi = hora_ing % 100

            minutos_totales = (hs * 60 + ms) - (hi * 60 + mi)

            if minutos_totales < 0:
                print("La hora de salida no puede ser inferior a la de ingreso.")
                print("----------------------------------------------------------------------")
                bandera = False

        if bandera == True:
            facturas[pos][5] = hora_s
            facturas[pos][7] = minutos_totales

            if facturas[pos][2] == "a":
                if facturas[pos][8] == 0:
                    facturas[pos][8] = 0
                else:
                    facturas[pos][8] = minutos_totales * lista_tarifas[0]

            if facturas[pos][2] == "m":
                facturas[pos][8] = minutos_totales * lista_tarifas[1]

            if facturas[pos][2] == "b":
                facturas[pos][8] = minutos_totales * lista_tarifas[2]

            print("Factura No: ", facturas[pos][0])
            print("Num Placa:: ", facturas[pos][1])
            print("Vehículo tipo: ", facturas[pos][2])
            print("Fecha de ingreso: ", facturas[pos][3])
            print("Hora de ingreso: ", facturas[pos][4])
            print("Hora de salida: ", facturas[pos][5])
            print("Nombre: ", facturas[pos][6])
            print("Numero minutos: ", facturas[pos][7])
            print("Total: ", facturas[pos][8])
            print("----------------------------------------------------------------------")
    return facturas
def buscar_factura(facturas):
    num =int(input("Digite el número de la Factura: > "))
    encontrada = False
    i = 0
    while i < len(facturas):
        if facturas[i][0] == num:
            print("Factura No: ", facturas[i][0])
            print("Num Placa:: ", facturas[i][1])
            print("Vehículo tipo: ", facturas[i][2])
            print("Fecha de ingreso: ", facturas[i][3])
            print("Hora de ingreso: ", facturas[i][4])
            if facturas[i][5] == 0:
                print("Hora de salida: ", "")
                print("Nombre: ", facturas[i][6])
                print("Numero minutos: ", "")
                print("Total: ", "")
            else:
                print("Hora de salida: ", facturas[i][5])
                print("Nombre: ", facturas[i][6])
                print("Numero minutos: ", facturas[i][7])
                print("Total: ", facturas[i][8])
            encontrada = True
            i = len(facturas)
            i = i + 0
        else:
            i = i + 1
    if encontrada == False:
        print("Factura no encontrada.")
    print("----------------------------------------------------------------------")

def cuadre_de_caja(facturas, mensualidades):
    total_facturas = 0
    total_mensualidades = 0

    i = 0
    while i < len(facturas):
        if facturas[i][8] > 0:
            total_facturas = total_facturas + facturas[i][8]
        i = i + 1

    j = 0
    while j < len(mensualidades):
        total_mensualidades = total_mensualidades + mensualidades[j][5]
        j = j + 1

    total_general = total_facturas + total_mensualidades

    print("----------------------------------------------------------------------")
    print("Total por facturas:", total_facturas)
    print("Total por mensualidades:", total_mensualidades)
    print("Total general del día:", total_general)
    print("----------------------------------------------------------------------")


def menu():
    opc = 0
    lista_tarifas = [0, 0, 0, 0]
    mensualidades = []
    vehiculos = []
    facturas = []

    consecutivo_ciclas = 111111
    consecutivo_vehiculos = 1
    consecutivo_facturas = 1

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
        print("")
        opc = int(input("Ingrese una opcion: >"))
        print("")

        if opc == 1:
            lista_tarifas = tarifas(lista_tarifas)

        if opc == 2:
            mensualidades.append(registrar_mensualidad(mensualidades, lista_tarifas))

        if opc == 3:
            retorno = ingresar_vehiculo(consecutivo_ciclas, consecutivo_vehiculos, mensualidades, lista_tarifas, consecutivo_facturas, vehiculos,facturas)
            if retorno:
                vehiculos.append(retorno[0])
                facturas.append(retorno[1])
                consecutivo_ciclas = consecutivo_ciclas + 1
                consecutivo_vehiculos = consecutivo_vehiculos + 1
                consecutivo_facturas = consecutivo_facturas + 1

        if opc == 4:
            buscar_vehiculo(facturas)

        if opc == 5:
            mostrar_registros(facturas,mensualidades )

        if opc==6:
            mostrar_mensualidades(mensualidades)

        if opc==7:
            salida_vehiculo(facturas, lista_tarifas)

        if opc==8:
            buscar_factura(facturas)

        if opc==9:
            cuadre_de_caja(facturas, mensualidades)
    print("----------------------------------------------------------------------")
    print("Saliendo del sistema...")
    print("----------------------------------------------------------------------")

menu()
