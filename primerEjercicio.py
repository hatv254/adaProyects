import sys

# Define una variable de cada tipo de primitivo
numero = 9999 #int
flotante = 3.14 #float
boleano = True #Boolean
texto = "Hola mundo" #String
print(f"Define una variable de cada tipo de primitivo\nInt: {numero}\nFlotatne: {flotante}\nBoolean: {boleano}\nTexto: {texto}")

# Concatena a la cadena las otras variables aplicando la conversión correcta para funcionar, guarda el resultado en una variable
texto2 = str(numero) + str(flotante) + str(boleano) + texto
print(f"\nConcatena a la cadena las otras variables aplicando la conversión correcta para funcionar, guarda el resultado en una variable \n{texto2}")

# Investiga sobre el límite de los enteros y los flotantes en python y anotar sus descubrimientos como comentarios en el archivo
print("\nInvestiga sobre el límite de los enteros y los flotantes en python y anotar sus descubrimientos como comentarios en el archivo")
print(f"Int tiene un tamaño maximo de 2**31 - 1 en un entorno de 32 bits y 2**63 - 1 en un entorno de 64 bits en Python 2 y en Python 3 int es indiferente que long y no tiene un tamaño ni minimo non maximo. Lo podemos revisar de la siguiente manera: \nprint(sys.maxsize)={sys.maxsize}")

# Aplica la fórmula de la suma de los primeros n números pares (investigar), tomando como n la variable de tipo entero y almacenar el resultado 
# en una variable
numero = 16
suma_pares = numero*(numero+1)
print("\nAplica la fórmula de la suma de los primeros n números pares (investigar), tomando como n la variable de tipo entero y almacenar el resultado en una variable")
print(f"Formula S=N(N+1)\nEjemplo con el numero 16 es {suma_pares}")
