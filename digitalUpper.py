# -*- coding: utf-8 -*-
from contain_zh import is_contain_dot


def digital_to_Upper(moneystr):

    nums = {0: '零', 1: '壹', 2: '贰', 3: '叁', 4: '肆', 5: '伍', 6: '陆', 7: '柒', 8: '捌', 9: '玖'}
    decimal_label = ['角', '分']
    small_int_label = {0: '', 1: '拾', 2: '佰', 3: '仟', 4: '万', 5: '拾', 6: '佰', 7: '仟', 8: '亿'}
    decimal_part = ''
    integer_part_list = []
    integer_part = ''
    if is_contain_dot(moneystr) is True:
        integer, decimal = str(moneystr).split('.', 1)
        if len(decimal)>2:
            # print('小数部分超出')
            return ('小数部分超出范围')
        elif len(integer)>9:
            return ('还没见过这么多钱')
        # 处理小数部分，只处理到百分位
        for i, j in enumerate(decimal):
            """
            i: 记录循环次数
            """
            if j == '0' and decimal[-1] != '0':
                decimal_part += nums[int(j)]
            elif j == '0' and decimal[-1] == '0':
                pass
            else:
                decimal_part += (nums[int(j)] + decimal_label[i])
    else:
        integer = str(moneystr)
        if len(integer)>9:
            return ('还没见过这么多钱')

    # 处理整数部分,到亿
    if integer != '' and int(integer) != 0:
        integer_part_list.insert(0, '元')
    for n, m in enumerate(integer[::-1]):

        if n == 0 and m == '0':
            pass
        else:
            if m=='0' and n==4 and int(integer) != 0:
                integer_part_list.insert(0, '万')

            elif m=='0' and integer[::-1][n-1] != '0':
                integer_part_list.insert(0, (nums[int(m)]))

            elif m == '0' and integer[::-1][n-1] == '0':
                pass
            else:
                integer_part_list.insert(0, (nums[int(m)] + small_int_label[n]))
    integer_part = ''.join(integer_part_list)
    return (integer_part+decimal_part)




