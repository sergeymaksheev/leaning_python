"""Dunder methods"""

# Dunder method - специальный метод внутри класса, который начинается с двух нижних подчеркиваний и
# оканчивается ими.
# Они берут на себя функционал и вызываются автоматически в определенный момент внутри вашего класса.

# Например, метод __init__ вызывается сразу после создания объекта вашего класса.

# __str__ и __repr__ - Отвечают за текстовое изображение объекта в системе.


class Cat:
    """This is class Cat"""

    def __init__(self, name) -> None:
        self.name = name

    def __repr__(self) -> str:
        return f"The object Cat - {self.name}"  # изменение отображения объекта в консоли для разработчика

    def __str__(self) -> str:
        return f"Cat - {self.name}"  # изменение отображения объекта при вызове команды print


cat = Cat("Milka")  # The object Cat
cat  # The object Cat - Milka
print(cat)  # Cat - Milka


# __new__
class Car:
    """Class Car"""

    model = "BMW"  # Атрибуты класса.
    engine = 1.6


car1.__new__(Car)  # оздание нового экземпляра класса


# __len__ и __abs__


class Person:
    """This is class Person"""

    def __init__(self, name, surname) -> None:
        self.name = name
        self.surname = surname

    # Метод __len__ изначально у класса Person отсутствует. При вызове будет ошибка.
    # Определяем метод __len__ для класса Person

    def __len__(self) -> int:
        return len(self.name + self.surname)


person = Person("Ivan", "Ivanov")

len(person)


class LineSegment:
    """LineSegment"""

    def __init__(self, point1, point2) -> None:
        self.x1 = point1
        self.x2 = point2

    def __len__(self) -> None:
        res = abs(self.x2 - self.x1)
        return res


# __add__, __mul__, __sub__, __truediv__
