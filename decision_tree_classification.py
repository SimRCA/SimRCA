

# 给定数据前k列特征k+1列为标签，标签为三分类问题，划分训练集 测试机，构建决策树模型，判断分类结果
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.metrics import classification_report

def decision_tree_classification(X,y):
    
    # 划分训练集和测试集
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    # 构建决策树模型
    clf = DecisionTreeClassifier(max_depth=5)
    clf.fit(X_train, y_train)

    # 输出决策树的判断逻辑
    tree_rules = export_text(clf, feature_names=list(X.columns))
    print(tree_rules)
    # 预测分类结果
    y_pred = clf.predict(X_test)
    # 输出分类报告
    print(classification_report(y_test, y_pred))
    # 展示一些训练决策树模型结果
    print("训练集上的准确率: {:.2f}".format(clf.score(X_train, y_train)))
    print("测试集上的准确率: {:.2f}".format(clf.score(X_test, y_test)))
    # 判断规则
