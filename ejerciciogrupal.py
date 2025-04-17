# Bucle principal: se repite hasta que el usuario decida salir
while True:

    # Muestra el menú de opciones
    print("\n" + "="*60)
    print("        *** CONVERSOR BINARIO / DECIMAL ***")
    print("="*60)
    print("Seleccione una opción:")
    print()
    print("  [0]  Binario → Decimal")
    print("  [1]  Decimal → Binario")
    print("="*60)

    # Pide al usuario que ingrese su elección (0 o 1)
    ingreso_char = input("\nElija la opción: ")

    # Valida que el usuario haya ingresado 0 o 1
    while ingreso_char != "1" and ingreso_char != "0":
        print("Entrada inválida. Ingrese 1 o 0.")
        ingreso_char = input("Para convertir de decimal a binario ingrese 1, de binario a decimal ingrese 0: ")       
    
    # Convierte la opción ingresada (texto) a número
    ingreso = int(ingreso_char)

    # Si elige 1, se convierte de decimal a binario
    if ingreso == 1:
        numero_char = input("Ingrese el número que desea pasar a binario: ")

        # Valida que se ingrese un número entero positivo
        while numero_char == "" or not numero_char.isdigit():
            print("Entrada inválida. Ingrese solo números enteros positivos.")
            numero_char = input("Ingrese el número que desea pasar a binario: ")
        
        # Convierte el número ingresado a entero
        numero = int(numero_char)
        binario = ""

        # Si el número es 0, el binario también es 0
        if numero == 0:
                binario = "0"
        else:
            # Convierte decimal a binario dividiendo entre 2 y guardando los restos
            while numero > 0:
                binario = str(numero % 2) + binario
                numero = numero // 2
        # Muestra el resultado en binario
        print("El número en binario es:", binario)

    # Si elige 0, se convierte de binario a decimal
    elif ingreso == 0:
        # Binario a decimal
        binario = input('Ingresa el número binario: ')
        
        # Valida que la entrada no esté vacía y que solo tenga 0 y 1
        while binario == "" or True:
            es_valido = True  # Supone que es válido

            # Verifica que cada carácter sea 0 o 1
            for caracter in binario:
                if caracter != "0" and caracter != "1":
                    es_valido = False
                    break  # Si encuentra otro carácter, no es binario

            if binario == "" or not es_valido:
                print("Entrada inválida. Ingrese solo ceros y unos.")
                binario = input("Introduce un número binario: ")
            else:
                break  # Salimos del while si es válido
        
        # Se inicia la conversión del número binario a decimal
        if reversed(binario):
            decimal = 0
            potencia = 0
            
            # Recorremos el número binario desde el final hacia el principio
            for digito in reversed(binario):
                if digito == '1':
                    decimal += 2 ** potencia
                potencia += 1
            
            # Muestra el resultado en decimal
            print(f'El binario ingresado: {binario}, es en decimal: {decimal}')
        else:
            # Manejo adicional por si se detecta una entrada no válida
            print("Error: el número ingresado no es binario válido (solo debe contener 0 y 1).")

    else:
        # Mensaje de error si la opción ingresada no es válida
        print('Ingreso inválido. Debes ingresar 0 o 1.')
    
    # Pregunta al usuario si desea realizar otra conversión
    repetir = input('\n¿Deseas realizar otra conversión? (si / no): ').lower()
    if repetir != 'si':
        print("¡Hasta la próxima!")
        break  # Sale del bucle y termina el programa