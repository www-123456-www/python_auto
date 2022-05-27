# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : wyy
# @file       :  pandas_file.py
# @Time    : 2022/5/25 16:23
# @Function:
import json

import pandas
from sqlite3 import connect

conn = connect(':memory:')
abspath = ""

# read
df_csv_table = pandas.read_table(abspath)  # csv
df_csv = pandas.read_csv(abspath)
df_json = pandas.read_json(abspath)
df_excel = pandas.read_excel(abspath)
df_sqlite = pandas.read_sql('SELECT int_column, date_column FROM test_data', conn)

# write
df = pandas.DataFrame()

df.to_csv(abspath)
df.to_json(abspath)
df.to_excel(abspath)
df.to_sql('test_data', conn)

#json_to_dict
def json_to_obj():
    json.loads()
