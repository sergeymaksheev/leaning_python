"""Public, private and protect attr and methods"""


class BankAccount:
    """Class BankAccount"""

    def __init__(self, name, balance, passport) -> None:
        self.name = name
        self.balance = balance
        self.passport = passport

    def print_data(self):
        print(self.name, self.balance, self.passport)


# Атрибуты с правом доступа public, доступны как внутри класса, так и вне класса
account1 = BankAccount("Bob", 1000, 4324324324)
account1.print_data()
print(account1.name)
print(account1.balance)
print(account1.passport)


# Protected attributes - создается добавлением перед атрибутом одного нижнего подчеркивания
class BankAccount2:
    """Class BankAccount"""

    def __init__(self, name, balance, passport) -> None:
        self._name = name
        self._balance = balance
        self._passport = passport

    def print_data(self):
        print(self._name, self._balance, self._passport)


account2 = BankAccount2("Bob", 1000, 4324324324)
account2.print_data()
print(account2._name)
print(account2._balance)
print(account2._passport)

# Protected atributes можно вызвать вне класса также, как и public, уровень protected
# в python  устанавливается на уровне согласования.

# Private attributes - создаются добавлением перед атрибутом двух нижних поддчеркиваний.
# Атрибуты Private защищены от вызова вне класса.
# Данный метод в ООП называется инкапсуляция.


class BankAccount3:
    """Class BankAccount"""

    def __init__(self, name, balance, passport) -> None:
        self.__name = name
        self.__balance = balance
        self.__passport = passport

    def __print_data(self):
        print(
            self.__name, self.__balance, self.__passport
        )  # из класса вызов приватных атрибутов возможен


account3 = BankAccount3("Bob", 1000, 4324324324)
print(dir(account3))
account3._BankAccount3__print_data()  # Пробел в безобасности защищенных атрибутов питона. Можно вызвать вне класса.

# account3.__print_data()
# print(account3.__name)
# print(account3.__balance)
# print(account3.__passport) # вызов приведет к ошибке
