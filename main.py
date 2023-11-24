# -*- coding:utf-8 -*-
# @Time : 2023/4/4 9:45
# @Author: gzr
# @File : main.py.py
# @Description :
import pandas as pd
import numpy as np
import config as cg
from rules_classification import rules_classification
from decision_tree_classification import decision_tree_classification
# read the abnormal file
data = pd.read_csv('/home/fjd/code_space/guo_fault_classification/data/concat_abnormal_kpi_file.csv')
# train data
kpi_title = ["down_MAC_throughput(bps)",
             "up_MAC_throughput(bps)",  "RSRP(dBm)", "RSRQ(dB)"]
x = data[kpi_title]
# lables
y = data.iloc[:,-1]
#print(y)
rules_classification(x, y)
decision_tree_classification(x,y)

 