import pandas as pd

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class KNNModel:
    def __init__(self):
        lysis_data=pd.read_csv("../Stress-Lysis.csv")
        hum_temp_data = lysis_data[['Humidity', 'Temperature']]
        str_lev_data = lysis_data['Stress Level']
    
        train_data , self.test_data , train_label , self.test_label = train_test_split(hum_temp_data, str_lev_data, test_size=0.2)
        self.train_data , self.ver_data , self.train_label , self.ver_label = train_test_split(train_data, train_label, test_size=0.25)

        self.knn_model = KNeighborsClassifier(n_neighbors=3).fit(self.train_data, self.train_label)

    def knn_prediction(self, predict_data):
        return self.knn_model.predict(predict_data)


if __name__ == '__main__':

    KNNModel = KNNModel()
    
    predicted = KNNModel.knn_prediction(KNNModel.ver_data) # 0:Overcast, 2:Mild
    acc_train = accuracy_score(KNNModel.ver_label, predicted)

    predicted = KNNModel.knn_prediction(KNNModel.test_data)
    acc_test = accuracy_score(KNNModel.test_label, predicted)

    print("KNN Verification Accuracy: {} \nKNN Test Accuracy: {}".format(acc_train, acc_test))

    