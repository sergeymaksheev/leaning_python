"""Work with files in Python"""


file = open(
    r"/home/sergey/projects/learning_python/python/api.txt", encoding="utf-8"
)  # чтение файла при указании полного пути.
# encoding="utf-8" необходимо использовать при работе с кириллицей

# file1 = open("api.txt")
# print(file1.read())

print(
    file.read(3)
)  # Прочитать только первые три символа. Программа запоминает место, где остановилась.
print(file.read(3))  # Прочитать следующие три символа

print(file.readline())  # Прочитать одну строку
print(file.readline())  # Прочитать следующую строку

print(
    file.read()
)  # При запуске прочитает весь файл до конца и далее чтение файла станет не доступно,
# так как файл является итерируемым объектом.

# NB!!! При работе с файлами необходимо закрывать файл при окончании работы с ним!!!
# Если не закрыть файл, то при работе с ним, существует риск того, что память, которую
# занимал файл при работе с ним не освободится.

file.close()

# Однако при работе с файлом во время обработки может произойти ошибка и до метода объекта
# file.close() интерпретатор может не дойти

# По этому существует два варианта работы с файлами: через вызов try exept и через
# менеджер контекста


# С помощью цикла for возможно обойти все строки файла, т. к. файл является итерируемым объектом
file = open(r"/home/sergey/projects/learning_python/python/api.txt", encoding="utf-8")
for row in file:
    print(row)

file.close()

# Побуквенный обход каждой строки
file = open(r"/home/sergey/projects/learning_python/python/api.txt", encoding="utf-8")
for row in file:
    for letter in row:
        print(letter)

file.close()

# Метод создание списка из файла, элентами которого будут строки из файла
file = open(r"/home/sergey/projects/learning_python/python/api.txt", encoding="utf-8")
lst = file.readlines()
print(lst)

file.close()

# Режим записи в файл. По умолчанию при открытии файла запись в него невозможна, т.к. файл открывается
# в режиме только для чтения.

file_copy = open(
    r"/home/sergey/projects/learning_python/python/api copy.txt", "r", encoding="utf-8"
)
# Параметр 'r' - read, который если не указывать будет по умолчанию дает права только на чтение.
# file4.write("helo")  # выдаст ошибку, т.к. файл открыт только для чтения. io.UnsupportedOperation: not writable

file_copy.close()

file_copy = open(
    r"/home/sergey/projects/learning_python/python/api copy.txt", "w", encoding="utf-8"
)
# При замене параметра на 'r' на 'w', файл становится доступным для перезаписи.
file_copy.write("helo")  # Полностью заменяет содержимое файла

file_copy.close()

file_copy = open(
    r"/home/sergey/projects/learning_python/python/api copy.txt", "a", encoding="utf-8"
)
file_copy.write(" World")  # 'a' - режим запист в конец файла без перезаписи

# Одновременная работа в нескольких режимах невозможна.
# Существует режим 'a+', который позволяет одновременно работать в режиме записи в конец файла и чтении.

file_copy.close()

# Менеджер контекста - специальная конструкция управления внешними ресурсами в Python
# Внешние ресурсы: база данных, блокировки, файлы, сессии на сайтах итд.

# Ко всем этим ресурсам мыдолжны вначале подключиться, а затем отключиться
# Менеджер контекста контролирует, что нужно делать, когда мы получаем доступ к ресурсу, и что
# нужно делать, когда нам этот ресурс уже не нужен

# # NB!!! При работе с файлами необходимо закрывать файл при окончании работы с ним!!!
# Однако при работе с файлом во время обработки может произойти ошибка и до метода объекта
# file.close() интерпретатор может не дойти

with open(  # open -  в данном случае объект менеджера контекста
    "/home/sergey/projects/learning_python/python/password.txt", "w", encoding="utf-8"
) as f:
    f.write("123")
    f.write("hello")
print("end")
# f.write(" World!!!") #ValueError: I/O operation on closed file.

# После блока with менеджер контекста автоматически закрывает файл

# Не каждая функция поддерживает менеджер контекста, например функция print()
# with print("Hello") as f:
#    pass  # AttributeError: __enter__ (у функции print не реализован такой магический метод)
# Соответственно не каждый объект может быть объектом менеджера контекста

# При этом можно создать свой собственный объект для менеджера контекста
