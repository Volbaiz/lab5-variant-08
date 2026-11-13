"""
Лабораторна робота №5: Варіант 8
Студент: Зяблов Нікіта
Група: EIP30

"""

from math import sin, cos
from typing import Callable

def target_function(x) -> float:
    return sin(x ** 2) - 6 * x + 1

def phi(x) -> float:
    return ((sin(x ** 2) / 6) + (1 / 6))

def d_phi(x) -> float:
    return(1 / 3) * x * cos(x ** 2)
