from __init__ import *
from pylatex import Command, Package, Math, VectorName, NewPage, Figure, Tabu, Document
from pylatex.utils import italic, NoEscape
from pylatex.position import Center
import matplotlib.pyplot as plt
import os

doc = Document(default_filepath='basic', documentclass='ctexart')
core = Core(doc)
doc.packages.append(Package("geometry", "a4paper,centering,scale=0.8"))
doc.packages.append(Package("amsmath"))
doc.packages.append(Package("graphicx"))
doc.packages.append(Package("tasks"))

fig = Figure(position='h!')
fig.add_image(os.path.join(os.path.dirname(__file__), "timg.jpg"), width=NoEscape(r'0.8\linewidth'))

doc.preamble.append(Command('title', NoEscape(fig.dumps()+r'\heiti 西安电子科技大学爱数社数学竞赛预览卷（模板）')))
doc.preamble.append(Command('author', NoEscape(r'\kaishu 西电爱数社')))
doc.preamble.append(Command('date', NoEscape(r'\today')))

doc.append(NoEscape(r'\maketitle'))
doc.append(NoEscape(r'本试卷分为100分的必答题和10分的选做题，选做题做对加分，做错不扣分，最多累计10分，整卷最高分110分。'))

doc.append(NoEscape(r"\vspace{10cm}"))
with doc.create(Center()) as centered:
    with centered.create(Tabu("X[r] X[r]", spread="1in")) as data_table:
        doc.append(NoEscape(r'\bf{姓名}\ \underline{\hbox to 20mm{}}'))
        doc.append(NoEscape(r'\bf{学号}\ \underline{\hbox to 20mm{}}'))
        doc.append(NoEscape(r'\bf{编号}\ \underline{\hbox to 20mm{}}'))
doc.append(NewPage())

#  ——————————Numpy——————————
vec = array([[2, 3, 4]])
vec_name = VectorName('a')
math = Math(data=[vec_name, '=', vec])
matrix = array([[2, 3, 4],
                [0, 0, 1],
                [0, 0, 2]])
math2 = Math(data=['M=', matrix])
#  ——————————Numpy——————————
#  ——————————PLT——————————
x = [0, 1, 2, 3, 4, 5, 6]
y = [15, 2, 7, 1, 5, 6, 9]
plt.plot(x, y)
#  ——————————PLT——————————
#  ——————————选择题模板——————————
co = choice("这是用选择题模板编写的", "A", "B", "C", "D", "E", "F")
#  ——————————选择题模板——————————

#  ——————————题目内容——————————

p1 = Problem(core, "选择题", "在每小题给出的四个选项中，只有一项是符合题目要求的.", 5)
p2 = Problem(core, "填空题", "", 5)
p3 = Problem(core, "解答题", "解答应写出文字说明、证明过程或演算步骤.", [2, 3, 5])
p4 = Problem(core, "选做题", "考生根据心情作答，酌情给分.", [2, 3, 10])

p1.set(r"$1+1+1=$\underline{\hbox to 10mm{}}", co)
p2.set(r"设$\alpha \in[0.01,0.98]$, 则"
       r"$\lim_{n \to \infty}\left[(n+1)^{\alpha}-n^{\alpha}\right]=$",
       )
p3.set(r"已知$1+1=2$，求$\sum_{i=1}^{0}i$", r"这道题是利用numpy生成的向量和矩阵$=\_=!$" + math.dumps(),
       plot_show(r"这是图是matplotlib生成的$=\_=!$").dumps())
p4.set(r"\emph{“克尔苏加狗”}出自哪款游戏？", "西电和清华哪个学校更强？",
       r"\emph{“一只葫芦娃有两条腿和一个脑袋，一条猴子有四条腿和两个脑袋”}是命题吗？")

#  ——————————题目内容——————————

print("正在生成pdf")
doc.generate_pdf('competition', compiler='XeLatex', clean_tex=False)

print("已知问题")
print("3 换行不能和居中同时使用")
print("4 使用plt生成tex后修改tex不能编译（这是由于pylatex将plt图像保存为临时文件，生成pdf后会被删除）")
print("5 选择题形式无法自定义")

print("新功能")
print("1 随机抽题（计划）")
print("2 集成图片转latex功能（计划）")
print("3 选择题模板（完成）")
print("4 支持markdown（计划）")
