示例代码在exam_demo.py
## **操作指南**
示例代码在exam_demo.py
### **基本操作指南**
1. **创建Problem对象**<br/>
创建Problem对象需要提供core，name，describe，score参数，
其中core直接使用预设的core即可，name，describe，score
根据实际情况确定，例如<br/>
**Problem(core, "选择题", "...", 5)**<br/>
即表示这是一道选择题，每小题5分。注意，若score是列表，则代表
不同小题有不同的分数，以列表的形式给出。
2. **调用Problem对象的set方法**<br/>
调用set方法可以输入任意数量的参数，每个参数代表一道题
(暂时仅支持使用latex代码)，为了
不引起歧义，建议此处参数数量与创建时输入的分数列表数量相等
（如果不是列表，会自动计算）。
如果未能成功生成pdf，可以打开latex文档寻找bug。
3. **运行文件main.py**<br/>
运行文件main.py即可生成latex文档和pdf文档
（经验证可通过XeLaTex编译，未验证其他编译器）。
如果未能成功生成pdf，可以打开latex文档寻找bug。

### **选择题创建指南**
推荐直接调用choice函数
1. 按顺序输入题目描述、各选项描述作为函数的参数。
2. 可以单独指定options参数作为选择题附加选项。
3. 例如：<br/>
co = choice("这是用选择题模板编写的", "A", "B", "C", "D", "E", "F",
            options=NoEscape(r"counter-format=(tsk[A]),label-width=4ex"))  # options为默认参数
## 第五版更新内容
1、简化了部分操作（自定义latex操作、添加包等）。<br/>

## 第四版更新内容
1、增加了题目内容。<br/>

## 第三版更新内容
1、细节优化。<br/>
2、支持在Python端创建选择题。<br/>

## 第二版更新内容
1、调整了程序结构，使结构更加清晰。<br/>
2、完善了自动题目分数计算。<br/>
3、简化了pylatex库利用Numpy的部分操作。<br/>
4、优化封面。<br/>
5、对matplotlib的利用进行了测试。<br/>
