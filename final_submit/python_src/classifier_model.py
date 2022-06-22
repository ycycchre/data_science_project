import pandas as pd

from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import train_test_split

class ClassifierModel:
    def __init__(self):
        lysis_data=pd.read_csv("../Stress-Lysis.csv")
        hum_temp_data = lysis_data[['Humidity', 'Temperature']]
        str_lev_data = lysis_data['Stress Level']
    
        train_data , self.test_data , train_label , self.test_label = train_test_split(hum_temp_data, str_lev_data, test_size=0.2)
        self.train_data , self.ver_data , self.train_label , self.ver_label = train_test_split(train_data, train_label, test_size=0.25)

        self.knn_model = KNeighborsClassifier(n_neighbors=3).fit(self.train_data, self.train_label)

        self.svc_model = svm.SVC(kernel='linear', C=2).fit(self.train_data, self.train_label)
        self.rbf_svc_model = svm.SVC(kernel='rbf', gamma=0.7, C=2).fit(self.train_data, self.train_label)
        self.poly_svc_model = svm.SVC(kernel='poly', degree=3, C=2).fit(self.train_data, self.train_label)
        self.lin_svc_model = svm.LinearSVC(C=2, dual=False).fit(self.train_data, self.train_label)

        self.decision_tree_model = AdaBoostClassifier(DecisionTreeClassifier(max_depth=2), n_estimators=50).fit(self.train_data, self.train_label)
        self.adaboost_model = AdaBoostClassifier(n_estimators=50, random_state=0).fit(self.train_data, self.train_label)


    def svc_prediction(self, predict_data):
        return self.svc_model.predict(predict_data)

    def rbf_svc_prediction(self, predict_data):
        return self.rbf_svc_model.predict(predict_data)

    def poly_svc_prediction(self, predict_data):
        return self.poly_svc_model.predict(predict_data)

    def lin_svc_prediction(self, predict_data):
        return self.lin_svc_model.predict(predict_data)

    def knn_prediction(self, predict_data):
        return self.knn_model.predict(predict_data)

    def decision_tree_prediction(self, predict_data):
        return self.decision_tree_model.predict(predict_data)

    def adaboost_prediction(self, predict_data):
        return self.adaboost_model.predict(predict_data)


