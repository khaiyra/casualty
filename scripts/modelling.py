import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


class Models():
    def __init__(self, df:pd.DataFrame):
        self.df = df
        #self.x_train = x_train
        #self.x_test = x_test
        #self.y_train = y_train
        #self.y_test = y_test

    def split_data(self):
        train, test = train_test_split(self.df, random_state=20, test_size=0.2)
        print('Train: ', train.shape)
        print('Hold-out: ', test.shape)

    def log_reg(self):
        #Using Logistic Regression
        from sklearn.linear_model import LogisticRegression
        log = LogisticRegression(random_state = 0)
        log.fit(x_train, y_train)
        #print model accuracy on the training data.
        print('[0]Logistic Regression Training Accuracy:', log.score(x_train, y_train))
        print('[1]Logistic Regression Testing Accuracy:', log.score(x_test, y_test))
    
    def svc_linear(self):
        #Using SVC linear
        from sklearn.svm import SVC
        svc_lin = SVC(kernel = 'linear', random_state = 0)
        svc_lin.fit(x_train, y_train)
        #print model accuracy on the training data
        print('[0]Support Vector Machine (Linear Classifier) Training Accuracy:', svc_lin.score(x_train, y_train))
        print('[1]Support Vector Machine (Linear Classifier) Testing Accuracy:', svc_lin.score(x_test, y_test))
    
    def svc_rbf(self):
        #Using SVC rbf
        from sklearn.svm import SVC
        svc_rbf = SVC(kernel = 'rbf', random_state = 0)
        svc_rbf.fit(x_train, y_train)
        #print model accuracy on the training data
        print('[0]Support Vector Machine (RBF Classifier) Training Accuracy:', svc_rbf.score(x_train, y_train))
        print('[1]Support Vector Machine (RBF Classifier) Testing Accuracy:', svc_rbf.score(x_test, y_test))
    
    def decision_tree(self):
        #Using DecisionTreeClassifier 
        from sklearn.tree import DecisionTreeClassifier
        tree = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
        tree.fit(x_train, y_train)
        #print model accuracy on the training data
        print('[0]Decision Tree Classifier Training Accuracy:', tree.score(x_train, y_train))
        print('[1]Decision Tree Classifier Testing Accuracy:', tree.score(x_test, y_test))
    
    def random_forest(self):
        #Using RandomForestClassifier method of ensemble class to use Random Forest Classification algorithm
        from sklearn.ensemble import RandomForestClassifier
        forest = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 0)
        forest.fit(x_train, y_train)
        #print model accuracy on the training data 
        print('[0]Random Forest Classifier Training Accuracy:', forest.score(x_train, y_train))
        print('[1]Random Forest Classifier Testing Accuracy:', forest.score(x_test, y_test))

