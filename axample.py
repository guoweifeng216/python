#!/usr/bin/env python
# coding=utf-8
"""
author:     weifeng.guo 
data:       2019/10/23 11:09
filename:   axample
"""
import random
a=[1, 2, 3, 4, 5]
random.shuffle(a)
print(a)
# print(a.sort())
b =[]
# for item in a:
#     b.append(item)
# b.sort
b = sorted(a)
print(b)
print(dict(zip(a,b)))
# print(a[:2])
# print(a[-4:-2])
print(sum([x+3 for x in a]))
# print(sum(list(filter(lambda x: x%2==0 x in a))))
print('pyothon'.find('o'))
print('python'.count('o'))
# num = eval(input("enter num"))
# print(1 + num)
print('{} is {}'.format('python', 'easy'))
# from functools import wraps
#
#
# def  logit(func):
#     @wraps(func)
#     def with_logging(*args, **kwargs):
#         print(func.__name__ + " was called")
#         return func(*args, **kwargs)
#
#     return with_logging
#
#
# @logit
# def addition_func(x):
#     """Do some math."""
#     return x + x
#
#
# result = addition_func(4)
# print(result)
# import string
# print(''.join((random.choice(string.printable)) for i in range(16)))
# info = {'name': 'Gage', 'age': 25, 'sex': 'man'}
# print(sorted(info.items(), key=lambda x: x[0]))
# a=b"hello"
# b="你好".encode()
# print(a,b)
# print(type(a),type(b))
# i =0
# while i < 9:
#     i += 1
#     j = 0
#     while j < i:
#         j += 1
#         print("{}*{}".format(j,i),end=" ")
#     print()
# from time import *
# begin = time()
# k = 2
# while k < 1000000:
#     flag = True
#     h = 2
#     while h <= k ** 0.5:
#         if k % h == 0:
#             flag = False
#             break
#         h += 1
#     if flag:
#         pass
#         # print(k)
#     k += 1
#
# end = time()
# print("运行时间",end - begin,"秒")
# print('-'*20, '欢迎光临《孙悟空大战白骨精》', '-'*20)
# print('请选择你的身份： ')
# print('\t1.孙悟空')
# print('\t2.白骨精')
# player_rolse = input('请选择[1-2]: ')
# print('-'*60)
# if player_rolse == '1':
#     print('你选择了1，你将以->孙悟空<-的身份来进行游戏！')
# elif player_rolse == '2':
#     print('你竟然选择了白骨精，太不要脸了，你将以->孙悟空<-的身份来进行游戏！')
# else:
#     print('你的输入有误，系统将自动分配身份，你将以->孙悟空<-的身份来进行游戏！')
#
# # 创建变量，来保存玩家的生命值和攻击力
# player_life = 2 # 生命值
# player_attack = 2 # 攻击力
#
# # 创建一个变量，保存boss的生命值和攻击力
# boss_life = 10
# boss_attack = 10
#
# print('-'*66)
# # 显示玩家的信息（攻击力、生命值）
# print(f'孙悟空，你的生命值是 {player_life} , 你的攻击力是 {player_attack}')
# while True:
#     print('-' * 66)
#     print('请选择你要进行的操作：')
#     print('\t1.练级')
#     print('\t2.打BOSS')
#     print('\t3.逃跑')
#     game_choose = input('请选择要做的操作[1-3]：')
#     if game_choose == '1':
#         # 增加玩家的生命值和攻击力
#         player_life += 2
#         player_attack += 2
#         # 显示最新的信息
#         # 打印一条分割线
#         print('-' * 66)
#         # 显示玩家的信息（攻击力、生命值）
#         print(f'恭喜你升级了！，你现在的生命值是 {player_life} , 你的攻击力是 {player_attack}')
#     elif game_choose == '2':
#         # 玩家攻击boss
#         # 减去boss的生命值，减去的生命值应该等于玩家的攻击力
#         boss_life -= player_attack
#         print('-' * 66)
#         print('->孙悟空<- 攻击了 ->白骨精<-')
#         # 检查boss是否死亡
#         if boss_life <= 0:
#             # boss死亡，player胜利，游戏结束
#             print(f'->白骨精<-受到了 {player_attack} 点伤害，重伤不治死了，->孙悟空<-赢得了胜利！')
#             # 游戏结束
#             break
#             # boss要反击玩家
#             # 减去玩家的生命值
#         player_life -= boss_attack
#         print(' ->白骨精<- 攻击了 ->孙悟空<-')
#         # 检查玩家是否死亡
#         if player_life <= 0:
#             # 玩家死亡
#             print(f'你受到了 {boss_attack} 点伤害，重伤不治死了！GAME OVER')
#             # 游戏结束
#             break
#     elif game_choose == '3':
#         print('-' * 66)
#         # 逃跑，退出游戏
#         print('->孙悟空<-一扭头，撒腿就跑！GAME OVER')
#         break
#     else:
#         # 打印一条分割线
#         print('-' * 66)
#         print('你的输入有误，请重新输入！')
# import re
# str1 = "Python's features"
# str2 = re.match( r'(.*)on(.*?) .*', str1, re.M|re.I)
# print(str2.group(1))
# print(str2.group(2))
# def w1():
#    print('正在装饰')
#    def inner():
#         print('正在验证权限')
#    return inner()
# w1()
# n = int(raw_input())
# num_list = []
# for i in range(n):
#     num = raw_input()
#     num_list.append(num)
# print(num_list)
# n1 = input('请输入用户名：')
# n2 = input('请输入密码：')
# print(n1)
# print(n2)
# list1 = ['Google', 'Runoob', 'Taobao']
# list_pop=list1.pop()
# print("删除的项为 :", list_pop)
# print("列表现在为 : ", list1)
def match_long_string(s):
    s_lenth = len(s)
    start = 0
    long_string = 0
    list_count = []
    for i in range(s_lenth):
        if s[i] == '(':
            list_count.append(i)
        else:
            if list_count == []:
                long_string = max(long_string, i -start)
                start = i + 1
            else:
                q = list_count.pop()
                if list_count == []:
                    long_string = max(long_string, i - start +1)
                else:
                    long_string = max(long_string, i - list_count[-1])

    return long_string
string_input = input()
print(match_long_string(string_input))