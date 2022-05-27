# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : wyy
# @file       :  yaml_file.py
# @Time    : 2022/5/24 15:44
# @Function:
import os

import pytest
import yaml

#os.path.abspath(__file__) 当前文件绝对路径
#os.path.dirname(__file__) 文件上一级路径
file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
# file_path=os.path.abspath(os.path.dirname(__file__))
# path=os.path.abspath(__file__)
# print(path)
print(file_path)

def read(abspath):
    with open(abspath, 'r', encoding="utf-8") as file:
        #msg = yaml.load(file, Loader=yaml.FullLoader)
        return yaml.safe_load(file)

# @pytest.mark.parametrize("a, b, c",read(abs_path))
# def test_add(a, b, c):
#     sum = a + b
#     #断言
#     assert sum == c



