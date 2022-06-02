# 引入 tkinter 模組
from email import message
import pandas as pd
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkFont
from classifier_model import ClassifierModel
from pandastable import Table, TableModel

# from sklearn.metrics import accuracy_score

# # 自訂函數
# def hello():
#     window = tk.Tk()
#     window.title('Test')

def taipei_pred():

    mon_data = ["110年1月", "110年2月","110年3月","110年4月","110年5月","110年6月","110年7月","110年8月","110年9月","110年10月","110年11月","110年12月","109年1月", "109年2月","109年3月","109年4月","109年5月","109年6月","109年7月","109年8月","109年9月","109年10月","109年11月","109年12月", "108年1月", "108年2月","108年3月","108年4月","108年5月","108年6月","108年7月","108年8月","108年9月","108年10月","108年11月","108年12月"]

    humi_data = [75,74,83,77,74,74,72,79,72,76,78,77,75,72,75,73,77,68,67,70,73,77,76,88,74,79,75,76,77,77,73,72,79,74,75,77]
    temp_data = [60.8,66.38,68.54,72.32,82.76,84.74,86.54,84.02,85.1,78.26,70.16,64.94,64.22,65.66,69.44,69.62,80.42,86.9,87.62,86.36,82.04,76.1,73.94,64.58,65.3,65.84,67.64,75.56,77,83.3,86.54,86.9,81.14,77.54,71.6,66.38]

    data = {'Humidity': humi_data, 'Temperature': temp_data}
    test_data = pd.DataFrame(data)

    class_model = ClassifierModel()

    predict_val = class_model.knn_prediction(test_data)

    show_data = {'Month': mon_data, 'Humidity': humi_data, 'Temperature': temp_data, 'Predict Stress Level':predict_val}
    show_data_frame = pd.DataFrame(show_data)

    weather_result = tk.Tk()
    weather_result.title('Taipei Weather Predict')

    frame = tk.Frame(weather_result)
    # frame.pack(fill='both', expand=True)

    pt = Table(frame)
    pt.model.df = show_data_frame

    pt.show()

    # weather_result.mainloop()

    


def predict_result():
    humidity_data = []
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
    label_temp = tk.Label(window, text = "Temperature(◦F):", font=("Times New Roman", 18))
    label_humi = tk.Label(window, text = "Humidity(RH%):   ", font=("Times New Roman", 18)) 
    label_mod = tk.Label(window, text = "Choose Model:   ", font=("Times New Roman", 18)) 
    
    
    # 建立按鈕
    predict_button = tk.Button(window,   # 按鈕所在視窗
                    text = 'Predict',  # 顯示文字
                    command = predict_result, # 按下按鈕所執行的函數
                    font=("Times New Roman", 18)) 

    label_taiwan_pred = tk.Label(window, text = "Taiwan Weather Prediction 108-110:", font=("Times New Roman", 18)) 

    taipei_predict_button = tk.Button(window,   # 按鈕所在視窗
                    text = 'Taipei',  # 顯示文字
                    command = taipei_pred, # 按下按鈕所執行的函數
                    font=("Times New Roman", 18))


    # grid method to arrange labels in respective 
    # rows and columns as specified
    label_temp.grid(row = 2, column = 1, sticky=tk.E)
    label_humi.grid(row = 3, column = 1, sticky=tk.E)
    label_mod.grid(row = 4, column = 1, sticky=tk.E)
    predict_button.grid(row = 5, column = 1, columnspan = 2)

    taipei_predict_button.grid(row = 7, column = 1, columnspan = 2)

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