#!/usr/bin/env
#-*- coding: utf-8 -*-

import os
import xlrd
import XlsMgr


GROUP_ROW = 1
KEY_ROW = 2
TYPE_ROW = 3
CONTROL_ROW = 4
NAME_ROW = 5
REMARK_ROW = 6


def main():
    print("开始转换......")
    xls_mgr = XlsMgr.XlsMgr()
    xls_mgr.load_xls("operatActivity.xlsx")
    xls_mgr.gen_lua()
    pass


if __name__ == "__main__":
    main()
