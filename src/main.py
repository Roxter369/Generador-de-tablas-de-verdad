
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
            
#Menú           
def menu():
    configurar_expresion()
    while True:
        opcion = input("\n¿Generar tabla de verdad con esta expresión? (S/N) ").strip().lower()
        if opcion == 's':
            break
        elif opcion == 'n':
            configurar_expresion()
        else:
            print("Opción incorrecta, ingrese S o N.")

# Ejecutar menú
if __name__ == '__main__':
    menu()