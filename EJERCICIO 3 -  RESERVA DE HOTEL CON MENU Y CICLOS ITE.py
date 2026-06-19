import os
import time

#-------------------------BIENVENIDA-------------------------|

print("\t\t        ===========================================")
print("\t\t        |-------> D U B L I N - H O T E L  <------|")
print("\t\t        -------------------------------------------")
print("\t\t        |---> * * * * * R E S O R T * * * * * <---|")
print("\t\t        ===========================================")

#--------------------VALORES CONSTANTES----------------------|

h_simples = 45000
h_dobles = 70000
h_suites = 120000 

#------------INICIALIZACION DE CONTADORES OCUPADAS-----------|

simple_ocupadas = 0
doble_ocupadas = 0
suite_ocupadas = 0

cat_noches = 0

#-------------------CANTIDAD DE HABITACIONES------------------|

simple = 5
doble = 3
suite = 2

#-----------------------------------------------------------------------|

while True:
#--------------CALCULO DE HABITACION DISPONIBLES------------------------|

    simple_disponible = simple - simple_ocupadas
    doble_disponible = doble - doble_ocupadas
    suite_disponible = suite - suite_ocupadas
    total_ocupadas = simple_ocupadas + doble_ocupadas + suite_ocupadas

#-------------------ESTRUCTURA DE MENU 1---------------------------------|

    print("\t---------------------------------------------------------------------------")
    print("\t|> MENU DE HABITACIONES - NO OLVIDE DIGITAR LA OPCION QUE DESEA RESERVAR <|")
    print("\t---------------------------------------------------------------------------")


    print("\t---------------------------------------------------------------------------")
    print("\t| OPCIONES      TIPO DE HABITACION       DISPONIBLES           VALOR $    |")
    print("\t---------------------------------------------------------------------------")
    print(f"\t|    1.-             SIMPLE                  '{simple}'              $45.000     |")
    print("\t---------------------------------------------------------------------------")
    print(f"\t|    2.-             DOBLE                   '{doble}'              $70.000     |")
    print("\t---------------------------------------------------------------------------")
    print(f"\t|    3.-             SUITE                   '{suite}'              $120.000    |")
    print("\t---------------------------------------------------------------------------")
    print("")
    try:
        tipo_habitacion = input("Ingrese tipo de habitacion para reservar: ")

        if tipo_habitacion == "":
            raise ValueError("ERROR")
        
    except Exception as e:
        print("\nDebe ingresar Tipo de habitacion para continuar.")
    try:
        tipo_habitacion = int(tipo_habitacion)
        if tipo_habitacion == 1:

            simple_ocupadas += 1
            disponible = simple_disponible
            precio = h_simples
            nombre_habitacion = "SIMPLE"
            cantidad_reserva = tipo_habitacion

            os.system("cls")
            print("\t---------------------------------------------------------------------------")
            print("\t| OPCIONES      TIPO DE HABITACION       DISPONIBLES           VALOR $    |")
            print("\t---------------------------------------------------------------------------")
            print(f"\t|    1.-             {nombre_habitacion}                 '{disponible}'               ${precio:,.0f}     |")
            print("\t---------------------------------------------------------------------------")
            print("")
            print("\t    ------------------------------------------------------")
            print("\t    |   INSTALACIONES      |          SERVICIOS          |")
            print("\t    |----------------------|-----------------------------|")
            print("\t    | > Piscina            |                      Wifi < |")
            print("\t    | > Estacionamiento    |                  TV Cable < |")
            print("\t    | > Bar                |        Aire acondicionado < |")
            print("\t    | > Restaurant         | Servicio de atencion 24/7 < |")
            print("\t    |----------------------------------------------------|")
            print("")
            try:
                cat_noches = int(input("Ingrese cantidad de noche a reservar: "))

                if cat_noches <= 0:
                    raise ValueError("Debe ingresar una cantidad mayor a cero.")
                
                print("")

                print("Para completar su reserva debe ingresar los siguientes datos: ")
                
                nombre = input("\nNombre completo: ").lower()
                if nombre == "":
                    raise ValueError("Debe ingresar su nombre para continuar")
                
                rut = input("\nRut: ")
                if rut == "": 
                    raise ValueError("Debe ingresar su Rut para continuar")

            except Exception as e:    
                print(f"ERROR: {e}") 

        elif tipo_habitacion == 2:

            doble_ocupadas += 1
            disponible = doble_disponible
            precio = h_dobles
            nombre_habitacion = "DOBLE"
            cantidad_reserva = tipo_habitacion

            os.system("cls")
            print("\t---------------------------------------------------------------------------")
            print("\t| OPCIONES      TIPO DE HABITACION       DISPONIBLES           VALOR $    |")
            print("\t---------------------------------------------------------------------------")
            print(f"\t|    2.-             {nombre_habitacion}                 '{disponible}'               ${precio:,.0f}     |")
            print("\t---------------------------------------------------------------------------")
            print("")
            print("\t    ------------------------------------------------------")
            print("\t    |   INSTALACIONES      |          SERVICIOS          |")
            print("\t    |----------------------|-----------------------------|")
            print("\t    | > Piscina            |                      Wifi < |")
            print("\t    | > Estacionamiento    |                  TV Cable < |")
            print("\t    | > Bar                |        Aire acondicionado < |")
            print("\t    | > Restaurant         | Servicio de atencion 24/7 < |")
            print("\t    |----------------------------------------------------|")
            print("")
            try:
                cat_noches = int(input("Ingrese cantidad de noche a reservar: "))

                if cat_noches <= 0:
                    raise ValueError("Debe ingresar una cantidad mayor a cero.")
                print("")

                print("Para completar su reserva debe ingresar los siguientes datos: ")
                
                nombre = input("\nNombre completo: ").lower()
                if nombre == "":
                    raise ValueError("Debe ingresar su nombre para continuar")
                
                rut = input("\nRut: ")
                if rut == "": 
                    raise ValueError("Debe ingresar su Rut para continuar")

            except Exception as e:    
                print(f"ERROR: {e}")

        elif tipo_habitacion == 3:

            suite_ocupadas += 1
            disponible = suite_disponible
            precio = h_suites
            nombre_habitacion = "SUITE"
            cantidad_reserva = tipo_habitacion

            os.system("cls")
            print("\t---------------------------------------------------------------------------")
            print("\t| OPCIONES      TIPO DE HABITACION       DISPONIBLES           VALOR $    |")
            print("\t---------------------------------------------------------------------------")
            print(f"\t|    3.-             {nombre_habitacion}                 '{disponible}'               ${precio:,.0f}     |")
            print("\t---------------------------------------------------------------------------")
            print("")
            print("\t    ------------------------------------------------------")
            print("\t    |   INSTALACIONES      |          SERVICIOS          |")
            print("\t    |----------------------|-----------------------------|")
            print("\t    | > Piscina            |                      Wifi < |")
            print("\t    | > Estacionamiento    |                  TV Cable < |")
            print("\t    | > Bar                |        Aire acondicionado < |")
            print("\t    | > Restaurant         | Servicio de atencion 24/7 < |")
            print("\t    | > TRANSPORTE         |         Desayuno + Buffet < |")
            print("\t    |----------------------------------------------------|")
            print("")
            try:
                cat_noches = int(input("Ingrese cantidad de noche a reservar: "))

                if cat_noches <= 0:
                    raise ValueError("Debe ingresar una cantidad mayor a cero.")
                print("")

                print("Para completar su reserva debe ingresar los siguientes datos: ")
                
                nombre = input("\nNombre completo: ").lower()
                if nombre == "":
                    raise ValueError("Debe ingresar su nombre para continuar")
                
                rut = input("\nRut: ")
                if rut == "": 
                    raise ValueError("Debe ingresar su Rut para continuar")

            except Exception as e:    
                print(f"ERROR: {e}") 
        else:
            print("La opcion ingresada no es valida debe ser [1 - 2 - 3]")

        subtotal = cat_noches * precio

        total_ocupadas = simple_ocupadas + doble_ocupadas + suite_ocupadas
        
        os.system("cls")
        print("Estamos Procesando su reserva. Por favor espere..!!")
        print("")
        print("loading.......")
        time.sleep(4)
        os.system("cls")

        print("==============================================================")
        print("|      ==========> RESUMEN DE RESERVA <==========            |")
        print("==============================================================")
        print(f"| > NOMBRE:                             {nombre.title()}")
        print(f"| > RUT:                                {rut}")
        print(f"| > TIPO DE HABITACION:                 {nombre_habitacion}")
        print(f"| > CANTIDAD DE NOCHES:                 {cat_noches}")
        print(f"| > CANTIDAD HABITACIONES RESERVADA:    {cantidad_reserva}")
        print(f"| > HABITACIONES DISPONIBLES:           {disponible - 1}")
        print("-------------------------------------------------------------|")
        print(f"|              TOTAL A PAGAR:  ${subtotal:,.0f}                       |")         
        print("==============================================================")
        
        print("")

        nueva_reserva = input("Desea realizar otra reserva [SI / NO]: ").upper()
        if nueva_reserva == "SI":
            os.system("cls")
        elif nueva_reserva == "NO":
            print(f"Gracias por elegirnos estimad@ {nombre.title()}. Hasta luego.")
            break
        else:
            print("La opcion ingresada no es valida, ingrese (SI o NO):")

    except ValueError as e:
        print(f"ERROR: {e}")


