# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : wyy
# @file       :  re_em.py
# @Time    : 2022/5/19 11:31
# @Function:
import re
#规则
#https://www.jb51.net/article/34642.htm
#实践
#https://blog.csdn.net/qq_40679091/article/details/109250279

re_obj= re.compile("hello")#
result = re_obj.search("helloworld")
print(result,"----",result.group(),"----", type(result))


# print(re.match("hEllo", "hellolzt whElloorHellold"))                 #始头匹配 类似 “^”       返回 re_obj
#
# print(re.search("hello", "2018helllolzt wohellorlhellod"))            #任意位置匹配第一个子串    返回 re_obj
#
# print(re.fullmatch("hello", "hello"))                                #完全匹配                返回 re_obj

print(re.findall("(he[l|ll]o.*?l)", "lzt helo chilna helo world"))   #匹配所有子串            返回list

print(re.split("hello", "hello china hello world hello",0,re.I))     #根据子串切割（分割）     返回list

print(re.sub("hello", "hi", "hello china hello world", 2) )          #替换                   返回string

result_finditer = re.finditer("hello", "hello world hello china")    #返回 re_obj 迭代器
for i in result_finditer:
    print(i.group())

"""
正则规则：
	单字符：
        .：除换行符外的所有字符
		[]:[aoe]a,o,e之中的一个；[a-w]a到w之间任意一个字符
		\d:数字[0-9]
		\D:非数字
		\w：数字，字母，下划线，中文
		\W：非\w
		\s:所有的空白字符
		\S：所有的非空白
	数量修饰：
		*：任意多次，大于等于0次
		+：至少一次,>=1
		？:可有可无，0次或者1次
		{m}:固定m次
		{m,}:至少m次
		{m,ne}:至少m次，最大n次
	边界
		\b  匹配位于开始或结尾的空字符串
		\B  匹配不位于开始或结尾的空字符串
		$：以某某开头
		^:以某某结尾
	分组：
		():(ab){4}视为一个整体，
		():子模式  \组模式  \1,\2
	贪婪模式：
		.*？
		.+？

"""