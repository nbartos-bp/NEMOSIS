# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 15:18:27 2019

@author: Nick
"""

from nemosis import data_fetch_methods

d = data_fetch_methods.dynamic_data_compiler('2019/01/01 00:00:00', '2019/01/02 00:00:00',
                                             'PREDISPATCH_PRICE','E:/NEMOSIS_raw_data')