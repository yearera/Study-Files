01 多维列表
 
创建二维列表 

一个一维的List是线性的List，多维List是一个平面的List：

a = [1,2,3,4,5] # 一行五列

multi_dim_a = [[1,2,3],
			   [2,3,4],
			   [3,4,5]] # 三行三列
索引 

在上面定义的List中进行搜索：

print(a[1])
# 2

print(multi_dim_a[0][1])
# 2
# 用行数和列数来定位list中的值。这里用的是二维的列表，但可以有更多的维度。





02 zip lambda map


全套代码
zip 

zip函数接受任意多个（包括0个和1个）序列作为参数，合并后返回一个tuple列表,请看示例：

a=[1,2,3]
b=[4,5,6]
ab=zip(a,b)
print(list(ab))  #需要加list来可视化这个功能
"""
[(1, 4), (2, 5), (3, 6)]
"""
zip 中的运算

a=[1,2,3]
b=[4,5,6]
ab=zip(a,b)
print(list(ab))
for i,j in zip(a,b):
     print(i/2,j*2)
"""
0.5 8
1.0 10
1.5 12
"""
lambda 

lambda定义一个简单的函数，实现简化代码的功能，看代码会更好理解。

fun = lambda x,y : x+y, 冒号前的x,y为自变量，冒号后x+y为具体运算。

fun= lambda x,y:x+y
x=int(input('x='))    #这里要定义int整数，否则会默认为字符串
y=int(input('y='))
print(fun(x,y))

"""
x=6
y=6
12
"""
map 

map是把函数和参数绑定在一起。

>>> def fun(x,y):
	return (x+y)
>>> list(map(fun,[1],[2]))
"""
[3]
"""
>>> list(map(fun,[1,2],[3,4]))
"""
[4,6]
"""



03 copy & deepcopy 浅复制 & 深复制



全套代码
Python中，对象的赋值，拷贝（深/浅拷贝）之间是有差异的，如果使用的时候不注意，就可能产生意外的结果。

id 

