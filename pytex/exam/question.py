from pylatex import Subsection, Enumerate
from pylatex.utils import NoEscapeStr

chinese_nums = ["一", "二", "三", "四", "五", "六"]


class Question:
    def __init__(self, core, name, describe, scores=0, line_space=2):
        """Init this question."""
        self.number = core.big_num
        core.big_num += 1
        self.core = core
        self.name = name
        self.line_space = line_space

        if describe == "":
            self.describe = "."
        else:
            self.describe = "，" + describe
        self.scores = scores

    def set(self, *problems, scores=None, line_space=None):
        """Set this question and output it."""
        if scores is None:
            if self.scores is None:
                print("你必须给定明确的分数（scores参数）")
            else:
                scores = self.scores
        if line_space is None:
            line_space = self.line_space

        n = len(problems)
        if type(scores) is list:
            title = f'本大题共{n}小题，共{sum(scores[:len(problems)])}分'
        else:
            title = f'本大题共{n}小题，每小题{scores}分，共{n * scores}分'
        title = f"{self.name}: {title}{self.describe}"
        with self.core.create(Subsection(f'{chinese_nums[self.number]}、' + title, False)):
            with self.core.create(Enumerate()) as enum:
                self.core.append(NoEscapeStr(r"\addtocounter{enumi}" + f"{{{self.core.num}}}"))
                for i, problem in enumerate(problems):
                    if type(scores) is list:
                        enum.add_item(NoEscapeStr(f"(本题{scores[i]}分)" + problem))
                    else:
                        if type(problem) is str:
                            enum.add_item(NoEscapeStr(problem))
                        else:
                            enum.add_item(problem)
                    enum.append(NoEscapeStr(f"\\\\[{line_space}mm]"))

        self.core.num += n
