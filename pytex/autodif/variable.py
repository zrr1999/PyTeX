import numpy as np


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


class Variable:
    def __init__(self, value=None, grad_fn=None, node=None, require_grad=False):
        if type(value) is not np.array:
            value = np.array(value)
        self.value = value
        self.grad_fn = grad_fn
        self.node = node
        self.grad = None
        self.require_grad = require_grad
        self.shape = self.value.shape

    def __str__(self):
        return "Variable({})".format(np.round(self.value, 2))

    def __add__(self, other):
        return add(self, other)

    def __iadd__(self, other):
        return add(self, other)

    def __radd__(self, other):
        return add(self, other)

    def __sub__(self, other):
        return sub(self, other)

    def __isub__(self, other):
        return sub(self, other)

    def __rsub__(self, other):
        return sub(other, self)

    def __mul__(self, other):
        return mul(self, other)

    def __matmul__(self, other):
        return matmul(self, other)

    def __imul__(self, other):
        return mul(self, other)

    def __rmul__(self, other):
        return mul(self, other)

    def __truediv__(self, other):
        return truediv(self, other)

    def __idiv__(self, other):
        return truediv(self, other)

    def __rtruediv__(self, other):
        return truediv(other, self)

    def __pow__(self, power):
        return pow(self, power)

    def __rpow__(self, other):
        return pow(other, self)

    def t(self):
        return Variable(self.value.T, self.grad_fn, self.node, self.require_grad)

    def backward(self, grad=None):
        """
        :type self:Variable
        :type grad
        """
        if grad:
            if type(grad) != Variable:
                grad = Variable(grad)
            if self.grad:
                self.grad += grad
            else:
                self.grad = grad
        if self.grad_fn:
            grad_ = diff(self.node, self.grad_fn)
            if grad:
                for i, node in enumerate(self.node):
                    if node.require_grad:
                        if self.grad_fn == "matmul":
                            if i == 0:
                                node.backward(grad @ grad_[i])
                            else:
                                print(grad, grad_[i])
                                node.backward(grad_[i] @ grad)
                        else:
                            node.backward(grad * grad_[i])
            else:
                for i, node in enumerate(self.node):
                    if node.require_grad:
                        node.backward(grad_[i])

    def zero_grad(self):
        self.grad = None
        if self.node:
            for node in self.node:
                node.zero_grad()
