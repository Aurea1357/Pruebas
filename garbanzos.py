num1 = float(input("Primer cantidad de garbanzos: "))
op = input("Operador: ")
num2 = float(input("Segundo cantidad de garbanzos: "))
print("Garbanzos totales: ")
if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("ERROR: Introduce un operador valido.")
