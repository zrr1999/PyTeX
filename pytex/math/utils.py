import numpy as np
from .variable import Variable


def add(a, b):
    """
    :type a:Optional[int]
    :type b: Optional[int]
    """
    if type(b) != Variable:
        b = Variable(b)
    return Variable(a.value + b.value, "add", (a, b), True)


def sub(a, b):
    """
    :type a:Optional[int]
    :type b: Optional[int]
    """
    if type(a) != Variable:
        a = Variable(a)
    if type(b) != Variable:
        b = Variable(b)
    return Variable(a.value - b.value, "sub", (a, b), True)


def mul(a, b):
    """
    :type a:Optional[int]
    :type b: Optional[int]
    """
    if type(b) != Variable:
        b = Variable(b)
    return Variable(a.value * b.value, "mul", (a, b), True)


def matmul(a, b):
    """
    :type a:Optional[int]
    :type b: Optional[int]
    """
    if type(b) != Variable:
        b = Variable(b)
    return Variable(a.value @ b.value, "matmul", (a, b), True)


def truediv(a, b):
    """
    :type a: Optional[int]
    :type b: Optional[int]
    """
    if type(a) != Variable:
        a = Variable(a)
    if type(b) != Variable:
        b = Variable(b)
    return Variable(a.value / b.value, "div", (a, b), True)


def pow(a, b):
    """
    :type a:Optional[int]
    :type b: Optional[int]
    """
    if b == 0:
        return Variable(1)
    elif a == 0:
        return Variable(0)
    else:
        if type(a) != Variable:
            a = Variable(a)
        if type(b) != Variable:
            b = Variable(b)
        return Variable(a.value ** b.value, "pow", (a, b), True)


def log(x):
    """
    :type x:Optional[int]
    """
    if type(x) != Variable:
        x = Variable(x)
    return Variable(np.log(x.value), "ln", (x,), True)


def exp(x):
    """
    :type x:Optional[int]
    """
    if type(x) != Variable:
        x = Variable(x)
    return Variable(np.exp(x.value), "exp", (x,), True)


def diff(value, func):
    if func == "add":
        one = Variable(np.ones_like(value))
        return one, one
    elif func == "mul":
        return value[::-1]
    elif func == "matmul":
        return value[1].t(), value[0].t()
    elif func == "pow":
        return value[1] * (value[0] ** (value[1] - 1)), value[0] ** value[1] * log(value[0])
    elif func == "exp":
        return exp(value[0]),
    elif func == "log":
        return 1 / value[0],
    elif func == "div":
        return 1 / value[1], -value[0] / value[1] ** 2
    elif func == "sub":
        one = Variable(np.ones_like(value))
        return one, one

