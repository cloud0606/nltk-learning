#  匹配以下特征的词
# • th前有一个字符
# • th前有一个或者0个字符
# • 单词中含有th的
# • 以数字开始的字符串
# • 含有非数字和字母的词
# • 文本中经常有<>括起来的特定内容，能找到所有这样的字符串么？
# • 在格式文本中一行中的：以后的部分是内容，：前是题名，能分开它们么？
import re

# th前有一个字符
m = re.match("^.th$","ath")
print(m.group())
# th前有一个或者0个字符
m = re.match("^[a-z]?th$","ath")
print(m.group())
m = re.match("^[a-z]?th$","th")
print(m.group())
# 单词中含有th的
m = re.match("^[a-zA-Z]*th[a-zA-Z]*$","hithey")
print(m.group())
# 以数字开始的字符串
m = re.match("^(\d)*(.)*$","123123hello")
print(m.group())
# 含有非数字和字母的词
m = re.match("^(\w|.)*$","123<<sdf>sd?a1")
print(m.group())
# 有<>括起来的特定内容
m = re.match("^(.)*<(.)*>(.)*$", "get <hello ?!> hi")
print(m.group())
# 分开使用 ：分隔的内容
m = re.match(r"(.)*:", "tomorrow:is another day!")
print(m.group())

