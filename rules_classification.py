# -*- coding:utf-8 -*-
# @Time : 2023/4/4 15:54
# @Author: fjd
# @File : rules_classification.py
# @Description :

from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
def rules_classification(x, y):
    """
    :param x: kpi
    :param y: ground truth
    :return: none
    """

    # rules infer
    rules_infer = []
    for index, row in x.iterrows():
        infer_class = 0
        if row["down_MAC_throughput(bps)"] == 0:
            infer_class = 2
        elif row["down_MAC_throughput(bps)"] >= 60000:
            infer_class = 0
        else:
            if row["RSRP(dBm)"] < -105 :
                if row["RSRQ(dB)"] <-19:
                    infer_class = 2
                elif row["RSRQ(dB)"]<-10:
                    infer_class = 1
                else:
                    infer_class = 0
        rules_infer.append(infer_class)
    accuracy = accuracy_score(y, rules_infer)
    # Print the accuracy score
    print("Accuracy:", accuracy)
    print("Confusion Matrix:\n", confusion_matrix(y, rules_infer))

