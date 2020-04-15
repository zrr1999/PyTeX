from .core import Core


class ExamCore(Core):
    def __init__(self, packages=None, debug=None, **kwargs):
        super().__init__(packages, debug, **kwargs)
        self.big_num = 0
        self.num = 0

    def set(self, add_big_num, add_num):
        self.big_num += add_big_num
        self.num += add_num
