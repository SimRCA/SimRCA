import pandas as pd
import numpy as np
import config as cg
from RulesClassification import RulesClassification
from DecisionTreeClassification import DecisionTreeClassification
data = pd.read_csv('data/abnormal_kpi_file.csv')
kpi_title = ["down_MAC_throughput(bps)",
             "up_MAC_throughput(bps)",  "RSRP(dBm)", "RSRQ(dB)"]
x = data[kpi_title]
y = data.iloc[:,-1]
RulesClassification(x, y)
DecisionTreeClassification(x,y)

