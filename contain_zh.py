# -*- coding: utf-8 -*-

def is_contain_chinese(check_str):
    check_str = str(check_str)

    for ch in check_str:
        if '0'<=ch<='9' or ch == '.':
            pass
        else:
            return False


def is_contain_dot(check_str):
    check_str = str(check_str)
    for ch in check_str:
        if ch == '.':
            return True
    return False