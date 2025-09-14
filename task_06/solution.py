# Задание 6: Циклы (while)
# Реализуйте функции с использованием цикла while
from tests.test_multiselects import test_render_multiselect_as_checks_extra


def sum_of_digits(number):
    """
    Возвращает сумму цифр числа
    Например, для 123 результат должен быть 1 + 2 + 3 = 6
    """
    num = abs(number)
    sum = 0
    while num > 0:
        sum += (num % 10)
        num = num // 10
    return sum


def count_digits(number):
    """
    Возвращает количество цифр в числе
    Например, для 123 результат должен быть 3
    """
    k = 0
    if number == 0:
        return 1
    while number != 0:
        k += 1
        number = number // 10
    return k


def reverse_number(number):
    s = ''
    if number == 0:
        return 0
    while number > 0:
        s = s + str(number%10)
        number = number // 10
    return int(s)


def is_prime(number):
    """
    Проверяет, является ли число простым
    Простое число - это число больше 1, которое делится только на 1 и на само себя
    """
    if number <= 1:
        return False
    i = 2
    while i*i <= number:
        if number%i == 0:
            return False
        i+=1
    return True


def gcd(a, b):
    """
    Находит наибольший общий делитель (НОД) двух чисел
    Используйте алгоритм Евклида
    """
    while b:
        a, b = b, a % b
    return a



def binary_search(sorted_list, target):
    """
    Реализует бинарный поиск элемента в отсортированном списке
    Возвращает индекс элемента, если он найден, иначе -1
    """
    l, r = 0, len(sorted_list) - 1
    while l <= r:
        m = (l+r)//2
        m_el = sorted_list[m]
        if m_el == target:
            return m
        elif m_el < target:
            l = m + 1
        else:
            r = m - 1
    return -1
                


