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

def solve_iteration(basic_function: Callable[[float], float], derivative_function: Callable[[float], float], initial_approximation, accurance_ε):
    x_before = initial_approximation
    q = 1 / 3 # upper bound of a derivative 
    iterations = 0
    history_of_calculations = []
    if derivative_function(x_before) < 0:
        threshold = accurance_ε
    else:
        threshold = ((1 - q) / q) * accurance_ε    

    while True:
        x_after = basic_function(x_before)
        iterations += 1
        delta = x_after - x_before
        history_of_calculations.append((x_before, x_after, iterations, delta))
        x_before = x_after
        if abs(delta) <= threshold:
            break

    return (x_before, iterations, history_of_calculations)
