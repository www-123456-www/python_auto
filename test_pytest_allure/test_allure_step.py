# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : wyy
# @file       :  test_allure_step
# @Time    : 2022/5/20 17:21
# @Function:
# -*- coding: utf-8
import os

import allure


@allure.step("步骤1：step1")
def step_1():
    print("step1")


@allure.step("步骤2：step2")
def step_2():
    print("step2")


@allure.feature("test")
class TestEditPage():
    @allure.story("test01")
    def test_1(self):
        """这是成功用例"""
        step_1()
        step_2()
        print("测试成功")

    @allure.story("test02")
    def test_2(self):
        """这是失败用例"""
        assert 1 == 2, "测试失败"

    @allure.story("test03")
    def test_3(self):
        """成功用例3"""
        print("test03")

    def test_31(self):
        """成功用例31"""
        print("成功用例31")

    def test_32(self):
        """成功用例32"""
        print("成功用例32")

    @allure.story("test04")
    def test_04(self):
        """成功用例4"""
        print("test04")

    def test_41(self):
        """失败用例41"""
        print("失败用例41")
        assert 1 == 2

    def test_42(self):
        """成功用例42"""
        print("成功用例42")

if __name__ == '__main__':
    os.system(r"pytest  test_pytest_allure/test_allure_step.py --clean-alluredir --alluredir=test_pytest_allure/allure-results ")
    os.system(
        r"allure generate ./test_pytest_allure/allure-results -c -o ./test_pytest_allure/allure-report")
