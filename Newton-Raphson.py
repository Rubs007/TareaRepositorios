import math


def newton_raphson(f, df, x0, tolerance=1e-7, max_iterations=1000):
    """
    Método de Newton-Raphson para encontrar la raíz de la función f.

    :param f: La función cuya raíz queremos encontrar.
    :param df: La derivada de la función f.
    :param x0: El valor inicial para comenzar el método.
    :param tolerance: La tolerancia para el criterio de parada.
    :param max_iterations: El número máximo de iteraciones.
    :return: La aproximación de la raíz.
    """
    x = x0
    for i in range(max_iterations):
        fx = f(x)
        dfx = df(x)
        if abs(fx) < tolerance:
            print(f'Convergió a {x} después de {i} iteraciones')
            return x
        if dfx == 0:
            print('La derivada es cero. No se puede continuar.')
            return None
        x = x - fx / dfx
    print('Se alcanzó el número máximo de iteraciones sin convergencia.')
    return x

# Definimos la función f(x) = ln(x^2) y su derivada f'(x) = 2/x


def f(x):
    return math.log(x**2) + math.exp(x**2)


def df(x):
    return 2/x + math.exp(x**2)


# Usamos el método de Newton-Raphson con un valor inicial, por ejemplo 0.5
raiz = newton_raphson(f, df, 0.5)
print(f'La raíz aproximada es: {raiz}')
