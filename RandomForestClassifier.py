import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.metrics import classification_report

def RandomForestClassifier(X,y):

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    rfc = RandomForestClassifier(max_depth=5)
    clf = rfc.fit(X_train, y_train)
    tree_rules = export_text(clf, feature_names=list(X.columns))
    print(tree_rules)
    y_pred = clf.predict(X_test)
    print(classification_report(y_test, y_pred))
    print("Accuracy on the training set: {:.2f}".format(clf.score(X_train, y_train)))
    print("Accuracy on the test set: {:.2f}".format(clf.score(X_test, y_test)))
