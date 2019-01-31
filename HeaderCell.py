# -*- coding: utf-8 -*-


class HeaderCell(object):
    data_index = 0
    data_key = ""
    date_group_key = ""

    def __int__(self, index, key):
        self.data_index = index
        self.data_key = key
