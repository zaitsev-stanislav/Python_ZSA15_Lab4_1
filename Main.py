#!/usr/bin/env python3
# coding=utf-8

import sys
from random import randint

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('uis/main.ui', self)  # загрузка формы в py-скрипт

        self.setWindowTitle('Работа с визуальными табличными данными в Python')
        self.setWindowIcon(QtGui.QIcon('images/logo.png'))

        self.btn_random_number.clicked.connect(self.fill_random_numbers)
        self.btn_solve.clicked.connect(self.solve)

    def fill_random_numbers(self):
        """
        Метод для кнопки "Заполнить случайными числами"
        Случайные числа от 1 до 100
        """
        self.label_info.setText("")
        row = 0
        col = 0
        while row < self.tableWidget.rowCount():
            while col < self.tableWidget.columnCount():
                random_num = randint(0, 100)
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(random_num)))
                col += 1
            row += 1
            col = 0

    def solve(self):
        """
        Метод для кнопки "Выполнить задание"
        """
        try:
            self.label_info.setText("Error!")

            self.uslovie()
            self.brain()
        except:
            pass

    def brain(self):
        """
        Поиск суммы чисел во второй строке
        :return: сумма чисел во второй строке
        """

        max = float(self.tableWidget.item(0, 0).text())
        max_cors = [0, 0]
        min = float(self.tableWidget.item(0, 0).text())
        min_cors = [0, 0]

        row = 0
        col = 0
        while row < self.tableWidget.rowCount():
            while col < self.tableWidget.columnCount():
                if (float(self.tableWidget.item(row, col).text()) > max):  # max elem

                    max = float(self.tableWidget.item(row, col).text())
                    max_cors[0] = row
                    max_cors[1] = col

                if (float(self.tableWidget.item(row, col).text()) < min):  # min elem
                    min = float(self.tableWidget.item(row, col).text())
                    min_cors[0] = row
                    min_cors[1] = col

                col += 1
            row += 1

        uslovie = False
        row = 0

        while row < self.tableWidget.rowCount():  # проверка условия
            if (float(self.tableWidget.item(row, 1).text()) == 1):
                uslovie = True
            else:
                uslovie = False
            row +=1

        if (uslovie):
            # print("Условие выполнено")
            self.label_info.setText("Условие выполнено!")
            self.tableWidget.setItem(max_cors[0], max_cors[1], QTableWidgetItem(str(100)))
            self.tableWidget.setItem(min_cors[0], min_cors[1], QTableWidgetItem(str(5)))


    def uslovie(self):
        """
        ЗАхардкодил условие
        """
        row = 0

        while row < self.tableWidget.rowCount():
            self.tableWidget.setItem(row, 1, QTableWidgetItem(str(1)))
            row +=1


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
