import pandas as pd

import matplotlib.pyplot as plt
import numpy as np


class LinearAnaiysis:

    def __init__(self):
        lysis_data=pd.read_csv("../Stress-Lysis.csv")

        self.temp_data = lysis_data['Temperature']
        self.humi_data = lysis_data['Humidity']
        self.step_data = lysis_data['Step count']
        self.str_lev_data = lysis_data['Stress Level']

        self.stress_level_classifier_data = [lysis_data[self.str_lev_data == 0], lysis_data[self.str_lev_data == 1], lysis_data[self.str_lev_data == 2]]

        self.linear_data_x = [self.humi_data, self.temp_data, self.step_data, self.humi_data, self.temp_data, self.temp_data]
        self.linear_data_y = [self.str_lev_data, self.str_lev_data, self.str_lev_data, self.step_data, self.step_data, self.humi_data]
        self.linear_name_x = ['Humidity', 'Temperature', 'Step count', 'Humidity', 'Temperature', 'Temperature']
        self.linear_name_y = ['Stress Level', 'Stress Level', 'Stress Level', 'Step count', 'Step count', 'Humidity']

    def get_data_by_name(self, name):
        if (name == 'Humidity'):
            return self.humi_data
        elif(name == 'Temperature'):
            return self.temp_data
        elif(name == 'Step count'):
            return self.step_data
        elif (name == 'Stress Level'):
            return self.str_lev_data
        else:
            return None

    def linear_with_correlation(self, x_name, y_name):
        x_data = self.get_data_by_name(x_name)
        y_data = self.get_data_by_name(y_name)
        correlation = x_data.corr(y_data)
        print("correlation coefficient between", x_name, "and", y_name, "is", correlation)

        plt.scatter(x_data, y_data, alpha=0.8)
        plt.xlabel(x_name)
        plt.ylabel(y_name)
        plt.title("Correlation = {}".format(correlation))
        plt.show()

    def linear_with_correlation_all(self):
        plot_row = 0
        plot_column = 0

        fig, axs = plt.subplots(2, 3)

        for i in range(6):
            correlation = self.linear_data_x[i].corr(self.linear_data_y[i])
            print("correlation coefficient between", self.linear_name_x[i], "and", self.linear_name_y[i], "is", correlation)
            axs[plot_column, plot_row].scatter(self.linear_data_x[i], self.linear_data_y[i], alpha=0.8)
            axs[plot_column, plot_row].set(xlabel=self.linear_name_x[i], ylabel=self.linear_name_y[i])
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

        

    def set_column_num(self, label):
        if (label == 'Humidity'):
            return 0
        elif(label == 'Temperature'):
            return 1
        elif(label == 'Step count'):
            return 2
        else:
            return None
        
    def linear_show_with_stress_level_all_in_one(self, x_name, y_name):
        x_num = self.set_column_num(x_name)
        y_num = self.set_column_num(y_name)

        stress_0 = self.stress_level_classifier_data[0]
        stress_1 = self.stress_level_classifier_data[1]
        stress_2 = self.stress_level_classifier_data[2]

        plt.scatter(stress_0.iloc[:, x_num], stress_0.iloc[:, y_num], c="red", marker='o', label='Stress Level 0')
        plt.scatter(stress_1.iloc[:, x_num], stress_1.iloc[:, y_num], c="blue", marker='*', label='Stress Level 1')
        plt.scatter(stress_2.iloc[:, x_num], stress_2.iloc[:, y_num], c="yellow", marker='+', label='Stress Level 2')

        plt.xlabel(x_name)
        plt.ylabel(y_name)

        plt.show()

    def linear_show_with_stress_level_split_to_three(self, x_name, y_name):

        x_num = self.set_column_num(x_name)
        y_num = self.set_column_num(y_name)
        color = ["red", "blue", "yellow"]
        marker = ['o', '*', '+']
        num = 0

        for stress_level in self.stress_level_classifier_data:
            label_name = "Stress Level" + str(num)
            plt.scatter(stress_level.iloc[:, x_num], stress_level.iloc[:, y_num], c=color[num], marker=marker[num], label=label_name)
            plt.xlabel(x_name)
            plt.ylabel(y_name)

            plt.show()
            num += 1

    def linear_show_with_stress_level_all(self):
        linear_name_x = ['Humidity', 'Temperature', 'Temperature']
        linear_name_y = ['Step count', 'Step count', 'Humidity']
        color = ["red", "blue", "yellow"]
        marker = ['o', '*', '+']

        stress_0 = self.stress_level_classifier_data[0]
        stress_1 = self.stress_level_classifier_data[1]
        stress_2 = self.stress_level_classifier_data[2]

        plot_row = 0
        plot_column = 0

        fig, axs = plt.subplots(3, 4)

        for i in range(3):
            x_num = self.set_column_num(linear_name_x[i])
            y_num = self.set_column_num(linear_name_y[i])

            axs[plot_column, plot_row].scatter(stress_0.iloc[:, x_num], stress_0.iloc[:, y_num], c="red", marker='o', label='Stress Level 0')
            axs[plot_column, plot_row].scatter(stress_1.iloc[:, x_num], stress_1.iloc[:, y_num], c="blue", marker='*', label='Stress Level 1')
            axs[plot_column, plot_row].scatter(stress_2.iloc[:, x_num], stress_2.iloc[:, y_num], c="yellow", marker='+', label='Stress Level 2')

            axs[plot_column, plot_row].set(xlabel=linear_name_x[i], ylabel=linear_name_y[i])
            plot_row += 1
            num = 0

            for stress_level in self.stress_level_classifier_data:
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

    linear_analysis = LinearAnaiysis()

    linear_analysis.linear_with_correlation_all()
    linear_analysis.linear_show_with_stress_level_all()


    # linear_analysis.linear_with_correlation('Humidity', 'Stress Level')
    # linear_analysis.linear_with_correlation('Temperature', 'Stress Level')
    # linear_analysis.linear_with_correlation('Step count', 'Stress Level')
    # linear_analysis.linear_with_correlation('Humidity', 'Step count')
    # linear_analysis.linear_with_correlation('Temperature', 'Step count')
    # linear_analysis.linear_with_correlation('Temperature', 'Humidity')



    # linear_analysis.linear_show_with_stress_level_all_in_one('Humidity', 'Step count')
    # linear_analysis.linear_show_with_stress_level_split_to_three('Humidity', 'Step count')

    # linear_analysis.linear_show_with_stress_level_all_in_one('Temperature', 'Step count')
    # linear_analysis.linear_show_with_stress_level_split_to_three('Temperature', 'Step count')

    # linear_analysis.linear_show_with_stress_level_all_in_one('Temperature', 'Humidity')
    # linear_analysis.linear_show_with_stress_level_split_to_three('Temperature', 'Humidity')