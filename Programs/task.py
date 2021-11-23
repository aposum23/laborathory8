#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    tpl = tuple(input('tpl = ').split())

    i = 1
    flag = False

    while i < len(tpl) - 1:
        if int(tpl[i]) > int(tpl[i - 1]) \
                and int(tpl[i]) > int(tpl[i + 1]):
            flag = True
            print(f'ind1 = {i - 1}, ind2 = {i}, ind3 = {i + 1}')
            break
        i += 1

    if not flag:
        print('Таких троек нет')
