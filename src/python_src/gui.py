# 引入 tkinter 模組
from email import message
import pandas as pd
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkFont
from classifier_model import ClassifierModel
# from sklearn.metrics import accuracy_score

# # 自訂函數
# def hello():
#     window = tk.Tk()
#     window.title('Test')

def predict_result():
    data = {'Humidity': [float(entry_humi.get())], 'Temperature': [float(entry_temp.get())]}

    test_data = pd.DataFrame(data)
    model = combo_mod.get()
    class_model = ClassifierModel()
    predict_val = -1

    if (model == "K-NN"):
        predict_val = class_model.knn_prediction(test_data)[0]
    elif (model == "Decision Tree"):
        predict_val = class_model.decision_tree_prediction(test_data)[0]
    elif (model == "Adaboost"):
        predict_val = class_model.adaboost_prediction(test_data)[0]
    elif (model == "SVM"):
        predict_val = class_model.svc_prediction(test_data)[0]
    elif (model == "SVM Poly"):
        predict_val = class_model.poly_svc_prediction(test_data)[0]
    elif (model == "SVM RBF"):
        predict_val = class_model.rbf_svc_prediction(test_data)[0]
    elif (model == "SVM Linear"):
        predict_val = class_model.lin_svc_prediction(test_data)[0]
    else:
        # message = tk.Tk()
        # message.title('Warning')
        # label_warning_message = 
        print("Please choose a predict model.")

    res_val.config(text = str(predict_val))
       
    # print("Hello, {}.".format(predict_val))


if __name__ == "__main__":

    # 建立主視窗 Frame
    window = tk.Tk()

    # 設定視窗標題
    window.title('Predict Stress Level')

    # 標示文字
    title_label_font_style = tkFont.Font(family="Times New Roman", size=24, weight="bold")
    title = tk.Label(window, text = 'Predict Stress Level by Temperature and Humidity',
                     font = title_label_font_style)
    title.grid(row = 1, column = 0, columnspan = 7)
    
    # this will create a label widget
    label_temp = tk.Label(window, text = "Temperature:", font=("Times New Roman", 18))
    label_humi = tk.Label(window, text = "Humidity:   ", font=("Times New Roman", 18)) 
    label_mod = tk.Label(window, text = "Choose Model:   ", font=("Times New Roman", 18)) 
    
    
    # 建立按鈕
    predict_button = tk.Button(window,   # 按鈕所在視窗
                    text = 'Predict',  # 顯示文字
                    command = predict_result, # 按下按鈕所執行的函數
                    font=("Times New Roman", 18)) 


    # grid method to arrange labels in respective 
    # rows and columns as specified
    label_temp.grid(row = 2, column = 1, sticky=tk.E)
    label_humi.grid(row = 3, column = 1, sticky=tk.E)
    label_mod.grid(row = 4, column = 1, sticky=tk.E)
    predict_button.grid(row = 5, column = 1, columnspan = 2)

    # entry widgets, used to take entry from user 
    entry_temp = tk.Entry(window, width = 20)
    entry_humi = tk.Entry(window, width = 20)

    combo_mod = ttk.Combobox(window, 
                            values=[
                                    "K-NN", 
                                    "Decision Tree",
                                    "Adaboost",
                                    "SVM",
                                    "SVM Poly",
                                    "SVM RBF",
                                    "SVM Linear"])

    # this will arrange entry widgets 
    entry_temp.grid(row = 2, column = 2, sticky=tk.W)
    entry_humi.grid(row = 3, column = 2, sticky=tk.W)
    combo_mod.grid(row = 4, column = 2, sticky=tk.W)

    label_res = tk.Label(window, text = "Predict Stress Level:", font=("Times New Roman", 18))
    res_val = tk.Label(window, text = "", font=("Times New Roman", 52))

    label_res.grid(row = 2, column = 3, sticky=tk.W)
    res_val.grid(row = 3, column = 3, rowspan = 3)

    # # 輸入欄位
    # entry = tk.Entry(window,     # 輸入欄位所在視窗
    #                 width = 20) # 輸入欄位的寬度

    # 執行主程式
    window.mainloop()