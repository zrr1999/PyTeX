import os

from pylatex import Command, NewPage, LongTable, MultiColumn
from pylatex.position import Center
from pylatex.utils import NoEscape

from pytex import MathCore, Abstract, abstract
from pytex.math import DocTree, Appendices, appendices, table

core = MathCore(packages=["amsmath", "graphicx", "amssymb", "cite"])
core.define([r"\dif", ], [r"\text{d}", ])
core.pre_append(title=Command('ha', '数学建模'), date="")

# core.add_pdf("standard.pdf")
core.body_append(Command('maketitle'))
core.body_append(Abstract("这是一个摘要的示例", ["关键词1", "关键词2"]))
core.body_append(NewPage())

data_table = table()
row = ["Content1", "这个描述最好不要超过一行"]
for i in range(5):
    data_table.add_row(row)
# 问题重述
wtcs = [{
    "title": "背景资料与条件",
    "content": "出租车是市民出行的重要交通工具之一，"
               "“打车难”是人们关注的一个社会热点问题。"
               "随着“互联网+”时代的到来，有多家公司依托移动互联网建立了打车软件服务平台，"
               "实现了乘客与出租车司机之间的信息互通，同时推出了多种出租车的补贴方案。"
}, {
    "title": "需要解决的问题",
    "content": "0_0"
}]


doctree = DocTree({
    "title": "问题重述",
    "content": wtcs
}, {
    "title": "问题分析",
    "content": "这是一个严肃的问题分析"
},  {
    "title": "模型假设",
    "content": "这是一个严肃的模型假设"
},  {
    "title": "符号说明",
    "content": data_table
},  {
    "title": "模型的建立与求解",
    "content": NoEscape(r"小明研究过\cite{name1}小黑根据哈士奇原理\cite{name2}发明的冰淇淋\cite{name3}，不过后来放弃了。")
},  {
    "title": "模型的评价",
    "content": "这是一个严肃的评价"
}, {
    "title": "模型的改进与推广",
    "content": "这是一个优秀的改进"
})
core.body_append(doctree)
core.body_append(NoEscape(r"\bibliography{document.bib}"))
# core.body_append(appendices("../", "main.py", 10))


print("正在生成pdf")
core.generate_pdf('resources/math', compiler='XeLatex', clean_tex=False)

print("已知问题")
print("换行不能和居中同时使用")

