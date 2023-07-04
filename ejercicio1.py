"""Escribe, en Python, un programa que muestre en pantalla los números del 0 al 100,
sustituyendo los múltiplos de 3 por la palabra "Fizz" y, a su vez, los múltiplos de 5 por "Buzz".
Cuando, al mismo tiempo, son múltiplos de 3 y 5, utiliza 'FizzBuzz'"""

def fizz_buzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizz_buzz(40)
