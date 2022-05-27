# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : wyy
# @file       :  JsonPath_em.py
# @Time    : 2022/5/24 13:24
# @Function:
from jsonpath import jsonpath
#https://blog.csdn.net/qq_36595013/article/details/109455924
from lxml import etree
json_example = {
    "store": {
        "book": [
            {
            "ww": {
                "book":"boook",
                "W":"WWWW",
                "price": 8.95},
            "category": "reference",
            "author": "Nigel Rees",
            "title": "Sayings of the Century",
            "price": 8.95
        }, {
            "category": "fiction",
            "author": "Evelyn Waugh",
            "title": "Sword of Honour",
            "price": 12.99
        }, {
            "category": "fiction",
            "author": "Herman Melville",
            "title": "Moby Dick",
            "isbn": "0-553-21311-3",
            "price": 8.99
        }, {
            "category": "fiction",
            "author": "J. R. R. Tolkien",
            "title": "The Lord of the Rings",
            "isbn": "0-395-19395-8",
            "price": 22.99
        }
        ],
        "bicycle": {
            "color": "red",
            "price": 19.95
        }
    }
}
if __name__ == '__main__':
    XPAth_=""
    # jsonPath_=jsonpath(json_example,"$.store.book[*].author")
    # jsonPath_=jsonpath(json_example,"$.store.book[?(@.price>10)]")
    #$.store.[?(@.price)]   查 store下的n层, 返回 price的上层
    #$.store[?(@.price)]    查 store下的1层, 返回 price的上层
    #$.store.[price]        查 store下的n层, 返回 price的value
    #$.store[price]         查 store下的1层, 返回 price的value

    jsonPath_ = jsonpath(json_example, "$.store[price]")

    print(jsonPath_)
    print(len(jsonPath_))

    ##  节点为key

    # 根：                                                $
    #value 为 {...}，过滤 子节点层次(下一层、递归层次)：      .节点         ..节点              [节点（，节点）]       .[节点（，节点）]
                                                         #下级节点      所有节点             下级节点                所有节点
    #value 为 [ {...}(,{...}) ]，
    # 过滤value中的节点：                                    节点[@.节点]  节点[?(条件)]
    # value 为 [...]，过滤(索引)切片：                       节点[*]      节点[start:end:step]   节点[n,m]
