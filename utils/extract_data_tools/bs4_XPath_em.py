# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : wyy
# @file       :  bs4_XPath_em.py
# @Time    : 2022/5/24 14:51
# @Function:

#https://www.cnblogs.com/airapple/p/9132374.html
#https://blog.csdn.net/hoochon/article/details/87893497
"""
BeautifulSoup 可以将html文件转换为指定的对象，然后通过对象的方法或属性查找指定的内容
需要安装pip install bs4
bs4 在使用的时候需要一个第三方库，也需要安装
pip install lxml


xml是用来储存和传输数据的、与html的区别：
1、html 是用来显示数据，xml是用来传输数据；
2、html的标签是固定的，xml的标签是自定义的
xpath是一门在xml文档中查找信息的语言，他是一种路径表达式；需要安装第三方插件，pip install lxml
常用的路径表达式：
1、//：不考虑位置的查找
2、./:从当前节点开始往下查找
3、…:当前节点的父节点
4、@：选取属性

使用：安装谷歌xpath插件：xpath helper 2.0.2
导入库：from lxml import etree
使用两种方法:将html文件变成一个对象,然后调用对象的方法去查找指定的节点
1、本地文件：tree=etree.parse(文件名)
2、网络文件：tree=etree.HTML(网页字符串)
ret=tree.xpath(路径表达式) ret是一个列表

"""

#Xpath  是查找xml和html
#选取节点
    # 根节点 ：   /
    # 所有结点：  //
    # 当前节点：  .
    # 当前父节点： ..
  #过滤（属性） @属性