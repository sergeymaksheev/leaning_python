from typing import Any, Dict, List, Optional, Union


# __annotations__ - показывает аннотированные (объеявлен тип) значения в функции
def func(a: int, b: int) -> int:
    return a + b  # {'a': int, 'b': int, 'return': int}


# Аннотация коллекции с указанием аннотации ее элементов осуществляется
# с помощью модуля typing


def lower_list(lst: List[str]) -> None:
    """Make str in your list lower cases"""
    for elem in lst:
        print(elem.lower())


lower_list(["A", "B", "C"])

d: Dict[str, int] = {"a": 100, "b": 200}  # Аннотация словаря

e: Any = 12  # В данной переменной может содержаться любой тип


# В данной переменной может содержаться тип int  или None
def get_sum(point1: int, point2: Optional[int] = None) -> int:
    """Return sum point1 and point2"""
    return point1 + point2


# Union - служит для определения нескольких типов данных, которые может
# содержать переменная. В python 3.10 заменен на вертикальную черту


def new_get_sum(point1: int, point2: Union[int, float, str]) -> int:
    """Return sum point1 and point2"""
    return point1 + point2


# def new_get_sum(point1: int, point2: int | float | str] = None) -> int - короткий
# вариант записи метода Union
