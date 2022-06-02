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
    frame.pack(fill='both', expand=True)

    pt = Table(frame, dataframe=show_data_frame, width=605, height=500, cellwidth=150, align='center')

    pt.show()

    # weather_result.mainloop()

def kaohsiung_pred():
    mon_data = ["110年1月", "110年2月","110年3月","110年4月","110年5月","110年6月","110年7月","110年8月","110年9月","110年10月","110年11月","110年12月","109年1月", "109年2月","109年3月","109年4月","109年5月","109年6月","109年7月","109年8月","109年9月","109年10月","109年11月","109年12月", "108年1月", "108年2月","108年3月","108年4月","108年5月","108年6月","108年7月","108年8月","108年9月","108年10月","108年11月","108年12月"]

    humi_data = [69,72,73,75,76,84,81,84,80,77,71,71,70,69,71,69,79,75,76,82,75,74,74,71,71,71,73,74,79,79,81,84,76,72,70,71]
    temp_data = [64.94,69.44,74.48,77.72,84.38,82.76,84.38,83.12,84.38,81.68,76.28,70.16,69.62,71.24,76.46,77,83.48,86.54,86.9,84.38,85.46,82.22,78.44,72.14,71.42,74.84,75.38,80.42,81.5,85.1,84.74,83.84,83.66,81.86,77.18,71.24]

    data = {'Humidity': humi_data, 'Temperature': temp_data}
    test_data = pd.DataFrame(data)

    class_model = ClassifierModel()

    predict_val = class_model.knn_prediction(test_data)

    show_data = {'Month': mon_data, 'Humidity': humi_data, 'Temperature': temp_data, 'Predict Stress Level':predict_val}
    show_data_frame = pd.DataFrame(show_data)

    weather_result = tk.Tk()
    weather_result.title('Kaohsiung Weather Predict')

    frame = tk.Frame(weather_result)
    frame.pack(fill='both', expand=True)

    pt = Table(frame, dataframe=show_data_frame, width=605, height=500, cellwidth=150, align='center')

    pt.show()

def tamsui_pred():
    mon_data = ["110年1月", "110年2月","110年3月","110年4月","110年5月","110年6月","110年7月","110年8月","110年9月","110年10月","110年11月","110年12月","109年1月", "109年2月","109年3月","109年4月","109年5月","109年6月","109年7月","109年8月","109年9月","109年10月","109年11月","109年12月", "108年1月", "108年2月","108年3月","108年4月","108年5月","108年6月","108年7月","108年8月","108年9月","108年10月","108年11月","108年12月"]

    humi_data = [79,80,88,78,82,82,79,84,77,77,80,82,82,85,86,79,84,73,62,72,78,76,76,88,83,87,81,84,82,85,79,77,83,84,80,82]
    temp_data = [59,64.04,65.3,70.7,80.6,83.12,85.1,83.12,83.84,77.36,68.9,63.14,62.24,63.14,67.28,68.18,78.62,84.38,85.82,84.56,79.88,75.2,72.68,63.32,63.68,63.86,66.38,73.58,75.56,81.32,85.28,84.92,79.34,75.74,70.34,64.4]

    data = {'Humidity': humi_data, 'Temperature': temp_data}
    test_data = pd.DataFrame(data)

    class_model = ClassifierModel()

    predict_val = class_model.knn_prediction(test_data)

    show_data = {'Month': mon_data, 'Humidity': humi_data, 'Temperature': temp_data, 'Predict Stress Level':predict_val}
    show_data_frame = pd.DataFrame(show_data)

    weather_result = tk.Tk()
    weather_result.title('Tamsui Weather Predict')

    frame = tk.Frame(weather_result)
    frame.pack(fill='both', expand=True)

    pt = Table(frame, dataframe=show_data_frame, width=605, height=500, cellwidth=150, align='center')

    pt.show()

def hsinchu_pred():
    mon_data = ["110年1月", "110年2月","110年3月","110年4月","110年5月","110年6月","110年7月","110年8月","110年9月","110年10月","110年11月","110年12月","109年1月", "109年2月","109年3月","109年4月","109年5月","109年6月","109年7月","109年8月","109年9月","109年10月","109年11月","109年12月", "108年1月", "108年2月","108年3月","108年4月","108年5月","108年6月","108年7月","108年8月","108年9月","108年10月","108年11月","108年12月"]

    humi_data = [74,76,84,76,78,77,75,79,73,71,76,75,78,74,79,74,78,70,65,72,73,71,73,82,76,80,78,77,77,74,68,74,71,71,70,75]
    temp_data = [59.54,64.22,66.56,71.78,81.5,83.66,85.64,83.48,84.74,78.8,69.98,64.22,62.06,63.68,68,68.9,79.88,85.46,87.44,85.28,81.5,76.82,73.94,64.4,63.86,64.4,66.74,74.48,76.46,82.94,86.36,85.1,80.96,77.36,71.24,64.94]

    data = {'Humidity': humi_data, 'Temperature': temp_data}
    test_data = pd.DataFrame(data)

    class_model = ClassifierModel()

    predict_val = class_model.knn_prediction(test_data)

    show_data = {'Month': mon_data, 'Humidity': humi_data, 'Temperature': temp_data, 'Predict Stress Level':predict_val}
    show_data_frame = pd.DataFrame(show_data)

    weather_result = tk.Tk()
    weather_result.title('Hsinchu Weather Predict')

    frame = tk.Frame(weather_result)
    frame.pack(fill='both', expand=True)

    pt = Table(frame, dataframe=show_data_frame, width=605, height=500, cellwidth=150, align='center')

    pt.show()

