'''
Enunciado ejercicio:
 crea una funcion a la cual le pones un array de numeros y un numero que sera el resultado de la suma de dos de los valores.

Ejemplo :
sumarDos ([3,7,8,2], 10) // [3,7] ambos suman 10
([4,5,9,1],10)
([1,2,3,4],5)

'''

def sumTwo (number, resultado):
    # recorrer el array de numeros
    for i in range(len(number)):
        number[i]
        firstNumber = number[i]
        print(f'primer numero: {number[i]}')
        #calculo, para sacar el segundo numero para devovler el resultado
        secondNumber = resultado - number[i] 
        print(f'segundo numero {secondNumber}' )  

        #comprar si existe un segundo numero en el array que sumado al actual sea igual al resultado esperado 
        #comprar que la variable (segundo numero) el valor es distinto al primer numero 

        if secondNumber in number and secondNumber != firstNumber:
            return [firstNumber, secondNumber]


    #si se cumple la condicion devolver un array con el numero actual que estoy recorriendo y el segundo numero calculado  
        
resultado =sumTwo([3,8,2,5],10) # [3,7] ambos suman 10
print(resultado) # [3,7] ambos suman 10