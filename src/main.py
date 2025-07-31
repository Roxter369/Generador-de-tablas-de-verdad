import itertools

# Mapeo de operadores a Python
mapeado = {
    '<->': '==',
    '->' : '<=',
    '&&' : ' and ',
    '||' : ' or ',
    '!'  : ' not ',
}

operadores = ['<->', '->', '&&', '||', '!']

def configurar_expresion():
    global expr, expr_py, valores, ancho_columna
    expr = input("Ingrese expresión lógica (&&, ||, !, ->, <->): ").strip()
    # Reemplazar símbolos en el orden definido
    expr_py = expr
    for simb in operadores:
        if simb in expr_py:
            expr_py = expr_py.replace(simb, mapeado[simb])
            
    #Extraer variables
    #valores = variables     
    valores = []
    for caracter in expr:
        # Chequear si es letra
        if (("A" <= caracter <= "Z") or ("a" <= caracter <= "z")) and caracter not in valores:
            valores.append(caracter)
    #Generar un error si se ingresan más de 10 variables
    if len(valores) > 10:
        raise ValueError("Máximo 10 variables permitidos.")
    
    #Calcular ancho de columna según la longitud de las variables
    mayor_long = 0
    for v in valores:
        if len(v) > mayor_long:
            mayor_long = len(v)
    ancho_columna = mayor_long + 2 if mayor_long + 2 > 10 else 10


    #Imprimir encabezado
def encabezado():
    encabezado = ''
    for val in valores:
        encabezado += format(val, f"<{ancho_columna}") + " | "
    encabezado += format("RESULTADO", f"<{ancho_columna}")
    print("\n" + encabezado)
    print("-" * len(encabezado))
    
def tabla_de_verdad():
    #Cambiar los True y False por V y F
    cambio_simbolos = {
        True: "V",
        False: "F"
}
    #Utilizando itertools para iterar todas las combinaciones psobiles de True/False con una longitud igual a len(valores)
    for combinacion in itertools.product([True, False], repeat=len(valores)):
        valores_diccionario = {}
        #Construcción del diccionario "valores" mapeando cada variable a su valor booleano
        for i in range(len(valores)):
            nombre = valores[i]
            valor = combinacion[i]
            valores_diccionario[nombre] = valor
        #Manejo de excepciones para evitar error al evaluar una expresion
        try:
            resultado = eval(expr_py,valores_diccionario)
        except Exception as e:
            print(f"Error al evaluar la expresión: {e}")
            return
        
        #Imprimir fila
        fila = ''
        for v in valores:
            fila += format(cambio_simbolos[valores_diccionario[v]], f"<{ancho_columna}") + " | "
        fila += format(cambio_simbolos[resultado], f"<{ancho_columna}")
        print(fila)
            
#Menú           
def menu():
    configurar_expresion()
    while True:
        opcion = input("\n¿Generar tabla de verdad con esta expresión? (S/N) ").strip().lower()
        if opcion == "s":
            encabezado()
            tabla_de_verdad()
            break
        elif opcion == "n":
            configurar_expresion()
        else:
            print("Opción incorrecta, ingrese S o N.")

# Ejecutar menú
if __name__ == '__main__':
    menu()