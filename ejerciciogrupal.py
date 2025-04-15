ingreso=(int(input('Para convertir de decimal a binario ingrese 1, de binario a decimal ingrese 0: ')))
binario=''   
    
if ingreso == 1 :
    numero=int(input("Ingrese el numero que desea pasar a binario:"))
    binario=""

    while numero > 0:
        if numero %2 == 0:
            binario="0"+ binario
        else:
            binario="1"+ binario
        numero=numero//2

    print("El numero en binario es:", binario)

elif ingreso == 0:  
#Pasar de binario a decimal
    binario=input('ingresa el binario')
    decimal=0
    potencia=0
    for digito in reversed(binario):
      if digito == '1':
          decimal += 2 ** potencia
      potencia += 1
    print(f'el binario ingresado: {binario}, es en decimal: {decimal}')
 
else:
    print('Ingreso invalido.')

