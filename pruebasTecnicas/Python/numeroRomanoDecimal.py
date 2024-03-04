'''Enunciado ejericio:
crear una función que convierte un número romano a decimal
Ejemplos:
romanoEntero('XVIII') // 18
romanoEntero('XXI') // 21
romanoEntero('CXX') // 120'''

def romanToInteger(roman):
    #crear objeto con numeros romanos y sus correpondientes valores valores numericos  
    romanNumerals = {'I': 1, 'V': 5, 'IX':9, 'X': 10, 'L': 50, 'C': 100, 'CD':400, 'D': 500, 'CM':900,'M': 1000}

    #crear una variable para almacenar el numero que se vaya calculando 
    result=0

    #recorrer el numero romano letra a letra 
    for i in range(len(roman)):
        #si la letra actual es la ultima o si el valor del siguiente caracter es menor o igual al del actual
        print (f'recorrido del roman: {roman[i]},{romanNumerals[roman[i]]}')
        if i == len(roman)-1 or romanNumerals[roman[i]] >= romanNumerals[roman[i+1]]:
            #entonces añadimos el valor al resultado 
            result += romanNumerals[roman[i]]
            print(f'result: {result}')
        else:
            #si no, restamos el valor de la letra actual al resultado 
            result -= romanNumerals[roman[i]] 

    #devolver resultado 
    return result

resultDef = romanToInteger('XIV')
print(resultDef) #18