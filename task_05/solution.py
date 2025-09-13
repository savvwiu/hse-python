# Задание 5: Циклы (for)
# Реализуйте функции с использованием цикла for


def sum_of_numbers(n):
    """
    Возвращает сумму чисел от 1 до n включительно
    """
    sum = 0
    for i in range(1, n+1):
        sum+=i
    return sum    


def factorial(n):
    """
    Возвращает факториал числа n (произведение чисел от 1 до n)
    Для n <= 1 возвращает 1
    """
    if n <= 1:
        return 1
    fact = 1
    for i in range(1, n+1):
        fact*=i
    return fact    


def count_vowels(s):
    """
    Возвращает количество гласных букв в строке s
    Гласные: 'a', 'e', 'i', 'o', 'u' (регистр не имеет значения)
    """
    k = 0
    for i in range(len(s)):
        if s[i] in 'aeiouAEIOU':
            k+=1
    return k


def find_max(numbers):
    """
    Возвращает максимальное число из списка numbers
    Если список пуст, возвращает None
    """
    if len(numbers)==0:
        return None
    else:
        mx = -100000
        for i in numbers:
            if i > mx:
                mx = i
        return mx        



def filter_even_numbers(numbers):
    """
    Возвращает новый список, содержащий только четные числа из списка numbers
    """
    res = []
    for i in numbers:
        if i%2 == 0:
            res.append(i)
    return res        


def generate_multiplication_table(n):
    """
    Возвращает таблицу умножения размером n x n в виде списка списков
    Например, для n=3 результат должен быть:
    [
        [1, 2, 3],
        [2, 4, 6],
        [3, 6, 9]
    ]
    """
    t = []
    for i in range(1, n+1):
        r = []
        for j in range(1, n+1):
            r.append(i*j)
        t.append(r)
    return t
print(generate_multiplication_table(4))


