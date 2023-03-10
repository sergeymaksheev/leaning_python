"""Methods and functions in OPP"""


class Car:
    """Class Car"""

    model = "BMW"  # Атрибуты класса.
    engine = 1.6

    # Создание функции внутри класса
    def drive():
        print(
            "Let's go"
        )  # В реальной практике необходимо использование декоратора staticmethod


Car.__dict__
Car.drive()  # Обращение к функции через класс

getattr(Car, "drive")()  # Вызов данной функции через функцию getattr()

car1 = Car()

# car1.drive() - вызов функции через экземпляр класса приводит к ошибке.

print(Car.drive, car1.drive)  # Обращение к ф-и drive как к объекту.
# Для класса объект будет являться функцией, а для экземпляра класса -
# уже методом.


# Методы класса - метод отличается от функции тем, что метод непосредственно связан с
# каким-либо объектом и при вызова метода в качестве аргумента ему добавляется объект, от
# которого он вызывается


class Cat:
    """Class Cat"""

    breed = "pers"

    def hello(*args):
        print("Hello World!")

    def show_breed(self):
        """self - первый аргумент, который принимает метод и который указывает на объект,
        которому вызывается метод. Может использоваться любое слово, но по стандарту используется self
        """
        print(f"my breed is {self.breed}")

    def show_age(self, age):
        self.age = age  # при вызове метода требуется указать один аргумент age, self указывать не нужно.
        print(f"Age is {age} years old")


Milka = Cat()
Milka.hello()
Milka.show_breed()  # Аргумент не нужен, передается по умолчанию как атрибут класса.

Milka.show_age(3)
