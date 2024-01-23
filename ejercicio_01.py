#código de ejercicio recursivo
import datetime

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
def ejecucion(n):
    start_time = datetime.datetime.now()
    resultado = fibonacci(n)
    end_time = datetime.datetime.now()
    tiempo_ejecucion = end_time - start_time
    return resultado, tiempo_ejecucion

n_valor = [1, 10, 20, 30, 40]
for n in n_valor:
    resultado, tiempo = ejecucion(n)
    print(f"Para {n}, resultado {resultado} y tiempo de ejecución es {tiempo} seg.")