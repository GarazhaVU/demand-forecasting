# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'maindesign.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import shutil
import forecast_generation
from MplCanvasQt import MplCanvas
import treatment
import pandas as pd


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        y_pred = 0
        dover = 0
        fh = 0
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(752, 426)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.SaveButton = QtWidgets.QPushButton(self.centralwidget)
        self.SaveButton.setObjectName("SaveButton")
        self.gridLayout_2.addWidget(self.SaveButton, 4, 0, 1, 1)
        self.CloseButton = QtWidgets.QPushButton(self.centralwidget)
        self.CloseButton.setObjectName("CloseButton")
        self.gridLayout_2.addWidget(self.CloseButton, 5, 0, 1, 1)
        self.DNBox = QtWidgets.QComboBox(self.centralwidget)
        self.DNBox.setObjectName("comboBox")
        self.DNBox.addItem("")
        self.DNBox.addItem("")
        self.DNBox.addItem("")
        self.DNBox.addItem("")
        self.DNBox.addItem("")
        self.DNBox.addItem("")
        self.DNBox.addItem("")
        self.DNBox.addItem("")
        self.DNBox.addItem("")
        self.DNBox.addItem("")
        self.DNBox.addItem("")
        self.DNBox.addItem("")
        self.gridLayout_2.addWidget(self.DNBox, 2, 0, 1, 1)
        self.AddButton = QtWidgets.QPushButton(self.centralwidget)
        self.AddButton.setObjectName("AddButton")
        self.gridLayout_2.addWidget(self.AddButton, 0, 0, 1, 1)
        self.SrokBox = QtWidgets.QComboBox(self.centralwidget)
        self.SrokBox.setObjectName("comboBox_2")
        self.SrokBox.addItem("")
        self.SrokBox.addItem("")
        self.gridLayout_2.addWidget(self.SrokBox, 1, 0, 1, 1)
        self.GenerButton = QtWidgets.QPushButton(self.centralwidget)
        self.GenerButton.setObjectName("GenerButton")
        self.gridLayout_2.addWidget(self.GenerButton, 3, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.Grafics = QtWidgets.QMdiArea(self.centralwidget)
        self.Grafics.setObjectName("Grafics")
        self.gridLayout_3.addWidget(self.Grafics, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 1, 1, 1)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 752, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(mainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(mainWindow)
        self.action_2.setObjectName("action_2")
        # self.action_3 = QtWidgets.QAction(mainWindow)
        # self.action_3.setObjectName("action_3")
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        # self.menu.addAction(self.action_3)
        self.menubar.addAction(self.menu.menuAction())
        self.connect_signal()
        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Прогнозирование спроса"))
        self.SaveButton.setText(_translate("mainWindow", "Сохранить"))
        self.CloseButton.setText(_translate("mainWindow", "Закрыть"))
        self.DNBox.setItemText(0, _translate("mainWindow", "DN15"))
        self.DNBox.setItemText(1, _translate("mainWindow", "DN20"))
        self.DNBox.setItemText(2, _translate("mainWindow", "DN25"))
        self.DNBox.setItemText(3, _translate("mainWindow", "DN32"))
        self.DNBox.setItemText(4, _translate("mainWindow", "DN40"))
        self.DNBox.setItemText(5, _translate("mainWindow", "DN50"))
        self.DNBox.setItemText(6, _translate("mainWindow", "DN65"))
        self.DNBox.setItemText(7, _translate("mainWindow", "DN80"))
        self.DNBox.setItemText(8, _translate("mainWindow", "DN100"))
        self.DNBox.setItemText(9, _translate("mainWindow", "DN125"))
        self.DNBox.setItemText(10, _translate("mainWindow", "DN150"))
        self.DNBox.setItemText(11, _translate("mainWindow", "DN200"))
        self.AddButton.setText(_translate("mainWindow", "Добавить файл"))
        self.SrokBox.setItemText(0, _translate("mainWindow", "3 месяца"))
        self.SrokBox.setItemText(1, _translate("mainWindow", "1 год"))
        self.GenerButton.setText(_translate("mainWindow", "Генерация"))
        self.menu.setTitle(_translate("mainWindow", "Группировка"))
        self.action.setText(_translate("mainWindow", "Каскадно"))
        self.action_2.setText(_translate("mainWindow", "По очереди"))
        # self.action_3.setText(_translate("mainWindow", "Все"))

    def connect_signal(self):
        self.AddButton.clicked.connect(lambda: self.AddButton_clicked())
        self.CloseButton.clicked.connect(lambda: self.CloseButton_clicked())
        self.GenerButton.clicked.connect(lambda: self.GenerButton_clicked())
        self.SaveButton.clicked.connect(lambda: self.SaveButton_clicked())

    def AddButton_clicked(self):
        wb_patch = QtWidgets.QFileDialog.getOpenFileNames(directory="/home", filter="XML files (*.xls)")[0]
        if wb_patch != "":
            for i in range(len(wb_patch)):
                # len_i_wb_patch = len(wb_patch[i])
                mass = wb_patch[i].split('/')
                standart_dir = "./indb/" + mass[-1]
                shutil.copy2(wb_patch[i], standart_dir )
                treatment.CreateTrainExcelFile(standart_dir)
        

    def GenerButton_clicked(self):
        massage = QtWidgets.QMessageBox(MainWindow)
        massage.setText("Подождите, программа выполняется...")
        # massage.setParent(self.Grafics)
        massage.exec()
        
        pop, self.y_pred, self.dover, self.fh = forecast_generation.main(self.DNBox.currentText(), self.SrokBox.currentText())

        # sc = MplCanvas( self.Grafics, width=5, height=4, dpi=100)
        # sc.axes.plot([0,1,2,3,4], [10,1,20,3,40])
        # maingrafic = QtWidgets.QMdiSubWindow()
        # maingrafic.setWidget(sc)
        pop.reverse()
        for i in range(len(pop)):
            pop[i].setParent(self.Grafics)
            self.Grafics.addSubWindow(pop[i])
            pop[i].show()
        # maingrafic.show()
        self.Grafics.tileSubWindows()
        massage.close()
        
    def SaveButton_clicked(self):
        dir_path = QtWidgets.QFileDialog.getExistingDirectory()

        if dir_path != "" and self.y_pred != 0:
            date = pd.read_excel("./train_indb/DN15.xlsx",index_col = False).fillna(0)
            date = date.iloc[-1][0]
            # сделать норм формат файла !!!!!!!!!!!
            if self.SrokBox.currentText() == "3 месяца":
                filename= dir_path +"/forecast"+ self.DNBox.currentText()+"_" + str(date)[0:9]+"_to_3_month.xlsx"
            else:
                filename=dir_path + "/forecast"+ self.DNBox.currentText()+"_" + str(date)[0:9]+"_to_1_year.xlsx"
            
            # Создаем объект writer с указанием пути сохранения filename
            writer = pd.ExcelWriter(filename, engine='xlsxwriter')

            # Записываем данные из датафрейма в Excel
            all = pd.concat([pd.DataFrame(self.y_pred.predicted_mean), pd.DataFrame(self.dover.iloc[: , 0]), pd.DataFrame(self.dover.iloc[: , 1])], axis=1)
            all.columns = ['mean', 'lower', 'upper']
            all['time'] = self.fh
            all = all[['time'] + [x for x in all.columns if x != 'time']]
            all.to_excel(writer, index=False)

            # Сохраняем файл
            # writer.save()
            writer.close()
        

    def CloseButton_clicked(self):
        MainWindow.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    MainWindow.show()
    sys.exit(app.exec_())