import time
import math

def calcular_erro():
    aprox = float(input("Digite o valor aproximado: "))
    exato = float(input("Digite o valor de referência: "))

    erro_abs = abs(exato - aprox)
    erro_rel = erro_abs / abs(exato) if exato != 0 else float('inf')

    print(f"\nErro absoluto: {erro_abs:.10f}")
    print(f"Erro relativo: {erro_rel:.10%}")

# Métodos numéricos
def euler(f, x0, y0, h, n):
    x, y = x0, y0
    for i in range(n):
        y += h * f(x, y)
        x += h
        print("Iteração", i + 1, ":")
        print(f"x = {x:.6f}, y = {y:.6f}")

    return x, y

def euler_melhorado(f, x0, y0, h, n):
    x, y = x0, y0
    for i in range(n):
        k1 = f(x, y)
        k2 = f(x + h, y + h * k1)
        y += (h / 2) * (k1 + k2)
        x += h
        print("Iteração", i + 1, ":")
        print(f"x = {x:.6f}, y = {y:.6f}")
    return x, y

def runge_kutta_3(f, x0, y0, h, n):
    x, y = x0, y0
    for i in range(n):
        k1 = f(x, y)
        k2 = f(x + h/2, y + h * k1 / 2)
        k3 = f(x + h, y - h * k1 + 2 * h * k2)
        y += h * (k1 + 4*k2 + k3) / 6
        x += h
        print("Iteração", i + 1, ":")
        print(f"x = {x:.6f}, y = {y:.6f}")
    return x, y

def runge_kutta_4(f, x0, y0, h, n):
    x, y = x0, y0
    for i in range(n):
        k1 = f(x, y)
        k2 = f(x + h/2, y + h * k1 / 2)
        k3 = f(x + h/2, y + h * k2 / 2)
        k4 = f(x + h, y + h * k3)
        y += h * (k1 + 2*k2 + 2*k3 + k4) / 6
        x += h
        print("Iteração", i + 1, ":")
        print(f"x = {x:.6f}, y = {y:.6f}")
    return x, y

def runge_kutta_5(f, x0, y0, h, n):
    x, y = x0, y0
    for i in range(n):
        k1 = f(x, y)
        k2 = f(x + h/4, y + h * k1 / 4)
        k3 = f(x + h/4, y + h * (k1 + k2) / 8)
        k4 = f(x + h/2, y + h * (-k2 + 2*k3) / 2)
        k5 = f(x + 3*h/4, y + h * (k1 + 4*k4) / 16)
        k6 = f(x + h, y + h * (-3*k1 + 2*k2 + 12*k3 - 12*k4 + 8*k5) / 7)
        y += h * (7*k1 + 32*k3 + 12*k4 + 32*k5 + 7*k6) / 90
        x += h
        print("Iteração", i + 1, ":")
        print(f"x = {x:.6f}, y = {y:.6f}")
    return x, y

print("====== MENU ======")
print("1 - Euler (1ª ordem)")
print("2 - Euler Melhorado (2ª ordem)")
print("3 - Runge-Kutta (3ª ordem)")
print("4 - Runge-Kutta (4ª ordem)")
print("5 - Runge-Kutta (5ª ordem)")
print("6 - Calcular erro")
print("==================")

opcao = int(input("Escolha a opcao: "))

if opcao == 6:
    calcular_erro()

# Entrada da função
expr = input("Digite a funcao dy/dx em termos de x e y (ex: x + y, x*y**(1/3)): ")
f = lambda x, y: eval(expr, {"x": x, "y": y, "math": math})

x0 = float(input("x0: "))
y0 = float(input("y0: "))
h = float(input("Passo h: "))
n = int(input("Numero de passos (n): "))

inicio = time.time()

match opcao:
    case 1:
        xf, yf = euler(f, x0, y0, h, n)
    case 2:
        xf, yf = euler_melhorado(f, x0, y0, h, n)
    case 3:
        xf, yf = runge_kutta_3(f, x0, y0, h, n)
    case 4:
        xf, yf = runge_kutta_4(f, x0, y0, h, n)
    case 5:
        xf, yf = runge_kutta_5(f, x0, y0, h, n)
    case _:
        print("Opção inválida.")

fim = time.time()
print(f"\nResultado: x = {xf}, y = {yf}")
print(f"Tempo de execucao: {fim - inicio:.6f} segundos")