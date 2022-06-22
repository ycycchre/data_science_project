import pandas as pd

from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class SVMModel:
    def __init__(self):
        lysis_data=pd.read_csv("../Stress-Lysis.csv")
        hum_temp_data = lysis_data[['Humidity', 'Temperature']]
        str_lev_data = lysis_data['Stress Level']
    
        train_data , self.test_data , train_label , self.test_label = train_test_split(hum_temp_data, str_lev_data, test_size=0.2)
        self.train_data , self.ver_data , self.train_label , self.ver_label = train_test_split(train_data, train_label, test_size=0.25)


        self.svc_model = svm.SVC(kernel='linear', C=2).fit(self.train_data, self.train_label)
        self.rbf_svc_model = svm.SVC(kernel='rbf', gamma=0.7, C=2).fit(self.train_data, self.train_label)
        self.poly_svc_model = svm.SVC(kernel='poly', degree=3, C=2).fit(self.train_data, self.train_label)
        self.lin_svc_model = svm.LinearSVC(C=2, dual=False).fit(self.train_data, self.train_label)

    def svc_prdiction(self, predict_data):
        return self.svc_model.predict(predict_data)

    def rbf_svc_prdiction(self, predict_data):
        return self.rbf_svc_model.predict(predict_data)

    def poly_svc_prdiction(self, predict_data):
        return self.poly_svc_model.predict(predict_data)

    def lin_svc_prdiction(self, predict_data):
        return self.lin_svc_model.predict(predict_data)

if __name__ == '__main__':

    SVMModel = SVMModel()

    pred_ver = SVMModel.svc_prdiction(SVMModel.ver_data)
    acc_train = accuracy_score(SVMModel.ver_label, pred_ver)

    pred_test = SVMModel.svc_prdiction(SVMModel.test_data)
    acc_test = accuracy_score(SVMModel.test_label, pred_test)

    print("SVM Verification Accuracy: {} \nSVM Test Accuracy: {}".format(acc_train, acc_test))

    pred_ver = SVMModel.rbf_svc_prdiction(SVMModel.ver_data)
    acc_train = accuracy_score(SVMModel.ver_label, pred_ver)

    pred_test = SVMModel.rbf_svc_prdiction(SVMModel.test_data)
    acc_test = accuracy_score(SVMModel.test_label, pred_test)

    print("SVM RBF Verification Accuracy: {} \nSVM RBF Test Accuracy: {}".format(acc_train, acc_test))

    pred_ver = SVMModel.poly_svc_prdiction(SVMModel.ver_data)
    acc_train = accuracy_score(SVMModel.ver_label, pred_ver)

    pred_test = SVMModel.poly_svc_prdiction(SVMModel.test_data)
    acc_test = accuracy_score(SVMModel.test_label, pred_test)

    print("SVM Poly Verification Accuracy: {} \nSVM Poly Test Accuracy: {}".format(acc_train, acc_test))

    pred_ver = SVMModel.lin_svc_prdiction(SVMModel.ver_data)
    acc_train = accuracy_score(SVMModel.ver_label, pred_ver)

    pred_test = SVMModel.lin_svc_prdiction(SVMModel.test_data)
    acc_test = accuracy_score(SVMModel.test_label, pred_test)

    print("SVM Linear Verification Accuracy: {} \nSVM Linear Test Accuracy: {}".format(acc_train, acc_test))


    