import os
import re

from pylatex import Command, NewPage, Figure
from pylatex.position import Center
from pylatex.utils import NoEscape

from core import Core
from exam import Question
from markdown import md2tex

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

with core.local_define([r"\d"], [r"\text{d}"]) as local_core:
    local_core.append(NoEscape(r"$\dif \d dx$"))

with core.local_define(
        [re.compile(r"<a>(\S+)</a>"), re.compile(r"<a href=(\S+)>(\S+)</a>")],
        [lambda m: r"\href{"+m.group(1)+"}{"+m.group(1)+"}",
         lambda m: r"\href{"+m.group(1)+"}{"+m.group(2)+"}"],
        package="hyperref"
) as local_core:
    local_core.append(r"<a href=www.baidu.com>百度</a> <a>www.baidu.com</a>")

md2tex(core, "**a** a* *a* ***b*** *b")

#  ——————————特色功能展示——————————

print("正在生成pdf")
core.doc.generate_pdf('resources/competition', compiler='XeLatex', clean_tex=False)