def taichung_pred():
    mon_data = ["110年1月", "110年2月","110年3月","110年4月","110年5月","110年6月","110年7月","110年8月","110年9月","110年10月","110年11月","110年12月","109年1月", "109年2月","109年3月","109年4月","109年5月","109年6月","109年7月","109年8月","109年9月","109年10月","109年11月","109年12月", "108年1月", "108年2月","108年3月","108年4月","108年5月","108年6月","108年7月","108年8月","108年9月","108年10月","108年11月","108年12月"]

    humi_data = [71,70,73,70,70,81,77,81,74,71,72,71,76,72,70,70,75,70,74,75,71,69,72,77,75,75,79,79,82,79,79,86,78,71,69,75]
    temp_data = [60.8,66.2,70.7,75.02,83.84,82.04,84.2,82.04,84.2,80.06,72.32,65.84,64.4,66.2,72.14,71.96,81.5,84.38,85.28,83.3,82.58,78.98,75.02,67.1,66.74,68.9,69.98,76.46,77.72,82.76,84.92,83.12,81.86,78.98,73.4,66.74]

    data = {'Humidity': humi_data, 'Temperature': temp_data}
    test_data = pd.DataFrame(data)

    class_model = ClassifierModel()

    predict_val = class_model.knn_prediction(test_data)

    show_data = {'Month': mon_data, 'Humidity': humi_data, 'Temperature': temp_data, 'Predict Stress Level':predict_val}
    show_data_frame = pd.DataFrame(show_data)

    weather_result = tk.Tk()
    weather_result.title('Taichung Weather Predict')

    frame = tk.Frame(weather_result)
    frame.pack(fill='both', expand=True)

    pt = Table(frame, dataframe=show_data_frame, width=605, height=500, cellwidth=150, align='center')

    pt.show()

def hualien_pred():
    mon_data = ["110年1月", "110年2月","110年3月","110年4月","110年5月","110年6月","110年7月","110年8月","110年9月","110年10月","110年11月","110年12月","109年1月", "109年2月","109年3月","109年4月","109年5月","109年6月","109年7月","109年8月","109年9月","109年10月","109年11月","109年12月", "108年1月", "108年2月","108年3月","108年4月","108年5月","108年6月","108年7月","108年8月","108年9月","108年10月","108年11月","108年12月"]

    humi_data = [79,78,84,82,84,84,77,82,80,80,81,75,77,74,80,79,83,75,76,75,76,74,79,81,77,80,75,76,80,81,77,78,75,73,71,75]
    temp_data = [61.88,67.1,70.7,72.86,80.42,82.4,84.56,82.76,82.4,77.36,70.88,67.1,67.1,67.28,70.52,70.7,78.98,84.74,85.1,84.38,81.32,77.54,74.3,68.36,68,69.8,69.62,76.1,75.92,81.86,84.74,84.02,81.32,77.54,73.22,68.36]

    data = {'Humidity': humi_data, 'Temperature': temp_data}
    test_data = pd.DataFrame(data)

    class_model = ClassifierModel()

    predict_val = class_model.knn_prediction(test_data)

    show_data = {'Month': mon_data, 'Humidity': humi_data, 'Temperature': temp_data, 'Predict Stress Level':predict_val}
    show_data_frame = pd.DataFrame(show_data)

    weather_result = tk.Tk()
    weather_result.title('Hualien Weather Predict')

    frame = tk.Frame(weather_result)
    frame.pack(fill='both', expand=True)

    pt = Table(frame, dataframe=show_data_frame, width=605, height=500, cellwidth=150, align='center')

    pt.show()

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


    label_taiwan_pred = tk.Label(window, text = "Taiwan Weather Prediction 108-110:",
                                 font=("Times New Roman", 18, "bold")) 
    taipei_predict_button = tk.Button(window,   # 按鈕所在視窗
                    text = 'Taipei',  # 顯示文字
                    command = taipei_pred, # 按下按鈕所執行的函數
                    font=("Times New Roman", 18))
    kaohsiung_predict_button = tk.Button(window,   # 按鈕所在視窗
                    text = 'Kaohsiung',  # 顯示文字
                    command = kaohsiung_pred, # 按下按鈕所執行的函數
                    font=("Times New Roman", 18))
    tamsui_predict_button = tk.Button(window,   # 按鈕所在視窗
                    text = 'Tamsui',  # 顯示文字
                    command = tamsui_pred, # 按下按鈕所執行的函數
                    font=("Times New Roman", 18))
    hsinchu_predict_button = tk.Button(window,   # 按鈕所在視窗
                    text = 'Hsinchu',  # 顯示文字
                    command = hsinchu_pred, # 按下按鈕所執行的函數
                    font=("Times New Roman", 18))
    taichung_predict_button = tk.Button(window,   # 按鈕所在視窗
                    text = 'Taichung',  # 顯示文字
                    command = taichung_pred, # 按下按鈕所執行的函數
                    font=("Times New Roman", 18))
    hualien_predict_button = tk.Button(window,   # 按鈕所在視窗
                    text = 'Hualien',  # 顯示文字
                    command = hualien_pred, # 按下按鈕所執行的函數
                    font=("Times New Roman", 18))

    label_taiwan_pred.grid(row = 6, column = 1, columnspan = 3, sticky=tk.W)
    taipei_predict_button.grid(row = 7, column = 1)
    kaohsiung_predict_button.grid(row = 7, column = 2)
    tamsui_predict_button.grid(row = 7, column = 3)
    hsinchu_predict_button.grid(row = 8, column = 1)
    taichung_predict_button.grid(row = 8, column = 2)
    hualien_predict_button.grid(row = 8, column = 3)

    # # 輸入欄位
    # entry = tk.Entry(window,     # 輸入欄位所在視窗
    #                 width = 20) # 輸入欄位的寬度

    # 執行主程式
    window.mainloop()