from classifier_model import ClassifierModel
from sklearn.metrics import accuracy_score


def svm(classifier_model):
    pred_ver = classifier_model.svc_prediction(classifier_model.ver_data)
    average_acc_train = accuracy_score(classifier_model.ver_label, pred_ver)

    pred_test = classifier_model.svc_prediction(classifier_model.test_data)
    average_acc_test = accuracy_score(classifier_model.test_label, pred_test)

    print("SVM Verification Average Accuracy: {} \nSVM Test Average Accuracy: {}".format(average_acc_train, average_acc_test))

def svm_rbf(classifier_model):
    pred_ver = classifier_model.rbf_svc_prediction(classifier_model.ver_data)
    average_acc_train = accuracy_score(classifier_model.ver_label, pred_ver)

    pred_test = classifier_model.rbf_svc_prediction(classifier_model.test_data)
    average_acc_test = accuracy_score(classifier_model.test_label, pred_test)

    print("SVM RBF Verification Average Accuracy: {} \nSVM RBF Test Average Accuracy: {}".format(average_acc_train, average_acc_test))

def svm_poly(classifier_model):
    pred_ver = classifier_model.poly_svc_prediction(classifier_model.ver_data)
    average_acc_train = accuracy_score(classifier_model.ver_label, pred_ver)

    pred_test = classifier_model.poly_svc_prediction(classifier_model.test_data)
    average_acc_test = accuracy_score(classifier_model.test_label, pred_test)

    print("SVM Poly Verification Average Accuracy: {} \nSVM Poly Test Average Accuracy: {}".format(average_acc_train, average_acc_test))

def svm_linear(classifier_model):
    pred_ver = classifier_model.lin_svc_prediction(classifier_model.ver_data)
    average_acc_train = accuracy_score(classifier_model.ver_label, pred_ver)

    pred_test = classifier_model.lin_svc_prediction(classifier_model.test_data)
    average_acc_test = accuracy_score(classifier_model.test_label, pred_test)

    print("SVM Linear Verification Average Accuracy: {} \nSVM Linear Test Average Accuracy: {}".format(average_acc_train, average_acc_test))

def knn(classifier_model):
    predicted = classifier_model.knn_prediction(classifier_model.ver_data) # 0:Overcast, 2:Mild
    average_acc_train = accuracy_score(classifier_model.ver_label, predicted)

    predicted = classifier_model.knn_prediction(classifier_model.test_data)
    average_acc_test = accuracy_score(classifier_model.test_label, predicted)

    print("KNN Verification Average Accuracy: {} \nKNN Test Average Accuracy: {}".format(average_acc_train, average_acc_test))

def decision_tree(classifier_model):
    predicted = classifier_model.decision_tree_prediction(classifier_model.ver_data) # 0:Overcast, 2:Mild
    average_acc_train = accuracy_score(classifier_model.ver_label, predicted)

    predicted = classifier_model.decision_tree_prediction(classifier_model.test_data)
    average_acc_test = accuracy_score(classifier_model.test_label, predicted)

    print("Decision Tree Verification Average Accuracy: {} \nDecision Tree Test Average Accuracy: {}".format(average_acc_train, average_acc_test))

def adaboost(classifier_model):
    predicted = classifier_model.adaboost_prediction(classifier_model.ver_data) # 0:Overcast, 2:Mild
    average_acc_train = accuracy_score(classifier_model.ver_label, predicted)

    predicted = classifier_model.adaboost_prediction(classifier_model.test_data)
    average_acc_test = accuracy_score(classifier_model.test_label, predicted)

    print("Adaboost Verification Average Accuracy: {} \nAdaboost Test Average Accuracy: {}".format(average_acc_train, average_acc_test))

if __name__ == '__main__':
    classifier_model = ClassifierModel()

    svm(classifier_model)
    svm_rbf(classifier_model)
    svm_poly(classifier_model)
    svm_linear(classifier_model)
    knn(classifier_model)
    decision_tree(classifier_model)
    adaboost(classifier_model)
    