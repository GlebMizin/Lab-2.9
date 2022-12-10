#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def inspection(num):
    try:
        ins_list = []
        x = 1
        while x < num + 1:
            ins_list.append(x)
            x += 1
        for i in ins_list:
            print(ins_list[i - 1:])
        return inspection(num - 1)
    except RecursionError:
        exit(1)


if __name__ == '__main__':
    num = int(input('Enter the last number of inspection: '))
    inspection(num)
