## Calculate wieght loss during a triathlon.
# cycling = float(input("Enter number of hours cycling: "))
# running = float(input("Enter number of hours running: "))
# swimming = float(input("Enter number of hours swimming: "))
# pounds = (200 * cycling + 475 * running + 275 * swimming) / 3500
# pounds =round(pounds, 1)
# print("Weight loss:", pounds, "pounds")

# i =0
# n = int(input())
# num_list = []
# for i in range(n):
#     num = input()
#     num_list.append(num)
# for i in list(sorted(set(num_list))):
#     print(i)
# num = int(input())
# num_b = bin(num)
# print(str(num_b).count('1'))
# num = input()
# print(num[::-1])

# str_input = input()
# temp_list = list(set(list(str_input)))
# count=0
# for letter in temp_list:
#     if ord(letter) > 0 and ord(letter) < 128:
#         count += 1
# print(count)
# num = input()
# list_temp = []
# for i in list(num)[::-1]:
#     if i not in list_temp:
#         list_temp.append(i)
#     else:
#         continue
# print(''.join(list_temp))
# num = int(input())
# i = 0
# dict_value = {}
# while i < num:
#     key_value, dic_value=map(int, input().split(" "))
#     print(key_value, dic_value)
#     if key_value in dict_value.keys():
#         dict_value[key_value] = dict_value[key_value] + dic_value
#     else:
#         dict_value[key_value] = dic_value
#     i += 1
# for key, value in dict_value.items():
#     print(key,value)

# urivthvtlqqerctlxmjvkgvfclaaduwmaadedpadanl
# batkqdhjnrwtsmzidswdnenqpsblsszldyttytrgenaizwehntqiaaufble
# def str_list(str):
#     list_s = []
#     if len(str) > 8:
#         i = 0
#         while i < len(str):
#             list_s.append(str[i:i + 8])
#             i += 8
#     else:
#         list_s.append(str)
#
#     return list_s
# s1 = input()
# s2 = input()
# list_s = []
# list_s1 = str_list(s1)
# list_s2 = str_list(s2)
# list_temp = list_s1 + list_s2
# print(list_temp)
# for i in list_temp:
#     print(i.ljust(8, '0'))
# def str_list(str1):
#     list_s = []
#     if len(str1) > 8:
#         i = 0
#         while i < len(str1):
#             list_s.append(str1[i:i + 8])
#             i += 8
#     else:
#         list_s.append(str1)
#
#     return list_s
#
# num = int(input())
# i = 0
# list_total = []
# while i < num:
#     str_input = input()
#     list_total += str_list(str_input.strip())
#     i +=1
# print(list_total)
# for i in list_total:
#     print(i.ljust(8, '0'))
# import re
# str_input = input()
# p=re.compile(r'[-,$()#+&*!]')
# print(re.sub(p,' ',str_input))
# print(' '.join(re.sub(p,' ',str_input).strip().split(' ')[::-1]))
def digital_to_chinese(digital):
    str_digital = str(digital)
    chinese = {'1': '壹', '2': '贰', '3': '叁', '4': '肆', '5': '伍', '6': '陆', '7': '柒', '8': '捌', '9': '玖', '0': '零'}
    chinese2 = ['拾', '佰', '仟', '万', '厘', '分', '角']
    jiao = ''
    bs = str_digital.split('.')
    print(bs)
    yuan = bs[0]
    if len(bs) > 1:
        jiao = bs[1]
    r_yuan = [i for i in reversed(yuan)]
    print(r_yuan)
    count = 0
    for i in range(len(yuan)):
        if i == 0:
            r_yuan[i] += '圆'
            continue
        r_yuan[i] += chinese2[count]
        count += 1
        if count == 4:
            count = 0
            chinese2[3] = '亿'
        print(r_yuan)
    s_jiao = [i for i in jiao][:3]  # 去掉小于厘之后的

    j_count = -1
    for i in range(len(s_jiao)):
        s_jiao[i] += chinese2[j_count]
        j_count -= 1
    last = [i for i in reversed(r_yuan)] + s_jiao
    print(last)
    last_str = ''.join(last)
    print(str_digital)
    print(last_str)
    for i in range(len(last_str)):
        digital = last_str[i]
        if digital in chinese:
            last_str = last_str.replace(digital, chinese[digital])
    print('人民币'+last_str)
    return last_str


if __name__ == '__main__':
    digital_to_chinese(10200406789.456)