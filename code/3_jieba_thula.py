# 计算jieba和thula的P，R，F值。基于文本‘express.txt’，标准文本是人工切分。
import jieba
import re
import thulac
 
def P_R_F(n, c, e):
    R = round(c / n, 4)
    P = round(c / (c + e), 4)
    F = round(2*P*R / (P + R), 4)
    print("精度P为：", P * 100, '%')
    print("召回率R为：", R * 100, '%')
    print("F值为：", F * 100, '%')
    return P, R, F
 
f = str(open("express.txt").readlines())
print(f)
 

#标准文本
fp = open('express_cut.txt','w')
ls = ["近些年来","快递","行业","发生","了","巨大","转变","各类","机器人","正","试图","夺走","快递小哥","的","工作","。","继","多家","公司","试验","无人机","送货","后","，","地面送货机器人","也","开始","上路","了","。","本月","月初","，","弗吉尼亚州","通过","法案","，","允许","地面送货机器人","上路","，","今天","爱达荷州","（","位于","美国","西北部","）","则","成","了","第二个","批准","送货","机器人", "上路","的","州","，","不过","这项","法案","今年","7", "月", "1", "日","才","会","正式","生效","。"]
for i in ls:
    fp.write(i+"\n")
fp.close()
raw = open('express_cut.txt').readlines()

d=[re.split(r' |\n',w)[0] for w in raw]
dict = []
for w in d:
    if w == r'，' or w == r'。' or w == r'（'or w == r'）':
        pass
    else:
        dict.append(w)
print('*************标准分词文本*************')
print(dict)
n = len(dict)
 
#结巴
s1 = list(jieba.cut(f))
s_jieba = []
for w in s1:
    if w == r'，' or w == r'。' or w == r'（'or w == r'）'or w == r'['or w == r']'or w == r"'":
        pass
    else:
        s_jieba.append(w)
#print(s_jieba)
e_jieba = 0
c_jieba = 0
for i in range(len(s_jieba)):
    if s_jieba[i] in dict:
        c_jieba += 1
    else:
        e_jieba += 1
 
print('*************结巴分词结果*************')
print(s_jieba)
print('c:',c_jieba)
print('e:',e_jieba)
print('n:',n)
P_R_F(n, c_jieba, e_jieba)
 
#清华
thu1 = thulac.thulac(seg_only=True)
s_2 = thu1.cut(f, text=True)
s2 = []
print(s_2)
s_qinghua = []
a=0
for i in range(len(s_2)):
    if s_2[i] == ' ':
        s2.append(s_2[a:i])
        a = i+1
    else:
        continue
for w in s2:
    if w == r'，' or w == r'。' or w == r'（'or w == r'）'or w == r'['or w == r']'or w == r"'":
        pass
    else:
        s_qinghua.append(w)
#print(s_qinghua)
 
e_qinghua = 0
c_qinghua = 0
for i in range(len(s_qinghua)):
    if s_qinghua[i] in dict:
        c_qinghua += 1
    else:
        e_qinghua += 1
 
print('*************清华分词结果*************')
print(s_qinghua)
print('c:',c_qinghua)
print('e:',e_qinghua)
print('n:',n)
P_R_F(n, c_qinghua, e_qinghua)