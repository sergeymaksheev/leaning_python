"""Introduction"""

# Существует два варианта выполнения программы в Python:
# 1) Интерактивный вариант (консоль Python/ Shell) - днако инструкции мгновенно выполняются,
# может быть полезно для тестирования. Однако инструкции нигде не сохраняются.
# не нужно писать команду print().

# 2) Файловый вариант (стандартный вариант)

# Понятие ОБЪЕКТ в python
# В питоне существует очень много типов объектов: целое число, строка и др.
#
# Числа:
# NB!!! при делении чисел, в том числе целых, результат деления всегда вещественный:
# 8/2 = 4.0
#
# остаток от деления
# 2%7 = 2 - 0 как результат деления и 2 остаток
#
# функции min(), max(), round()
#
# неявные округления
a = round(456, -1)
print(a)  # 460 - до десятков
a = round(456, -2)
print(a)  # 500 - до сотен

# pow(x, y) - возводит одно число в другое
a = pow(2, 3)
print(a)


# Переменные - именованная область памяти, предназначенная для хранения значений
a = 4  # создание переменной в момент присвоения ей значения.

# Переменные нельзя называть зарезервированными ключевыми словами, например class  и т.д.
# Однако возможно назвать переменную именем функции например print,
# но делать так не нужно. в этом случае вы потеряете возможность использовать функцию.

# print = 5
# a = print + 4
# print(a) # TypeError: 'int' object is not callable
