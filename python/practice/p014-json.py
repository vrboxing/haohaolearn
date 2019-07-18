#! /usr/bin/python3
# -*- coding: utf-8 -*-

# http://c.biancheng.net/view/2423.html
import json


def linux(s):
    print("%s is linux" % s)


def gnu(s):
    print("%s is gnu" % s)


if __name__ == '__main__':

    json.__all__

    # python字典
    p = {"name": 'yeeku', "gender": 'male', "linux": linux, "gnu": gnu}

    p["linux"]("debian")
    p["gnu"]("emacs")

    # 不可转换为json
    # s = json.dumps(p)

    # dump和dumps属于编码操作，将obj对象转换为json字符串

    # json.dumps(obj)
    # 将obj对象转换为json字符串，并返回该字符串
    q = {"name": 'yeeku', "gender": 'male'}

    s = json.dumps(q)
    print(s)

    # json.dump(obj, f)
    # 将obj转换为json字符中，并存于f文件
    f = open("a.json", "w")
    json.dump(q, f)
    f.close()

    # load和loads为解码操作，将json字符串恢复为python列表

    result1 = json.loads('["yeeku", {"favorite": ["coding", null, "game", 25]}]')
    print(result1)
