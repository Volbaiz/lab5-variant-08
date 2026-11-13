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

def save_results_to_file(filename: str, data: tuple[float, int, list[tuple[float, float, int, float]]]) -> None:
    root, iterations, history = data
    with open(filename, "w", encoding = 'utf-8') as file:
        file.write(f"The solution is: \n")
        file.write(f"The root is: {root:.6f} \n")
        file.write(f"The quantity of iterations: {iterations} \n\n\n")
        file.write(f"{'Iteration':<12} | {'x_before':>10} | {'x_after':>10} | {'delta':>9} \n")
        file.write("*" * 50 + "\n")
        for x_before, x_after, iterations, delta in history:
            file.write(f"{iterations:>12} | {x_before:>10.6f} | {x_after:>10.6f} | {abs(delta):>9.6f} \n")
