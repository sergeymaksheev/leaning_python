"""Examples using decorator in python"""
from abc import abstractmethod
from functools import wraps

# Для использования декораторов необходимо понимание функции замыкание


# decorator
def decorator(func):
    """This is decorator for your function"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("start decorator")
        res = func(*args, **kwargs)
        print("finish decorator")

        return res

    # wrapper.__doc__ = func.__doc__    -  эту функцию ывполняет декоратор wraps - сохраняет имя и docstring
    # wrapper.__name__ = func.__name__      декорируемой функции
    return wrapper


@decorator  # say = decorator(say)
def say(name):
    """This function print Hello with name you gave"""
    print("Hello,", name)


print(say.__name__, say.__doc__)
say("Milka")


# Property - класс для реализации методов getter, setter
# getter - возвращает значение приватного свойства name
# setter - установление приватному свойству нового значения
class BankAccount:
    """Class BankAccount"""

    def __init__(self, name, balance, passport) -> None:
        self.name = name
        self.__balance = balance  # private attribute
        self.__passport = passport

    def get_balance(self):
        return self.__balance  # возвращает приватный атрибут

    def set_balance(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Баланс должен быть числом")
        self.__balance = value

    def del_balance(self):
        del self.__balance

    balance = property(fget=get_balance, fset=set_balance, fdel=del_balance)

    my_balance = property()
    my_balance.getter(get_balance)
    my_balance.setter(set_balance)
    my_balance.deleter(del_balance)

    # Декоратор Property позволяет обращаться через setter, getter, deleter не через функции, а через свойства
    # за счет декорирования метод превращается в свойство, по которому можно обращаться
    # Getter и Setter необъодимо называть одним именем.

    @property
    def balance(self):
        return self.__balance

    @property
    def balance(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Баланс должен быть числом")
        self.__balance = value

    # Обратиться как к функции при использовании декоратора не возможно


account1 = BankAccount("Ivan", 100, 42332432)

account1.get_balance()
account1.set_balance(400)


class Person:
    """Init new object for class Person"""

    def __init__(self, name, family) -> None:
        self._name = name
        self._family = family

    def get_name(self):
        """Return value private name"""
        print("From get_name()")
        return self._name

    def set_name(self, value):
        """Set new value for private name"""
        print("From set_name()")
        self._name = value

    name = property(fget=get_name, fset=set_name)
    name = name.getter(get_name)
    name = name.setter(set_name)

    @property
    def family(self):
        """Return name"""
        return self._family

    @family.setter
    def family(self, value):
        self._family = value

    @family.deleter
    def family(self):
        del self._family


Jack = Person("Jake", "Orange")

Jack.family = "Black"
print(Jack.family)
Jack.family = "White"
print(Jack.family)
# del Jack.family  # удаляет свойство
print(Jack.family)


# вычисляемые property


class Square:
    def __init__(self, sq):
        self.side = sq
        # Чтобы результат каждый раз не высчитывался заного, мы можеи воспользоваться следующим свойством
        self.__area = None

    # def area(self):
    #   return self.side**2

    @property  # Используя property мы переопределяем метод, превращая его в свойство
    def area(self):
        if self.__area is None:
            print("calculate")
            self.__area = self.side**2
        return self.__area


square1 = Square(5)
# print(square1.area())

print(square1.area)
print(square1.area)


"""
@with_routing("/api/goods")
def get_goods():
    pass



class BaseMachine:

    @abstractmethod
    def make(self):
        raise NotImplementedError()

    

class GazMachine(BaseMachine):
    def make(self):
        print('Making something')
        """
