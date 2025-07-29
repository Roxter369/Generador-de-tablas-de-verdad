expr = input("Ingrese expresión lógica (&&, ||, !, ->, <->): ").strip()

# Mapeo de operadores a Python
mapeado = {
    '<->': '==',
    '->' : '<=',
    '&&' : ' and ',
    '||' : ' or ',
    '!'  : ' not ',
}

expr_py = expr
for simb, py in mapeado.items():
    expr_py = expr_py.replace(simb, py)