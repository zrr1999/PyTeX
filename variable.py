class Variable(object):
    """一个存储变量和运算变量的类

    属性：
        name：传递进来的值，字符串或数字

    """

    def __init__(self, name):
        """

        :param name: 变量的显示名字，支持传入数字
        """
        self.name = str(name)
        pass

    def __repr__(self):
        """

        :return: 返回字符串型的变量名
        """
        return self.name

    def __add__(self, other):
        """
        :param other:参与到运算的一个变量或者值
        :return: +运算符重载，返回计算后的结果
        """
        return self.name + "+" + str(other)

    def __sub__(self, other):
        """

        :return: -运算符重载，返回计算后的结果
        """
        return self.name + "-" + str(other)

    def __mul__(self, other):
        """

        :return: *运算符重载，返回计算后的结果
        """
        return self.name + "*" + str(other)

    def __truediv__(self, other):
        """

        :return: /运算符重载，返回计算后的结果，Latex公式
        """
        return "\\frac {" + self.name + "} {" + str(other) + "}"

    def __floordiv__(self, other):
        """

        :return: //运算符重载，返回计算后的结果
        """
        return self.name + "//" + str(other)

    def __mod__(self, other):
        """

        :return: %运算符重载，返回计算后的结果
        """
        return self.name + "%" + str(other)

    def __pow__(self, other):
        """

        :return: **运算符重载，返回计算后的结果
        """
        return self.name + "**" + str(other)
