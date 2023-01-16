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
