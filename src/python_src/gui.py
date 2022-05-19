# 引入 tkinter 模組
import tkinter as tk
import tkinter.font as tkFont

# # 自訂函數
# def hello():
#     window = tk.Tk()
#     window.title('Test')

# def onOK():
#     # 取得輸入文字
#     print("Hello, {}.".format(entry.get()))

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
    Label_temp = tk.Label(window, text = "Temperature:", font=("Times New Roman", 18))
    Label_humi = tk.Label(window, text = "Humidity:   ", font=("Times New Roman", 18)) 
    
    # grid method to arrange labels in respective 
    # rows and columns as specified
    Label_temp.grid(row = 2, column = 1, sticky=tk.E)
    Label_humi.grid(row = 3, column = 1, sticky=tk.E)

    # entry widgets, used to take entry from user 
    entry_temp = tk.Entry(window, width = 20)
    entry_humi = tk.Entry(window, width = 20)

    # this will arrange entry widgets 
    entry_temp.grid(row = 2, column = 2, sticky=tk.W)
    entry_humi.grid(row = 3, column = 2, sticky=tk.W)

    # # 輸入欄位
    # entry = tk.Entry(window,     # 輸入欄位所在視窗
    #                 width = 20) # 輸入欄位的寬度

    # # 建立按鈕
    # button = tk.Button(window,          # 按鈕所在視窗
    #                 text = 'Hello',  # 顯示文字
    #                 command = hello) # 按下按鈕所執行的函數

    # 執行主程式
    window.mainloop()