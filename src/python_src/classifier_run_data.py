from classifier_model import ClassifierModel
from sklearn.metrics import accuracy_score


def svm(classifier_model):
    pred_ver = classifier_model.svc_prediction(classifier_model.ver_data)
    acc_train = accuracy_score(classifier_model.ver_label, pred_ver)

    pred_test = classifier_model.svc_prediction(classifier_model.test_data)
    acc_test = accuracy_score(classifier_model.test_label, pred_test)

    print("SVM Verification Accuracy: {} \nSVM Test Accuracy: {}".format(acc_train, acc_test))

def svm_rbf(classifier_model):
    pred_ver = classifier_model.rbf_svc_prediction(classifier_model.ver_data)
    acc_train = accuracy_score(classifier_model.ver_label, pred_ver)

    pred_test = classifier_model.rbf_svc_prediction(classifier_model.test_data)
    acc_test = accuracy_score(classifier_model.test_label, pred_test)

    print("SVM RBF Verification Accuracy: {} \nSVM RBF Test Accuracy: {}".format(acc_train, acc_test))

def svm_poly(classifier_model):
    pred_ver = classifier_model.poly_svc_prediction(classifier_model.ver_data)
    acc_train = accuracy_score(classifier_model.ver_label, pred_ver)

    pred_test = classifier_model.poly_svc_prediction(classifier_model.test_data)
    acc_test = accuracy_score(classifier_model.test_label, pred_test)

    print("SVM Poly Verification Accuracy: {} \nSVM Poly Test Accuracy: {}".format(acc_train, acc_test))

def svm_linear(classifier_model):
    pred_ver = classifier_model.lin_svc_prediction(classifier_model.ver_data)
    acc_train = accuracy_score(classifier_model.ver_label, pred_ver)

    pred_test = classifier_model.lin_svc_prediction(classifier_model.test_data)
    acc_test = accuracy_score(classifier_model.test_label, pred_test)

    print("SVM Linear Verification Accuracy: {} \nSVM Linear Test Accuracy: {}".format(acc_train, acc_test))

def knn(classifier_model):
    predicted = classifier_model.knn_prediction(classifier_model.ver_data) # 0:Overcast, 2:Mild
    acc_train = accuracy_score(classifier_model.ver_label, predicted)

    predicted = classifier_model.knn_prediction(classifier_model.test_data)
    acc_test = accuracy_score(classifier_model.test_label, predicted)

    print("KNN Verification Accuracy: {} \nKNN Test Accuracy: {}".format(acc_train, acc_test))

def decision_tree(classifier_model):
    predicted = classifier_model.decision_tree_prediction(classifier_model.ver_data) # 0:Overcast, 2:Mild
    acc_train = accuracy_score(classifier_model.ver_label, predicted)

    predicted = classifier_model.decision_tree_prediction(classifier_model.test_data)
    acc_test = accuracy_score(classifier_model.test_label, predicted)

    print("Decision Tree Verification Accuracy: {} \nDecision Tree Test Accuracy: {}".format(acc_train, acc_test))

def adaboost(classifier_model):
    predicted = classifier_model.adaboost_prediction(classifier_model.ver_data) # 0:Overcast, 2:Mild
    acc_train = accuracy_score(classifier_model.ver_label, predicted)

    predicted = classifier_model.adaboost_prediction(classifier_model.test_data)
    acc_test = accuracy_score(classifier_model.test_label, predicted)

    print("Adaboost Verification Accuracy: {} \nAdaboost Test Accuracy: {}".format(acc_train, acc_test))

if __name__ == '__main__':
    classifier_model = ClassifierModel()

    svm(classifier_model)
    svm_rbf(classifier_model)
    svm_poly(classifier_model)
    svm_linear(classifier_model)
    knn(classifier_model)
    decision_tree(classifier_model)
    adaboost(classifier_model)
    