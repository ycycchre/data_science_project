import pandas as pd

import matplotlib.pyplot as plt
import numpy as np

def linear_with_correlation(x_data, y_data, x_name, y_name):
    correlation = x_data.corr(y_data)
    print("correlation coefficient between", x_name, "and", y_name, "is", correlation)

    plt.scatter(x_data, y_data, alpha=0.8)
    plt.xlabel(x_name)
    plt.ylabel(y_name)
    plt.title("Correlation = {}".format(correlation))
    plt.show()

def linear_with_correlation_all(linear_data_x, linear_data_y, linear_name_x, linear_name_y):
    plot_row = 0
    plot_column = 0

    fig, axs = plt.subplots(2, 3)

    for i in range(6):
        correlation = linear_data_x[i].corr(linear_data_y[i])
        print("correlation coefficient between", linear_name_x[i], "and", linear_name_y[i], "is", correlation)
        axs[plot_column, plot_row].scatter(linear_data_x[i], linear_data_y[i], alpha=0.8)
        axs[plot_column, plot_row].set(xlabel=linear_name_x[i], ylabel=linear_name_y[i])
        axs[plot_column, plot_row].set_title("Correlation = {}".format(correlation))
        if (plot_row == 2):
            plot_column += 1
            plot_row = 0
        else:
            plot_row += 1


    fig.tight_layout()
    fig.set_figheight(6)
    fig.set_figwidth(12)
    plt.show()

    

def set_column_num(label):
    if (label == 'Humidity'):
        return 0
    elif(label == 'Temperature'):
        return 1
    elif(label == 'Step count'):
        return 2
    else:
        return None
    
def linear_show_with_stress_level_all_in_one(stress_level_classifier_data, x_name, y_name):
    x_num = set_column_num(x_name)
    y_num = set_column_num(y_name)

    stress_0 = stress_level_classifier_data[0]
    stress_1 = stress_level_classifier_data[1]
    stress_2 = stress_level_classifier_data[2]

    plt.scatter(stress_0.iloc[:, x_num], stress_0.iloc[:, y_num], c="red", marker='o', label='Stress Level 0')
    plt.scatter(stress_1.iloc[:, x_num], stress_1.iloc[:, y_num], c="blue", marker='*', label='Stress Level 1')
    plt.scatter(stress_2.iloc[:, x_num], stress_2.iloc[:, y_num], c="yellow", marker='+', label='Stress Level 2')

    plt.xlabel(x_name)
    plt.ylabel(y_name)

    plt.show()

def linear_show_with_stress_level_split_to_three(stress_level_classifier_data, x_name, y_name):

    x_num = set_column_num(x_name)
    y_num = set_column_num(y_name)
    color = ["red", "blue", "yellow"]
    marker = ['o', '*', '+']
    num = 0

    for stress_level in stress_level_classifier_data:
        label_name = "Stress Level" + str(num)
        plt.scatter(stress_level.iloc[:, x_num], stress_level.iloc[:, y_num], c=color[num], marker=marker[num], label=label_name)
        plt.xlabel(x_name)
        plt.ylabel(y_name)

        plt.show()
        num += 1

def linear_show_with_stress_level_all(stress_level_classifier_data):
    linear_name_x = ['Humidity', 'Temperature', 'Temperature']
    linear_name_y = ['Step count', 'Step count', 'Humidity']
    color = ["red", "blue", "yellow"]
    marker = ['o', '*', '+']

    stress_0 = stress_level_classifier_data[0]
    stress_1 = stress_level_classifier_data[1]
    stress_2 = stress_level_classifier_data[2]

    plot_row = 0
    plot_column = 0

    fig, axs = plt.subplots(3, 4)

    for i in range(3):
        x_num = set_column_num(linear_name_x[i])
        y_num = set_column_num(linear_name_y[i])

        axs[plot_column, plot_row].scatter(stress_0.iloc[:, x_num], stress_0.iloc[:, y_num], c="red", marker='o', label='Stress Level 0')
        axs[plot_column, plot_row].scatter(stress_1.iloc[:, x_num], stress_1.iloc[:, y_num], c="blue", marker='*', label='Stress Level 1')
        axs[plot_column, plot_row].scatter(stress_2.iloc[:, x_num], stress_2.iloc[:, y_num], c="yellow", marker='+', label='Stress Level 2')

        axs[plot_column, plot_row].set(xlabel=linear_name_x[i], ylabel=linear_name_y[i])
        plot_row += 1
        num = 0

        for stress_level in stress_level_classifier_data:
            label_name = "Stress Level" + str(num)
            axs[plot_column, plot_row].scatter(stress_level.iloc[:, x_num], stress_level.iloc[:, y_num], c=color[num], marker=marker[num], label=label_name)
            axs[plot_column, plot_row].set(xlabel=linear_name_x[i], ylabel=linear_name_y[i])

            num += 1
            plot_row += 1

        if (plot_row == 4):
            plot_column += 1
            plot_row = 0
        else:
            plot_row += 1


    fig.tight_layout()
    fig.set_figheight(8)
    fig.set_figwidth(15)
    plt.show()

    
if __name__ == '__main__':
    lysis_data=pd.read_csv("../Stress-Lysis.csv")

    temp_data = lysis_data['Temperature']
    humi_data = lysis_data['Humidity']
    step_data = lysis_data['Step count']
    str_lev_data = lysis_data['Stress Level']

    stress_level_classifier_data = [lysis_data[str_lev_data == 0], lysis_data[str_lev_data == 1], lysis_data[str_lev_data == 2]]

    linear_data_x = [humi_data, temp_data, step_data, humi_data, temp_data, temp_data]
    linear_data_y = [str_lev_data, str_lev_data, str_lev_data, step_data, step_data, humi_data]
    linear_name_x = ['Humidity', 'Temperature', 'Step count', 'Humidity', 'Temperature', 'Temperature']
    linear_name_y = ['Stress Level', 'Stress Level', 'Stress Level', 'Step count', 'Step count', 'Humidity']

    linear_with_correlation_all(linear_data_x, linear_data_y, linear_name_x, linear_name_y)
    linear_show_with_stress_level_all(stress_level_classifier_data)

    # linear_with_correlation(humi_data, str_lev_data, 'Humidity', 'Stress Level')
    # linear_with_correlation(temp_data, str_lev_data, 'Temperature', 'Stress Level')
    # linear_with_correlation(step_data, str_lev_data, 'Step count', 'Stress Level')
    # linear_with_correlation(humi_data, step_data, 'Humidity', 'Step count')
    # linear_with_correlation(temp_data, step_data, 'Temperature', 'Step count')
    # linear_with_correlation(temp_data, humi_data, 'Temperature', 'Humidity')

    # linear_show_with_stress_level_all_in_one(stress_level_classifier_data, 'Humidity', 'Step count')
    # linear_show_with_stress_level_split_to_three(stress_level_classifier_data, 'Humidity', 'Step count')

    # linear_show_with_stress_level_all_in_one(stress_level_classifier_data, 'Temperature', 'Step count')
    # linear_show_with_stress_level_split_to_three(stress_level_classifier_data, 'Temperature', 'Step count')

    # linear_show_with_stress_level_all_in_one(stress_level_classifier_data, 'Temperature', 'Humidity')
    # linear_show_with_stress_level_split_to_three(stress_level_classifier_data, 'Temperature', 'Humidity')