# Задание 4: Условные операторы (if-else)
# Реализуйте функции с использованием условных операторов


def is_positive(number):
    """
    Возвращает True, если число положительное, иначе False
    """
    if number > 0:
        return True
    else:
        return False


def is_even(number):
    """
    Возвращает True, если число четное, иначе False
    """
    if number % 2 == 0:
        return True
    else:
        return False


def is_in_range(number, start, end):
    """
    Возвращает True, если число находится в диапазоне [start, end], иначе False
    """
    if number >= start and number <= end:
        return True
    else:
        return False


def max_of_three(a, b, c):
    """
    Возвращает максимальное из трех чисел
    """
    if a >= b and a >= c:
        return a
    elif b >= c and b >= a:
        return b
    elif c >= b and c >= a:
        return c


def fizz_buzz(number):
    """
    Если число делится на 3, возвращает "Fizz"
    Если число делится на 5, возвращает "Buzz"
    Если число делится и на 3, и на 5, возвращает "FizzBuzz"
    Иначе возвращает само число в виде строки
    """
    if number % 3 == 0 and number % 5 == 0:
        return 'FizzBuzz'
    elif number % 3 == 0:
        return 'Fizz'
    elif number % 5 == 0:
        return 'Buzz'
    else:
        return str(number)


def grade_converter(score):
    """
    Конвертирует числовую оценку в буквенную:
    90-100: 'A'
    80-89: 'B'
    70-79: 'C'
    60-69: 'D'
    0-59: 'F'
    Если score не в диапазоне 0-100, возвращает 'Invalid score'
    """
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score <= 89:
        return 'B'
    elif 70 <= score <= 79:
        return 'C'
    elif 60 <= score <= 69:
        return 'D'
    elif 0 <= score <= 59:
        return 'F'
    else:
        return 'Invalid score'
