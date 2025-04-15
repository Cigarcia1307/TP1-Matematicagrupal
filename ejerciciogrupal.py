while True:
    print("\n*** Programa de conversión de números: binario/decimal - decimal/binario ***\n")
    print()
    print("0 - Convierta binario a decimal")
    print("1 - convierta decimal a binario")

    ingreso_char = input("\nElija la opción: ")

    while ingreso_char != "1" and ingreso_char != "0":
        print("Entrada inválida. Ingrese 1 o 0.")
        ingreso_char = input("Para convertir de decimal a binario ingrese 1, de binario a decimal ingrese 0: ")       
    ingreso = int(ingreso_char)
    if ingreso == 1:
        # Decimal a binario
        numero_char = input("Ingrese el número que desea pasar a binario: ")
        while numero_char == "" or not numero_char.isdigit():
            print("Entrada inválida. Ingrese solo números enteros positivos.")
            numero_char = input("Ingrese el número que desea pasar a binario: ")
        numero = int(numero_char)
        binario = ""

        if numero == 0:
                binario = "0"
        else:
            while numero > 0:
                binario = str(numero % 2) + binario
                numero = numero // 2

        print("El número en binario es:", binario)

    elif ingreso == 0:
        # Binario a decimal
        binario = input('Ingresa el número binario: ')
        while binario == "" or True:
            es_valido = True  

            for caracter in binario:
                if caracter != "0" and caracter != "1":
                    es_valido = False
                    break  

            if binario == "" or not es_valido:
                print("Entrada inválida. Ingrese solo ceros y unos.")
                binario = input("Introduce un número binario: ")
            else:
                break  # Salimos del while si es válido
        if reversed(binario):
            decimal = 0
            potencia = 0
            for digito in reversed(binario):
                if digito == '1':
                    decimal += 2 ** potencia
                potencia += 1
            print(f'El binario ingresado: {binario}, es en decimal: {decimal}')
        else:
            print("Error: el número ingresado no es binario válido (solo debe contener 0 y 1).")

    else:
        print('Ingreso inválido. Debes ingresar 0 o 1.')

    repetir = input('\n¿Deseas realizar otra conversión? (si / no): ').lower()
    if repetir != 'si':
        print("¡Hasta la próxima!")
        break