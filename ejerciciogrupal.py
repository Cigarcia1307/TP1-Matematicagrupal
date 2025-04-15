binario=""

numero=int(input("Ingrese un numero que desea pasar a binario:"))


while numero > 0:
    if numero %2 == 0:
        binario="0"+ binario
    else:
        binario="1"+ binario
    numero=numero//2

print("El numero en binario es:", binario)

#Pasar de binario a decimal

decimal=0
pos=len(binario)

for i in reversed (binario):
    if i == "1":
        decimal=decimal + pow(2,(len(binario)-pos))
    pos=pos-1

print("el nuemro en decimal es:",decimal)



