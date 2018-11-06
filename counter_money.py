#coding=utf-8
"""
@athor:weifeng.guo 
@data:2018/9/11 11:50
@filename:counter_money
"""

print("奶茶馆售卖宇宙无敌奶茶，奶茶虽好，可不要贪杯哦！")
print("每次限尝鲜一种口味:\n1）原味冰奶茶\n2）香蕉冰奶茶\n3) 草莓冰奶茶\n4）蒟蒻冰奶茶\n5）珍珠冰奶茶\n")
name_tea = {'1': '原味冰奶茶', '2': '香蕉冰奶茶', '3': '草莓冰奶茶', '4': '蒟蒻冰奶茶', '5': '珍珠冰奶茶'}
price_tea = {'1': 3, '2': 5, '3': 5, '4': 7, '5': 7}
choice_number = ['否', '是']
choice_tea = raw_input("请输入要购买奶茶的序号：")
num = int(raw_input("要购买的数量："))
number = int(raw_input("是否时会员，1-是，0-否："))
if int(choice_tea) < 5:
    print('你选择的奶茶口味是：{}，购买的数量是：{}，是否会员：{}请确认'.format(name_tea[choice_tea], num, choice_number[number]))
else:
    print("Woops! 我们只售卖以上五种奶茶哦！新口味敬请期待")
if int(number) == 1:
    print('您购买的奶茶是：{},\n单价是：{},\n数量是：{},\n总额是：{}.'.format(name_tea[choice_tea], price_tea[choice_tea], num, num*price_tea[choice_tea]))
else:
    print('您购买的奶茶是：{},\n单价是：{},\n数量是：{},\n总额是：{}.'.format(name_tea[choice_tea], price_tea[choice_tea], num, 0.9*num * price_tea[choice_tea]))



