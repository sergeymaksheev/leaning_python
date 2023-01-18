"""Mononstate for all object in class"""


class Cat:
    """Class Cat"""

    breed = "pers"

    __shared_attr = {"breed": "pers", "color": "black"}

    def __init__(self):
        self.__private_field: int = 50
        """При инициализации экземпляра класса функция переопределят словарь атрибутов
        экземпляра на общий словарь, заданный в классе"""
        self.__dict__ = Cat.__shared_attr


# Все атрибуты классов при инициализации класса перезаписываются для всех экземпляров классов.
# В данном случае подобрая работа python на практике может быть неккоректной.
cat1 = Cat()

cat2 = Cat()

cat1.breed = "siam"  # прозошло переопределение атрибута breed для cat1

cat1.color = "black"  # создан личный атрибут для объекта cat2

cat1.name = "Milka"

cat1.breed = "siam"
print(cat2.breed, cat2.color, cat2.name)
