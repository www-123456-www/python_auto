# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : wyy
# @file       :  test_allure02.py
# @Time    : 2022/5/20 13:13
# @Function:
import os
import random
import sys
import time

import allure
import pytest


#Allure报告中看到所有默认的pytest状态
@allure.epic("epic-史诗-敏捷组件")#项目或组件
@allure.feature('test_success-模块') #业务模块
@allure.story("sort_用户故事-对象")#开发功能
@allure.title("title_用例标题")#


@allure.severity(allure.severity_level.TRIVIAL) # 不重要的
    # @allure.severity(allure.severity_level.MINOR) # 轻微的
    # @allure.severity(allure.severity_level.BLOCKER)  # 阻塞的
    # @allure.severity(allure.severity_level.CRITICAL)  # 严重的
    # @allure.severity(allure.severity_level.NORMAL)  # 普通的

@allure.description("用例描述")#详细描述

@allure.link("link")
@allure.issue("issue-缺陷url")
@allure.testcase("testcase-链接url")

@allure.step("步骤1")


def test_success():
    """this test succeeds"""
    assert True

@allure.feature('test_failure') #模块名
def test_failure():
    """this test fails"""
    assert False

@allure.feature('test_skip') #模块名
def test_skip():
    """this test is skipped"""
    pytest.skip('for a reason!')

@allure.feature('test_broken') #模块名
def test_broken():
    raise Exception('oops')


#xfail,失败不会影响用例执行。

@allure.feature('test_xfail_expected_failure')
@pytest.mark.xfail(reason='该功能尚未实现')
def test_xfail_expected_failure():
    print("该功能尚未实现")
    assert False

@allure.feature('test_xfail_unexpected_pass')
@pytest.mark.xfail(reason='该Bug尚未修复')
def test_xfail_unexpected_pass():
    print("该Bug尚未修复")
    assert True


#skip，
'''当条件为True则跳过执行'''
@allure.feature("test_skipif")
@pytest.mark.skip(reason="如果操作系统是win则跳过执行")
def test_skip__():
    print("操作系统是win，test_skipif()函数跳过执行")

#skipif，
'''当条件为True则跳过执行'''
@allure.feature("test_skipif")
@pytest.mark.skipif("win32" in sys.platform,reason="如果操作系统是Mac则跳过执行")
def test_skipif():
    print("操作系统是Mac，test_skipif()函数跳过执行")


#parametrize
@allure.step("parametrize 操作步骤")  #操作步骤
def simple_step(step_param1, step_param2 = None):
    pass

@pytest.mark.parametrize('param1', [True, False], ids=['1', '2'])
def test_parameterize_with_id(param1):
    simple_step(param1)

@pytest.mark.parametrize('param1', [True, False])
@pytest.mark.parametrize('param2', ['1', '2'])
def test_parametrize_with_two_parameters(param1, param2):
    simple_step(param1, param2)

#step  步骤说明
@allure.step("步骤二")
def passing_step():
    pass


@allure.step("步骤三")
def step_with_nested_steps():
    nested_step()


@allure.step("步骤四")
def nested_step():
    nested_step_with_arguments(1, 'abc')


@allure.step("步骤五")
def nested_step_with_arguments(arg1, arg2):
    pass


@allure.step("步骤一")
def test_with_nested_steps():
    passing_step()
    step_with_nested_steps()


#attach  allure.attach(body、name、attachment_type、extension)调用来创建附件。
@pytest.fixture
def attach_file_in_module_scope_fixture_with_finalizer(request):
    allure.attach('在fixture前置操作里面添加一个附件txt', 'fixture前置附件', allure.attachment_type.TEXT)

    def finalizer_module_scope_fixture():
        allure.attach('在fixture后置操作里面添加一个附件txt', 'fixture后置附件',allure.attachment_type.TEXT)
    request.addfinalizer(finalizer_module_scope_fixture)

def test_with_attacments_in_fixture_and_finalizer(attach_file_in_module_scope_fixture_with_finalizer):
    pass

def test_multiple_attachments():
    allure.attach('<head></head><body>html page</body>', 'Attach with HTML type', allure.attachment_type.HTML)
    # allure.attach.file('/Users/mrjade/Downloads/happy-new-year.html', attachment_type=allure.attachment_type.HTML)


#description 用例总结描述 类信息
@allure.description_html("""
<h1>这是html描述</h1>
<table style="width:100%">
  <tr>
    <th>Firstname</th>
    <th>Lastname</th>
    <th>Age</th>
  </tr>
  <tr align="center">
    <td>jade</td>
    <td>mr</td>
    <td>18</td>
  </tr>
  <tr align="center">
    <td>road</td>
    <td>Tester</td>
    <td>18</td>
  </tr>
</table>
""")
def test_html_description():
    assert True

@allure.description("""多行描述""")
def test_description_from_decorator():
    assert 42 == int(6 * 7)

def test_unicode_in_docstring_description():
    """在函数下方描述也可"""
    assert 42 == int(6 * 7)


#title 用例标题
@allure.title("断言2+2=4")
def test_with_a_title():
    assert 2 + 2 == 4

@allure.title("动态标题: {param1} + {param2} = {expected}")
@pytest.mark.parametrize('param1,param2,expected', [(2, 2, 4),(1, 2, 5)])
def test_with_parameterized_title(param1, param2, expected):
    assert param1 + param2 == expected

@allure.title("这是个动态标题，会被替换")
def test_with_dynamic_title():
    assert 2 + 2 == 4
    allure.dynamic.title('测试结束，做为标题')


#link  @allure.link、@allure.issue和@allure.testcase。
@allure.link('https://www.cnblogs.com/mrjade/')
def test_with_link():
    pass

@allure.link('https://www.cnblogs.com/mrjade/', name='点击进入mrjade博客园')
def test_with_named_link():
    pass

@allure.issue('https://github.com/allure-framework/allure-python/issues/642', 'bug issue链接')
def test_with_issue_link():
    pass

@allure.testcase("https://www.cnblogs.com/mrjade/", '测试用例地址')
def test_with_testcase_link():
    pass

#Retries  重试 pip3 install pytest-rerunfailures
@allure.step
def passing_step():
    pass

@allure.step
def flaky_broken_step():
    if random.randint(1, 5) != 1:
        raise Exception('Broken!')

"""需安装【pip3 install pytest-rerunfailures】"""
@pytest.mark.flaky(reruns=3, reruns_delay=1)  # 如果失败则延迟1s后重试
def test_broken_with_randomized_time():
    passing_step()
    time.sleep(random.randint(1, 3))
    flaky_broken_step()


# #tags
if __name__ == '__main__':
    os.system(r"pytest  test_pytest_allure/test_allure02.py --clean-alluredir --alluredir=test_pytest_allure/test02/allure-results ")
    os.system(
        r"allure generate ./test_pytest_allure/test02/allure-results -c -o ./test_pytest_allure/test02/allure-report")
#     # pytest.main(["-s","allure-test.py"])
#     '''
#     -q: 安静模式, 不输出环境信息
#     -v: 丰富信息模式, 输出更详细的用例执行信息
#     -s: 显示程序中的print/logging输出
#     '''
#     pytest.main([ '-s','-q','test_allure02.py','--clean-alluredir','--alluredir=./allure-results'])
#     os.system(r"allure generate ./allure-results -c -o ./allure-report")#根据pytest的结果文件，制定生成路径
#     # os.system("allure serve ./allure-results")#生成报告，并打开
