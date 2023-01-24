"""Magic method __init__"""


# Магические методы в Python начинаются с двух нижних подчеркиваний.
class Cat:
    """Class Cat"""

    def __init__(
        self, name
    ) -> (
        None
    ):  # Метод принимает экземпляр класса, принимая его в качестве аргумента и вызывается
        self.name = name
        print("Hello")  # при создании экземпляра класса

    def show_age(self, age):
        """Show cat's age"""
        self.age = (
            age  # данный атрибут не присваивается в момент инициализации нового объекта
        )
        print(f"Age is {age} years old")


cat1 = Cat("Milka")
print(cat1.name)

# print(cat1.age) - AttributeError: 'Cat' object has no attribute 'age'
