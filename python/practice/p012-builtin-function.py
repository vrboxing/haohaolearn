#! /usr/bin/python3
# -*- coding: utf-8 -*-

# 内建(built-in)函数是python解释器具有的函数和类型集合。
# https://docs.python.org/3/library/functions.html

if __name__ == '__main__':

    # str()
    # type()

    # zip(*iterables)
    # 构建一个迭代器，该迭代器集成每个迭代变量中的元素
    x = [1, 2, 3]
    y = [4, 5, 6]
    zipped = zip(x, y)
    list(zipped)
    # *zip(x,y)用于解压成列表
    x2, y2 = zip(*zip(x, y))

    # len(s)
    # 返回对象的长度，参数可以为序列(字符串、元组、列表或域)或集合(字典、集合)
    len(x)
    len('123')

    # round(number[,ndigits])
    # 返回一个具有ndigits精度的数字
    round(1 / 3, 3)
    round(0.5)
    round(0.7)
    round(1.5)
    round(-0.5)
