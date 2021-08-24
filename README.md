# AIreader简介
原计划是写一个修仙小说自动生成项目，后来发现AI的功能似乎和我所想有些脱轨，于是不了了之。
当时实现的功能是：
1.随机生成一个包含角色文字具体详细具体信息数据库
2.根据这些角色的详细信息生成对话及描述
3.将游戏过程的内容记录保存到doc文件内
4.文字转语音（非百度ai接口）

上传部分代码，基本每个函数都做了详细的注释。
有需要的人可以改写部分函数。

---
# 作者自述
本人是个标准的INTJ物理满分选手，
电气工程及其自动化转行程序员，原本是在闲暇的时候做的。
因为看上了AI所以搁置了。

原本就是做个小东西，
有感兴趣的人可以一起来做一个大游戏。
数据库的部分用py文件生成而非mysql文件，为的是方便非程序员玩家能够快速上手使用。
毕竟学习成本太高又很贵的小众游戏基本没有生存空间...
和主代码是分开的，为的是方便迁移到云上或数据库上。

当然说是游戏其实也就是个半成品。
感兴趣的同学请联系我。

---
# 构架简述

每个py文件及函数都有自己的功能概述及输入输出描述
部分代码会被放进一个加密的zip里，所以这个项目并不能跑起来。

具体架构如下：
1.main.py
  主程序入口。
  包含部分的游戏流程
  大致为：
  a.游戏开始环节。
  1.生成一个主玩家角色，并规定角色的部分特征。
  2.生成一个完全随机的角色库，角色库的种族等比例由数据库规定。
  3.生成一个半随机的角色库，玩家可以规定一部分内容，其他内容由数据库决定。
  
  b.游戏内容。（test）
  1.玩家在大街上看到一个系统生成的人，根据人的特征随机产生玩家的感受及对人的描述，以及玩家对他说的一句话。
  
  c.游戏结束时的收尾工作
  1.将生成的文字内容保存在目录下的doc文件中
  2.根据doc文件生成mp3和wav两种格式的语音文件。
  
2.help_tools.py
  生成数据库的小工具。
  以及测试部分代码用的小工具。
  运行时注意先把main函数的入口注释掉，否则可能会卡死。
  
3.count_tools.py
  生成的数据读取之后会变成一个字典文件，count_tools会读取这个字典文件并计算每个类目出现的参数的个数。
  （比如记录种族，有多少神，多少平民，多少精灵）
  假如一个类目的种类超过50，会默认是名字（姓氏会统计，但是名字太多了统计了也没意义）然后放弃统计。

4.data_base.py（缺失）
  如前所述，未来会做成mysql接口的形式的数据库文件。
  有一些小工具，来处理数据整合的时候遇到的小问题。
  
5.NLP_discribing.py（缺失）
  虽然叫NLP但没什么关系
  和4类似，根据资料库的信息调用生成的语料库。

6.NLP_eng.py
  输入关键信息和语料
  输出句子的引擎。
  为什么不放在5里，其实我自己也很疑惑。

7.random_name.py
  生成人物及其对应文字描述属性。
  未来的计划是不只是人物。
 
8.random_values.py
  根据人物属性对其进行赋值。
  未来的计划是不只是人物。

9.use_to_wave（缺失），read_docx
  前者是一个独立的语音合成软件，调用了里面的接口生成mp3，我自己生成的是wav
  一个大小更小，另一个方便和音乐音效等合成。可以自己取舍。
  因为前者的代码不是我码的所以就不放上来了。
  
10.save_dict.py
  方便字典文件存取的小应用，将字典程序存为excel格式，取出来时不会破坏它的结构。
