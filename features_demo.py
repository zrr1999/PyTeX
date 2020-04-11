import os
import re

from pylatex import Command, Figure, NewLine, NoEscape

from pytex import Core, DocTree
from pytex.markdown import md2tex
from pytex.pseudocode import algorithm, al_function, al_if

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
        [lambda m: r"\href{" + m.group(1) + "}{" + m.group(1) + "}",
         lambda m: r"\href{" + m.group(1) + "}{" + m.group(2) + "}"],
        package="hyperref"
) as local_core:
    local_core.append(r"使用正则表达式定义复杂局部符号：<a href=www.baidu.com>百度</a> <a>www.baidu.com</a>", mode="re")
core.body_append(NewLine())

md2tex("使用markdown表达式转换为LaTex：**a** a* *a* ***b*** *b", replace=True, core=core)
core.body_append(NewLine())

core.body_append("伪代码：")
al, alc = algorithm("Name", "input", "output", core=core, label=["算法", "输入", "输出"])
func = al_function("name", "args")
func.add_state(NoEscape("$6^6$"))
func.add_state(NoEscape("$2^2$"))
alc.append(func)
core.body_append(al)

_, alc = algorithm("Name", "input", "output", core=core)
con = al_if(NoEscape("$a=1$"))
con.add_state(NoEscape("$4^4$"))
con.append(Command("Else"))
con.add_state(NoEscape("$3^3$"))
alc.append(con)

doc_tree = DocTree({
    "title": "Sec1",
    "content": [{
        "title": "SubSec1",
        "content": "内容"
    }]
})
core.body_append(doc_tree)
#  ——————————特色功能展示——————————

print("正在生成pdf")
core.generate_pdf('resources/example', compiler='XeLatex', clean_tex=False)
print("生成完成！\n欢迎使用PyTex！")
