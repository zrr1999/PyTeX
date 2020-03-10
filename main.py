from __init__ import *
from pylatex import Command, NewPage, Figure, Tabu, Document, Math
from pylatex.utils import NoEscape
from pylatex.position import Center
import matplotlib.pyplot as plt
import os

doc = Document(default_filepath='basic', documentclass='ctexart')
packages = [["geometry", "a4paper,centering,scale=0.8"], "amsmath", "graphicx", "amssymb"]

core = Core(doc, packages)
core.define(r"\dif", r"\text{d}")

fig = Figure(position='h!')
fig.add_image(os.path.join(os.path.dirname(__file__), "resources/timg.jpg"), width=NoEscape(r'0.8\linewidth'))

core.pre_append(Command('title', NoEscape(fig.dumps() + Command('heiti', 'PyTex示例').dumps())),
                Command('author', Command('kaishu', 'tczrr1999')),
                Command('date', Command('today'))
                )
core.body_append(Command('maketitle'))
core.body_append(NoEscape(r'本试卷分为100分的必答题和10分的选做题，选做题做对加分，做错不扣分，最多累计10分，整卷最高分110分。'))

core.body_append(NoEscape(r"\vspace{10cm}"))
with doc.create(Center()) as centered:
    with centered.create(Tabu("X[r] X[r]", spread="1in")) as data_table:
        data_table.append(NoEscape(r'\bf{姓名}\ \underline{\hbox to 20mm{}}'))
        data_table.append(NoEscape(r'\bf{学号}\ \underline{\hbox to 20mm{}}'))
        data_table.append(NoEscape(r'\bf{编号}\ \underline{\hbox to 20mm{}}'))
core.body_append(NewPage())

#  ——————————题目内容——————————

# p1 = Question(core, "选择题", "在每小题给出的四个选项中，只有一项是符合题目要求的.", 5)
p2 = Question(core, name="填空题", describe="", scores=7)
p3 = Question(core, name="解答题", describe="解答应写出文字说明、证明过程或演算步骤.", line_space=50)
p4 = Question(core, name="选做题", describe="考生根据心情作答，酌情给分.", line_space=50)

p2.set(r"设$\alpha \in[0.01,0.98]$, 则"
       r"$\lim_{n \to \infty}\left[(n+1)^{\alpha}-n^{\alpha}\right]=\underline{\hspace*{4em}}$",

       r"极限 $\lim_{n\to\infty}\sin^2\big(\pi\sqrt{n^2+n}\big)=\underline{\hspace*{4em}}$",

       r"设 $w=f(u,v)$ 具有二阶连续偏导数, 且 $u=x-cy$, $v=x+cy$. 其中 $c$ 为非零常数.\\"
       r"则$w_{xx}-\frac{1}{c^2}w_{yy}=\underline{\hspace*{4em}}$",

       r"设 $f(x)$ 有二阶导数连续, 且 $f(0)=f'(0)=0$, $f''(0)=6$, "
       r"则 $\lim_{n\to\infty}\frac{f(\sin^2x)}{x^4}=\underline{\hspace*{4em}}$",

       r"不定积分 $\int\frac{e^{-\sin x}\sin2x}{(1-\sin x)^2}\dif x=\underline{\hspace*{4em}}$",

       r"记曲面 $z^2=x^2+y^2$ 和 $z=\sqrt{4-x^2-y^2}$ 围成空间区域为 $V$, "
       r"则三重积分 $\iint_Vz\dif x\dif y\dif z=\underline{\hspace*{4em}}$"
       )
p3.set(r"设二元函数 $f(x,y)$ 在平面上有连续的二阶导数. 对任意角度 $\alpha$, "
       r"定义一元函数\[g_{\alpha}(t)=f(t\cos\alpha,t\sin\alpha).\]"
       r"若对任何 $\alpha$ 都有 $\frac{\dif g_{\alpha}(0)}{\dif t}=0$ "
       r"且 $\frac{\dif^2 g_{\alpha}(0)}{\dif t^2}>0$.  求证: $f(0,0)$ 是 $f(x,y)$ 的极小值",

       r"设曲线 $\Gamma$ 为曲线\[x^2+y^2+z^2=1\;,\quad x+z=1\;,"
       r"\quad x\geqslant0\,,\;y\geqslant0\,,\;z\geqslant0\]上从点 $A(1,0,0)$ "
       r"到点 $B(0,0,1)$ 的一段.  求曲线积分 $I=\int\limits_{\Gamma}y\dif x+z\dif y+x\dif z$",

       r"设函数 $f(x)>0$ 且在实轴上连续, 若对任意实数 $t$ , "
       r"有 $\int_{-\infty}^{+\infty}e^{-|t-x|}f(x)\dif x\leqslant1$. "
       r"\\求证 $\forall\,a,b,a<b$, 有 $\int_{a}^{b}f(x)\dif x\leqslant\frac{b-a+2}{2}$.",

       r"设 $\{a_n\}$ 为一个数列, $p$ 为固定的正整数.  "
       r"若 $\lim_{n\to\infty}\big(a_{n+p}-a_n\big)=\lambda$, "
       r"求证: $\lim_{n\to\infty}\frac{a_n}{n}=\frac{\lambda}{p}$",
       scores=[14, 14, 15, 15]
       )

x = array([['x'], ['y'], ['z']])

p4.set(r"在求梯度的时候，经常会将$ f(x, y ,z)$简写成$ f(\boldsymbol x) $其中 $\boldsymbol x="
       f"{x.dumps()}$，使用这种记法，我们可以根据定义很容易证明"
       r"$\nabla (\boldsymbol x \cdot \boldsymbol x)=2\boldsymbol x$。"
       r"试证明 \[ \nabla (|| 2\boldsymbol x - \boldsymbol 1 ||^2)=4(2\boldsymbol x - \boldsymbol 1),\] "
       r"其中$||2\boldsymbol x - \boldsymbol 1||^2=(2\boldsymbol x - \boldsymbol 1)"
       r" \cdot (2\boldsymbol x - \boldsymbol 1)$，$\boldsymbol "
       f"1={array([[1], [1], [1]]).dumps()}$.",

       r"请简述人工智能、机器学习和深度学习的关系.",
       scores=[8, 5]
       )

#  ——————————题目内容——————————

print("正在生成pdf")
doc.generate_pdf('resources/competition', compiler='XeLatex', clean_tex=False)

print("已知问题")
print("换行不能和居中同时使用")

print("待开发功能")
print("1 随机抽题（计划）")
print("2 集成图片转latex功能（计划）")
print("4 支持markdown（计划）")
print("5 自动试题魔改（开发中）")
