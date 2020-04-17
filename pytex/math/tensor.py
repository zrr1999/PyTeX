from pytex.math.variable import Variable


class Tensor(object):
    """
    >>> x=Tensor(Variable("x"), Variable("y"))
    $向量latex代码$
    >>> x**2
    $向量latex代码^2$
    >>> x/2
    $\frac {向量latex代码} {2}$
    """
    def __init__(self, variables):
        """

        :param variables: 一个变量列表，对于非变量元素可以自动转化成变量元素
        """
        pass

    def __repr__(self):
        """

        :return: str
        """
        return "t"
