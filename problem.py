from pylatex import Subsection, Enumerate
from pylatex.utils import NoEscape

chinese_nums = ["一", "二", "三", "四", "五", "六"]


class Problem:
    def __init__(self, core, name, describe, score):
        core.big_num += 1
        self.core = core
        self.name = name
        if describe == "":
            self.describe = "."
        else:
            self.describe = "，" + describe
        if type(score) is list:
            self.score = score
            self.score_sum = sum(score)
        else:
            self.score = score
            self.score_sum = 0

    def set(self, *problems):
        n = len(problems)
        if type(self.score) is list:
            title = f'本大题共{n}小题，共{self.score_sum}分'
        else:
            title = f'本大题共{n}小题，每小题{self.score}分，共{n * self.score}分'
        title = f"{self.name}: {title}{self.describe}"
        with self.core.doc.create(Subsection(f'{chinese_nums[self.core.big_num]}、' + title, False)):
            with self.core.doc.create(Enumerate()) as enum:
                self.core.doc.append(NoEscape(r"\addtocounter{enumi}" + str(self.core.num)))
                for i, problem in enumerate(problems):
                    if type(self.score) is list:
                        if type(problem) is str:
                            enum.add_item(NoEscape(f"({self.score[i]}分)" + problem))
                        else:
                            enum.add_item(f"({self.score[i]}分)" + problem)
                    else:
                        if type(problem) is str:
                            enum.add_item(NoEscape(problem))
                        else:
                            enum.add_item(problem)

        self.core.num += n

