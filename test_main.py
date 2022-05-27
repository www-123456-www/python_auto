# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : wyy
# @file       :  test_main.py
# @Time    : 2022/5/20 14:38
# @Function:
import os

import pytest

if __name__ == '__main__':
    # pytest.main(["-s","allure-test.py"])
    '''
    -q: 安静模式, 不输出环境信息
    -v: 丰富信息模式, 输出更详细的用例执行信息
    -s: 显示程序中的print/logging输出
    '''
    # pytest.main(["test_pytest_allure/test_allure02.py",'--alluredir=test_pytest_allure/allure-results'])
    #pytest.main([ '-s','-q','./test_pytest_allure/test_allure02.py','--clean-alluredir','--alluredir=./test_pytest_allure/allure-results'])
    #os.system(r"allure generate ./test_pytest_allure/allure-results -c -o ./test_pytest_allure/allure-report")#根据pytest的结果文件，制定生成路径
    # os.system("allure serve ./allure-results")#生成报告，并打开
    os.system(r"pytest test_pytest_allure/test_allure02.py --alluredir=test_pytest_allure/allure-results")
    os.system(
        r"allure generate ./test_pytest_allure/allure-results -c -o ./test_pytest_allure/allure-report")  # 根据pytest的结果文件，制定生成路径
