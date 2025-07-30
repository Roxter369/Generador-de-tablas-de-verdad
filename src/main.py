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
    expr = input("Ingrese expresión lógica (&&, ||, !, ->, <->): ").strip()
    # Reemplazar símbolos en el orden definido
    expr_py = expr
    for simb in operadores:
        if simb in expr_py:
            expr_py = expr_py.replace(simb, mapeado[simb])
            
    #Extraer variables
    #vars = variables     
    vars = []
    for caracter in expr:
        # Chequear si es letra
        if (("A" <= caracter <= "Z") or ("a" <= caracter <= "z")) and caracter not in vars:
            vars.append(caracter)
    #Generar un error si se ingresan más de 10 variables
    if len(vars) > 10:
        raise ValueError("Máximo 10 variables permitidos.")
    
    #Calcular ancho de columna según la longitud de las variables
    mayor_long = 0
    for v in vars:
        if len(v) > mayor_long:
            mayor_long = len(v)
    ancho_columna = mayor_long + 2 if mayor_long + 2 > 10 else 10

    #Imprimir encabezado
    encabezado = ''
    for var in vars:
        encabezado += format(var, f"<{ancho_columna}") + " | "
    encabezado += format("RESULTADO", f"<{ancho_columna}")
    print("\n" + encabezado)
    print("-" * len(encabezado))
            
#Menú           
def menu():
    configurar_expresion()
    while True:
        opcion = input("\n¿Generar tabla de verdad con esta expresión? (S/N) ").strip().lower()
        if opcion == "s":
            break
        elif opcion == "n":
            configurar_expresion()
        else:
            print("Opción incorrecta, ingrese S o N.")

# Ejecutar menú
if __name__ == '__main__':
    menu()