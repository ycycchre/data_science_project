import pandas as pd

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class DecisionTreeModel:
    def __init__(self):
        lysis_data=pd.read_csv("../Stress-Lysis.csv")
        hum_temp_data = lysis_data[['Humidity', 'Temperature']]
        str_lev_data = lysis_data['Stress Level']
    
        train_data , self.test_data , train_label , self.test_label = train_test_split(hum_temp_data, str_lev_data, test_size=0.2)
        self.train_data , self.ver_data , self.train_label , self.ver_label = train_test_split(train_data, train_label, test_size=0.25)

        self.decision_tree_model = AdaBoostClassifier(DecisionTreeClassifier(max_depth=2), n_estimators=50).fit(self.train_data, self.train_label)
        self.adaboost_model = AdaBoostClassifier(n_estimators=50, random_state=0).fit(self.train_data, self.train_label)

    def decision_tree_prediction(self, predict_data):
        return self.decision_tree_model.predict(predict_data)

    def adaboost_prediction(self, predict_data):
        return self.adaboost_model.predict(predict_data)


if __name__ == '__main__':

    DecisionTreeModel = DecisionTreeModel()

    predicted = DecisionTreeModel.decision_tree_prediction(DecisionTreeModel.ver_data) # 0:Overcast, 2:Mild
    average_acc_train = accuracy_score(DecisionTreeModel.ver_label, predicted)

    predicted = DecisionTreeModel.decision_tree_prediction(DecisionTreeModel.test_data)
    average_acc_test = accuracy_score(DecisionTreeModel.test_label, predicted)

    print("Decision Tree Verification Average Accuracy: {} \nDecision Tree Test Average Accuracy: {}".format(average_acc_train, average_acc_test))

    predicted = DecisionTreeModel.adaboost_prediction(DecisionTreeModel.ver_data) # 0:Overcast, 2:Mild
    average_acc_train = accuracy_score(DecisionTreeModel.ver_label, predicted)

    predicted = DecisionTreeModel.adaboost_prediction(DecisionTreeModel.test_data)
    average_acc_test = accuracy_score(DecisionTreeModel.test_label, predicted)


    print("Adaboost Verification Average Accuracy: {} \nAdaboost Test Average Accuracy: {}".format(average_acc_train, average_acc_test))

    