from math import sqrt


print('Добро пожаловать в самую лучшую программу '
      'для вычисления квадратного корня из заданного числа')


def CalculateSquareRoot(Number: float) -> float:
    """Вычисляет квадратный корень."""
    return sqrt(Number)


def calc(your_number: float) -> str:
    """Выводит сообщение с результатом вычислений."""
    if your_number >= 0:
        sqr_from_number: float = CalculateSquareRoot(your_number)
    return (f'Мы вычислили квадратный корень из '
            f'введённого вами числа. Это будет: '
            f'{sqr_from_number}')


print(calc(25.5))
