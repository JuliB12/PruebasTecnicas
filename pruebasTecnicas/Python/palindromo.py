#Palindromo es una palabra que se lee igual de izquierda a derecha que de derecha a izquierda

''' El siguiente programa verifica si una palabra es palindromo o no, se resuelve con estructuras de control'''

def esPalindromo(palabra):
    letters = []
    #Dividir la cadena en un array de letras 
    for i in range(len(palabra)):
        #print(palabra[i])
        letters.append(palabra[i])
    
    #invertir el array con un bucle for 
    invertLetters = []
    for i in range(len(letters)-1, -1, -1):
        invertLetters.append(letters[i])

    #unirs todas las letras del array invertido y guardar el resultado en una variable
    #invertWord = ''.join(invertLetters) #forma 1
    invertWord = ""
    for i in range(len(invertLetters)):
        invertWord += invertLetters[i]
    #print(f'la palabra invertida es: {invertWord}')
        
    return palabra == invertWord
name = 'ana'
resultado = esPalindromo(name)
print(f'es palindromo el nombre {name}: {resultado}')

