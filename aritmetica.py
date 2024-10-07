def evaluar_expresion(expresion, tipo):
    pila = []

    if tipo == 'posfija':
        tokens = expresion.split()
    elif tipo == 'prefija':
        tokens = expresion.split()[::-1]
    else:
        raise ValueError("Tipo de notación no soportada. Usa 'posfija' o 'prefija'.")

    for token in tokens:
        if token.isdigit():
            pila.append(int(token))
        else:
            op1 = pila.pop()
            op2 = pila.pop()
            if tipo == 'posfija':
                if token == '+':
                    pila.append(op2 + op1)
                elif token == '-':
                    pila.append(op2 - op1)
                elif token == '*':
                    pila.append(op2 * op1)
                elif token == '/':
                    pila.append(op2 / op1)
            elif tipo == 'prefija':
                if token == '+':
                    pila.append(op1 + op2)
                elif token == '-':
                    pila.append(op1 - op2)
                elif token == '*':
                    pila.append(op1 * op2)
                elif token == '/':
                    pila.append(op1 / op2)
    
    return pila.pop()

expresion = input("Introduce la expresión aritmética: ")
tipo = input("Introduce el tipo de notación ('posfija' o 'prefija'): ")

try:
    resultado = evaluar_expresion(expresion, tipo)
    print(f"Resultado ({tipo}): {resultado}")
except ValueError as e:
    print(e)
