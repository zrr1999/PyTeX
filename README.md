# PyTex

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

本代码库借鉴和使用了部分JelteF的[PyLaTex](https://github.com/JelteF/PyLaTeX) 代码。

PyTex用于简化Tex的编写，熟练使用本库需要对Python语法基本了解。
本库适合对LaTex基本语法已经掌握的同学和不会使用LaTex却需要使用LaTex的同学。

## 背景

某天突发奇想要做个LaTex的辅助编写工具，于是就开始了。

## 优势
- LaTex
    1. 本辅助库可以有效避免拼写错误，漏加空格等低级错误。
    2. 本辅助库可以借助Python提供更多的功能。
    3. 本辅助库在插入图片、生成表格等方面有巨大优势。
- Word
    1. 本辅助库可以更加自由地编写文档。
    2. 本辅助库可以借助Python提供更多的功能。

## 安装[![Downloads](https://pepy.tech/badge/bone-pytex)](https://pepy.tech/project/bone-pytex)

这个项目使用 [Python](http://nodejs.org) 开发，请确保你本地安装了它。建议使用pip安装。

```sh
$ pip install bone-pytex
```

## 使用说明

使用时，你必须创建一个文档实例。

```python
from pytex import MathDocument
doc = MathDocument('数学建模', packages=["amsmath", "graphicx", "amssymb", "cite"],
                   standard="GJS", preface=False)
```

你可以将md转换为latex

```python
from pytex.utils import md2tex
latex_code = md2tex("md/abstract.md")
```

你可以在文档中添加标题、摘要、目录。

```python
doc.add_title()
doc.add_abstract(latex_code, 
                 ["出租车资源配置", "供求匹配模型", "缓解程度判断模型", "分区域动态实时补贴方案"])
doc.add_toc()
```

你可以在文档中添加 使用固定格式编写的md文档 作为一个section。

```python
doc.add_section(path="md/wtcs.md")
```

你可以在文档中添加指定标题和内容的 section。

```python
doc.add_section(title="符号说明", content="大家好啊")
```

你可以在文档中添加变量，将会自动添加到变量表中，同时还可以使用符号转化器将其转换为latex代码

```python
from pytex.utils import SymbolTransformer
x = doc.add_var("x", NoEscape("这是一个优秀的$x$"))
st = SymbolTransformer()
formula, name = st.sym2tex((x**2+7)*5)
```

## 示例

可以参考demo结尾的几个文件。

## 特色功能
1. 提供了试卷编写模块，详情见pytex/exam/README.md。<br/>
2. 支持定义局部操作（由于功能定位不清楚暂时废弃）。例如:
> 在经常用到导数和积分的局部区域
> 将`\text{d}`定义为`\d`，而在其他区域
> 将`\dot`定义为`\d`，注意定义命令符时应尽量避免歧义，
> 例如若将`\text{d}`定义为`d`，则`ad`也会被错误识别。
3. 支持部分Markdown语法转LaTex。
4. 伪代码编写。
5. 针对数模进行了大幅度优化，提供了高教社标准和西电标准（非官方）。

## 计划实现功能
1. 神经网络结构可视化，输入处理形状变换可视化。
2. 更好地和symbol交互。
3. Python端编辑公式。
3. Python端添加文献。
4. 图制作。

## 更新日志
- (2020.04. ) v0.1.4 发布
    - 完善了markdown到latex的转换功能。
- (2020.04.17) v0.1.3 发布
    - 大幅度优化了数模模块。
    - 优化了结构。
    - 支持添加sympy变量。
- (2020.04.15) v0.1.2 发布
    - 增加了数模模块。
    - 调整了结构。
- (2020.04.11) v0.1.1 发布
    - 修复了部分问题。
- (2020.04.08) v0.1.0 发布
    - 实现了DocTree，用于将dict转化为文档结构。

## 维护者

[@詹荣瑞](https://github.com/tczrr1999)、
[@WilsonLuo19](https://github.com/WilsonLuo19)。

## 如何贡献

非常欢迎你的加入！[提一个 Issue](https://github.com/tczrr1999/pytex/issues/new) 或者提交一个 Pull Request。

### 贡献者

感谢以下参与项目的人：


## 使用许可

[GNU](LICENSE) © Rongrui Zhan