#código de ejercicio de bucles
import time
start_time = time.time()

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b

valores_n = [1, 10, 20, 30, 40]

for n in valores_n:
    resultado = fibonacci(n)
    end_time = time.time()
    tiempo_ejecucion = end_time - start_time

    print(f"Para {n}, resultado {resultado} y tiempo de ejecución es {tiempo_ejecucion:.6f} seg.")