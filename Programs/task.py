#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    tpl = tuple(input('tpl = ').split())

    flag = False

    for idx, value in enumerate(tpl[1:-1], 1):
        if int(value) > int(tpl[idx - 1]) \
                and int(value) > int(tpl[idx + 1]):
            flag = True
            print(f'ind1 = {idx - 1}, ind2 = {idx}, ind3 = {idx + 1}')
            break

    if not flag:
        print('Таких троек нет')
