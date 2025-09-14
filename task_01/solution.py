# Задание 1: Переменные и типы данных
# Заполните переменные согласно их описанию


def get_variables():
    # Целое число
    integer_number = 18

    # Число с плавающей точкой
    float_number = 3.32617671

    # Строка
    string_value = "None"

    # Логическое значение (истина)
    boolean_true = True

    # Логическое значение (ложь)
    boolean_false = False

    # Список из чисел от 1 до 5
    list_of_numbers = [1, 2, 3, 4, 5]

    # Словарь с ключами 'name' и 'age', и соответствующими значениями
    dictionary = {'name' : 'Alice', 'age' : 18}

    # Вернуть все переменные в виде кортежа
    return (
        integer_number,
        float_number,
        string_value,
        boolean_true,
        boolean_false,
        list_of_numbers,
        dictionary,
    )