什么是id？一个对象的id值在CPython解释器里就代表它在内存中的`地址

>>> import copy
>>> a=[1,2,3]
>>> b=a
>>> id(a)
"""
4382960392
"""
>>> id(b)
"""
4382960392
"""
>>> id(a)==id(b)    #附值后，两者的id相同，为true。
True
>>> b[0]=222222  #此时，改变b的第一个值，也会导致a值改变。
>>> print(a,b)
[222222, 2, 3] [222222, 2, 3] #a,b值同时改变
浅拷贝 

当使用浅拷贝时，python只是拷贝了最外围的对象本身，内部的元素都只是拷贝了一个引用而已。看代码：

>>> import copy
>>> a=[1,2,3]
>>> c=copy.copy(a)  #拷贝了a的外围对象本身,
>>> id(c)
4383658568
>>> print(id(a)==id(c))  #id 改变 为false
False
>>> c[1]=22222   #此时，我去改变c的第二个值时，a不会被改变。
>>> print(a,c)
[1, 2, 3] [1, 22222, 3] #a值不变,c的第二个值变了，这就是copy和‘==’的不同

深拷贝 

deepcopy对外围和内部元素都进行了拷贝对象本身，而不是对象的引用。

#copy.copy()

>>> a=[1,2,[3,4]]  #第三个值为列表[3,4],即内部元素
>>> d=copy.copy(a) #浅拷贝a中的[3，4]内部元素的引用，非内部元素对象的本身
>>> id(a)==id(d)
False
>>> id(a[2])==id(d[2])
True
>>> a[2][0]=3333  #改变a中内部原属列表中的第一个值
>>> d             #这时d中的列表元素也会被改变
[1, 2, [3333, 4]]


#copy.deepcopy()

>>> e=copy.deepcopy(a) #e为深拷贝了a
>>> a[2][0]=333 #改变a中内部元素列表第一个的值
>>> e
[1, 2, [3333, 4]] #因为时深拷贝，这时e中内部元素[]列表的值不会因为a中的值改变而改变
>>>


04 threading 什么是多线程

全套threading 教程
多线程 

多线程 Threading 是一种让程序拥有分身效果. 能同时处理多件事情. 一般的程序只能从上到下一行行执行代码, 不过 多线程 (Threading) 就能打破这种限制. 让你的程序鲜活起来.



05 multiprocessing 什么是多进程

全套multiprocessing 教程
多进程 

我们在多线程 (Threading) 里提到过, 它是有劣势的, GIL 让它没能更有效率的处理一些分摊的任务. 而现在的电脑大部分配备了多核处理器, 多进程 Multiprocessing 能让电脑更有效率的分配任务给每一个处理器, 这种做法解决了多线程的弊端. 也能很好的提升效率.


06 什么是 tkinter 窗口

全套tkinter教程
窗口视窗 

Tkinter 是使用 python 进行窗口视窗设计的模块. 简单的构造, 多平台, 多系统的兼容性, 能让它成为让你快速入门定制窗口文件的好助手. 它在 python 窗口视窗模块中是一款简单型的. 所以用来入门, 熟悉 窗口视窗的使用, 非常有必要.


07 pickle 保存数据

全套代码
pickle 保存 

pickle 是一个 python 中, 压缩/保存/提取 文件的模块. 最一般的使用方式非常简单. 比如下面就是压缩并保存一个字典的方式. 字典和列表都是能被保存的.

import pickle

a_dict = {'da': 111, 2: [23,1,4], '23': {1:2,'d':'sad'}}

# pickle a variable to a file
file = open('pickle_example.pickle', 'wb')
pickle.dump(a_dict, file)
file.close()
wb 是以写的形式打开 ‘pickle_example.pickle’ 这个文件, 然后 pickle.dump 你要保存的东西去这个打开的 file. 最后关闭 file 你就会发现你的文件目录里多了一个 ‘pickle_example.pickle’ 文件, 这就是那个字典了.

pickle 提取 

提取的时候相对简单点, 同样我们以读的形式打开那个文件, 然后 load 进一个 python 的变量.

# reload a file to a variable
with open('pickle_example.pickle', 'rb') as file:
    a_dict1 =pickle.load(file)

print(a_dict1)



08 set 找不同

学习资料:

全套代码
set 基本 

Set 最主要的功能就是寻找一个句子或者一个 list 当中不同的元素.

char_list = ['a', 'b', 'c', 'c', 'd', 'd', 'd']

sentence = 'Welcome Back to This Tutorial'

print(set(char_list))
# {'b', 'd', 'a', 'c'}

print(set(sentence))
# {'l', 'm', 'a', 'c', 't', 'r', 's', ' ', 'o', 'W', 'T', 'B', 'i', 'e', 'u', 'h', 'k'}

print(set(char_list+ list(sentence)))
# {'l', 'm', 'a', 'c', 't', 'r', 's', ' ', 'd', 'o', 'W', 'T', 'B', 'i', 'e', 'k', 'h', 'u', 'b'}
添加元素 

定义好一个 set 之后我们还可以对其添加需要的元素, 使用 add 就能添加某个元素. 但是不是每一个东西都能添加, 比如一个列表.

unique_char = set(char_list)
unique_char.add('x')
# unique_char.add(['y', 'z']) this is wrong
print(unique_char)

# {'x', 'b', 'd', 'c', 'a'}
清除元素或 set 

清除一个元素可以用 remove 或者 discard, 而清除全部可以用 clear.

unique_char.remove('x')
print(unique_char)
# {'b', 'd', 'c', 'a'}

unique_char.discard('d')
print(unique_char)
# {'b', 'c', 'a'}

unique_char.clear()
print(unique_char)
# set()
筛选操作 

我们还能进行一些筛选操作, 比如对比另一个东西, 看看原来的 set 里有没有和他不同的 (difference). 或者对比另一个东西, 看看 set 里有没有相同的 (intersection).

unique_char = set(char_list)
print(unique_char.difference({'a', 'e', 'i'}))
# {'b', 'd', 'c'}

print(unique_char.intersection({'a', 'e', 'i'}))
# {'a'}




09 正则表达式


学习资料:

本节全部代码
代码的 notebook 形式
网页爬虫教程
正则表达式 (Regular Expression) 又称 RegEx, 是用来匹配字符的一种工具. 在一大串字符中寻找你需要的内容. 它常被用在很多方面, 比如网页爬虫, 文稿整理, 数据筛选等等. 最简单的一个例子, 比如我需要爬取网页中每一页的标题. 而网页中的标题常常是这种形式.

<title>我是标题</ title>
而且每个网页的标题各不相同, 我就能使用正则表达式, 用一种简单的匹配方法, 一次性选取出成千上万网页的标题信息. 正则表达式绝对不是一天就能学会和记住的, 因为表达式里面的内容非常多, 强烈建议, 现在这个阶段, 你只需要了解正则里都有些什么, 不用记住, 等到你真正需要用到它的时候, 再反过头来, 好好琢磨琢磨, 那个时候才是你需要训练自己记住这些表达式的时候.

简单的匹配 

正则表达式无非就是在做这么一回事. 在文字中找到特定的内容, 比如下面的内容. 我们在 “dog runs to cat” 这句话中寻找是否存在 “cat” 或者 “bird”.

# matching string
pattern1 = "cat"
pattern2 = "bird"
string = "dog runs to cat"
print(pattern1 in string)    # True
print(pattern2 in string)    # False
但是正则表达式绝非不止这样简单的匹配, 它还能做更加高级的内容. 要使用正则表达式, 首先需要调用一个 python 的内置模块 re. 然后我们重复上面的步骤, 不过这次使用正则. 可以看出, 如果 re.search() 找到了结果, 它会返回一个 match 的 object. 如果没有匹配到, 它会返回 None. 这个 re.search() 只是 re 中的一个功能, 之后会介绍其它的功能.

import re

# regular expression
pattern1 = "cat"
pattern2 = "bird"
string = "dog runs to cat"
print(re.search(pattern1, string))  # <_sre.SRE_Match object; span=(12, 15), match='cat'>
print(re.search(pattern2, string))  # None

灵活匹配 

除了上面的简单匹配, 下面的内容才是正则的核心内容, 使用特殊的 pattern 来灵活匹配需要找的文字.

如果需要找到潜在的多个可能性文字, 我们可以使用 [] 将可能的字符囊括进来. 比如 [ab] 就说明我想要找的字符可以是 a 也可以是 b. 这里我们还需要注意的是, 建立一个正则的规则, 我们在 pattern 的 “” 前面需要加上一个 r 用来表示这是正则表达式, 而不是普通字符串. 通过下面这种形式, 如果字符串中出现 “run” 或者是 “ran”, 它都能找到.

# multiple patterns ("run" or "ran")
ptn = r"r[au]n"       # start with "r" means raw string
print(re.search(ptn, "dog runs to cat"))    # <_sre.SRE_Match object; span=(4, 7), match='run'>
同样, 中括号 [] 中还可以是以下这些或者是这些的组合. 比如 [A-Z] 表示的就是所有大写的英文字母. [0-9a-z] 表示可以是数字也可以是任何小写字母.

print(re.search(r"r[A-Z]n", "dog runs to cat"))     # None
print(re.search(r"r[a-z]n", "dog runs to cat"))     # <_sre.SRE_Match object; span=(4, 7), match='run'>
print(re.search(r"r[0-9]n", "dog r2ns to cat"))     # <_sre.SRE_Match object; span=(4, 7), match='r2n'>
print(re.search(r"r[0-9a-z]n", "dog runs to cat"))  # <_sre.SRE_Match object; span=(4, 7), match='run'>

按类型匹配 

除了自己定义规则, 还有很多匹配的规则时提前就给你定义好了的. 下面有一些特殊的匹配类型给大家先总结一下, 然后再上一些例子.

\d : 任何数字
\D : 不是数字
\s : 任何 white space, 如 [\t\n\r\f\v]
\S : 不是 white space
\w : 任何大小写字母, 数字和 “” [a-zA-Z0-9]
\W : 不是 \w
\b : 空白字符 (只在某个字的开头或结尾)
\B : 空白字符 (不在某个字的开头或结尾)
\\ : 匹配 \
. : 匹配任何字符 (除了 \n)
^ : 匹配开头
$ : 匹配结尾
? : 前面的字符可有可无
下面就是具体的举例说明啦.

# \d : decimal digit
print(re.search(r"r\dn", "run r4n"))           # <_sre.SRE_Match object; span=(4, 7), match='r4n'>
# \D : any non-decimal digit
print(re.search(r"r\Dn", "run r4n"))           # <_sre.SRE_Match object; span=(0, 3), match='run'>
# \s : any white space [\t\n\r\f\v]
print(re.search(r"r\sn", "r\nn r4n"))          # <_sre.SRE_Match object; span=(0, 3), match='r\nn'>
# \S : opposite to \s, any non-white space
print(re.search(r"r\Sn", "r\nn r4n"))          # <_sre.SRE_Match object; span=(4, 7), match='r4n'>
# \w : [a-zA-Z0-9_]
print(re.search(r"r\wn", "r\nn r4n"))          # <_sre.SRE_Match object; span=(4, 7), match='r4n'>
# \W : opposite to \w
print(re.search(r"r\Wn", "r\nn r4n"))          # <_sre.SRE_Match object; span=(0, 3), match='r\nn'>
# \b : empty string (only at the start or end of the word)
print(re.search(r"\bruns\b", "dog runs to cat"))    # <_sre.SRE_Match object; span=(4, 8), match='runs'>
# \B : empty string (but not at the start or end of a word)
print(re.search(r"\B runs \B", "dog   runs  to cat"))  # <_sre.SRE_Match object; span=(8, 14), match=' runs '>
# \\ : match \
print(re.search(r"runs\\", "runs\ to me"))     # <_sre.SRE_Match object; span=(0, 5), match='runs\\'>
# . : match anything (except \n)
print(re.search(r"r.n", "r[ns to me"))         # <_sre.SRE_Match object; span=(0, 3), match='r[n'>
# ^ : match line beginning
print(re.search(r"^dog", "dog runs to cat"))   # <_sre.SRE_Match object; span=(0, 3), match='dog'>
# $ : match line ending
print(re.search(r"cat$", "dog runs to cat"))   # <_sre.SRE_Match object; span=(12, 15), match='cat'>
# ? : may or may not occur
print(re.search(r"Mon(day)?", "Monday"))       # <_sre.SRE_Match object; span=(0, 6), match='Monday'>
print(re.search(r"Mon(day)?", "Mon"))          # <_sre.SRE_Match object; span=(0, 3), match='Mon'>
如果一个字符串有很多行, 我们想使用 ^ 形式来匹配行开头的字符, 如果用通常的形式是不成功的. 比如下面的 “I” 出现在第二行开头, 但是使用 r"^I" 却匹配不到第二行, 这时候, 我们要使用 另外一个参数, 让 re.search() 可以对每一行单独处理. 这个参数就是 flags=re.M, 或者这样写也行 flags=re.MULTILINE.

string = """
dog runs to cat.
I run to dog.
"""
print(re.search(r"^I", string))                 # None
print(re.search(r"^I", string, flags=re.M))     # <_sre.SRE_Match object; span=(18, 19), match='I'>
重复匹配 

如果我们想让某个规律被重复使用, 在正则里面也是可以实现的, 而且实现的方式还有很多. 具体可以分为这三种:

* : 重复零次或多次
+ : 重复一次或多次
{n, m} : 重复 n 至 m 次
{n} : 重复 n 次
举例如下:

# * : occur 0 or more times
print(re.search(r"ab*", "a"))             # <_sre.SRE_Match object; span=(0, 1), match='a'>
print(re.search(r"ab*", "abbbbb"))        # <_sre.SRE_Match object; span=(0, 6), match='abbbbb'>

# + : occur 1 or more times
print(re.search(r"ab+", "a"))             # None
print(re.search(r"ab+", "abbbbb"))        # <_sre.SRE_Match object; span=(0, 6), match='abbbbb'>

# {n, m} : occur n to m times
print(re.search(r"ab{2,10}", "a"))        # None
print(re.search(r"ab{2,10}", "abbbbb"))   # <_sre.SRE_Match object; span=(0, 6), match='abbbbb'>
分组 

我们甚至可以为找到的内容分组, 使用 () 能轻松实现这件事. 通过分组, 我们能轻松定位所找到的内容. 比如在这个 (\d+) 组里, 需要找到的是一些数字, 在 (.+) 这个组里, 我们会找到 “Date: “ 后面的所有内容. 当使用 match.group() 时, 他会返回所有组里的内容, 而如果给 .group(2) 里加一个数, 它就能定位你需要返回哪个组里的信息.

match = re.search(r"(\d+), Date: (.+)", "ID: 021523, Date: Feb/12/2017")
print(match.group())                   # 021523, Date: Feb/12/2017
print(match.group(1))                  # 021523
print(match.group(2))                  # Date: Feb/12/2017
有时候, 组会很多, 光用数字可能比较难找到自己想要的组, 这时候, 如果有一个名字当做索引, 会是一件很容易的事. 我们字需要在括号的开头写上这样的形式 ?P<名字> 就给这个组定义了一个名字. 然后就能用这个名字找到这个组的内容.

match = re.search(r"(?P<id>\d+), Date: (?P<date>.+)", "ID: 021523, Date: Feb/12/2017")
print(match.group('id'))                # 021523
print(match.group('date'))              # Date: Feb/12/2017


findall 

前面我们说的都是只找到了最开始匹配上的一项而已, 如果需要找到全部的匹配项, 我们可以使用 findall 功能. 然后返回一个列表. 注意下面还有一个新的知识点, | 是 or 的意思, 要不是前者要不是后者.

# findall
print(re.findall(r"r[ua]n", "run ran ren"))    # ['run', 'ran']

# | : or
print(re.findall(r"(run|ran)", "run ran ren")) # ['run', 'ran']
replace 

我们还能通过正则表达式匹配上一些形式的字符串然后再替代掉这些字符串. 使用这种匹配 re.sub(), 将会比 python 自带的 string.replace() 要灵活多变.

print(re.sub(r"r[au]ns", "catches", "dog runs to cat"))     # dog catches to cat
split 

再来我们 Python 中有个字符串的分割功能, 比如想获取一句话中所有的单词. 比如 "a is b".split(" "), 这样它就会产生一个列表来保存所有单词. 但是在正则中, 这种普通的分割也可以做的淋漓精致.

print(re.split(r"[,;\.]", "a;b,c.d;e"))             # ['a', 'b', 'c', 'd', 'e']
compile 

最后, 我们还能使用 compile 过后的正则, 来对这个正则重复使用. 先将正则 compile 进一个变量, 比如 compiled_re, 然后直接使用这个 compiled_re 来搜索.

compiled_re = re.compile(r"r[ua]n")
print(compiled_re.search("dog ran to cat"))  # <_sre.SRE_Match object; span=(4, 7), match='ran'>
小抄 

为了大家方便记忆, 我很久以前在网上找到了一份小抄, 这个小抄的原出处应该是这里. 小抄很有用, 不记得的时候回头方便看.

