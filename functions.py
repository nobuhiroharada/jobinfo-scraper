# coding:utf-8

import datetime

class Functions:

    # def __init__(self):

    def get_exec_date(self):
        exec_date = datetime.datetime.now()
        return exec_date.strftime('%Y-%m-%d')
