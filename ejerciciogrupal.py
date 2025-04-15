while True:
    
    ingreso = int(input('\nPara convertir de decimal a binario ingrese 1, de binario a decimal ingrese 0: '))

    if ingreso == 1:
        # Decimal a binario
        numero = int(input("Ingrese el número que desea pasar a binario: "))
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