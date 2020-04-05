import os
import re

from pylatex import Command, NewPage, Figure, NewLine
from pylatex.position import Center
from pylatex.utils import NoEscape

from core import Core
from exam import Question
from markdown import md2tex
from pseudocode import Algorithm, algorithm, al_function, al_if

packages = [["geometry", "a4paper,centering,scale=0.8"], "amsmath", "graphicx", "amssymb"]
core = Core(packages=packages, debug=True)

define = [[r"\dif"], [r"\text{d}"]]
core.global_define(*define)

fig = Figure(position='h!')
fig.add_image(os.path.join(os.path.dirname(__file__), "resources/timg.jpg"),
              width=NoEscape(r'0.8\linewidth'))

core.pre_append(title=Command('heiti', 'PyTex特色功能展示'),
                author=Command('kaishu', '六个骨头'),
                date=Command('today'))
core.body_append(Command('maketitle'))

#  ——————————特色功能展示——————————
core.body_append(Command("noindent"))

with core.local_define([r"d"], [r"b"]) as local_core:  # 用r字符写正则表达式
    local_core.append(NoEscape(r"定义简单局部替换：$dif d d dx$"), mode="str")
core.body_append(NewLine())

# with core.local_define([r"\\d"], [r"\\text{d}"]) as local_core:
#     local_core.append(NoEscape(r"定义简单局部符号：$\dif \d \d dx$"), mode="re")
# core.body_append(NewLine())

with core.local_define(
        [re.compile(r"<a>(\S+)</a>"), re.compile(r"<a href=(\S+)>(\S+)</a>")],  # 用r字符写正则表达式
        [lambda m: r"\href{"+m.group(1)+"}{"+m.group(1)+"}",
         lambda m: r"\href{"+m.group(1)+"}{"+m.group(2)+"}"],
        package="hyperref"
) as local_core:
    local_core.append(r"使用正则表达式定义复杂局部符号：<a href=www.baidu.com>百度</a> <a>www.baidu.com</a>", mode="re")
core.body_append(NewLine())

md2tex("使用markdown表达式转换为LaTex：**a** a* *a* ***b*** *b", replace=True, core=core)
core.body_append(NewLine())

core.body_append("伪代码：")
alc = algorithm("Name", "input", "output", core=core, label=["算法"])
func = al_function("name", "args")
func.add_state(NoEscape("$6^6$"))
func.add_state(NoEscape("$2^2$"))
alc.append(func)

alc = algorithm("Name", "input", "output", core=core)
con = al_if(NoEscape("$a=1$"))
con.add_state(NoEscape("$4^4$"))
con.append(Command("Else"))
con.add_state(NoEscape("$3^3$"))
alc.append(con)

#  ——————————特色功能展示——————————

print("正在生成pdf")
core.generate_pdf('resources/competition', compiler='XeLatex', clean_tex=False)


