# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'moneytransform.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from contain_zh import is_contain_chinese
from digitalUpper import digital_to_Upper

class Ui_MoneyTransform(object):

    def setupUi(self, MoneyTransform):
        MoneyTransform.setObjectName("MoneyTransform")
        MoneyTransform.resize(351, 362)
        MoneyTransform.setWindowIcon(QtGui.QIcon('logo.ico'))
        QtWidgets.QToolTip.setFont(QtGui.QFont('SansSerif', 10))

        self.Money_Edit = QtWidgets.QLineEdit(MoneyTransform)
        self.Money_Edit.setGeometry(QtCore.QRect(30, 80, 181, 31))
        self.Money_Edit.setObjectName("Money_Edit")
        self.Money_Edit.setToolTip("输入金额")

        self.Transform_Btn = QtWidgets.QPushButton(MoneyTransform)
        self.Transform_Btn.setGeometry(QtCore.QRect(220, 80, 41, 31))
        self.Transform_Btn.setObjectName("Transform_Btn")

        self.Clear_Btn = QtWidgets.QPushButton(MoneyTransform)
        self.Clear_Btn.setGeometry(QtCore.QRect(270, 80, 41, 31))
        self.Clear_Btn.setObjectName("Clear_Btn")

        self.Title_label = QtWidgets.QLabel(MoneyTransform)
        self.Title_label.setGeometry(QtCore.QRect(120, 30, 71, 16))
        self.Title_label.setObjectName("Title_label")

        self.Result_Text = QtWidgets.QTextBrowser(MoneyTransform)
        self.Result_Text.setGeometry(QtCore.QRect(30, 130, 281, 101))
        self.Result_Text.setObjectName("Result_Text")

        # 复制按钮
        self.Copy_Btn = QtWidgets.QPushButton(MoneyTransform)
        self.Copy_Btn.setGeometry(QtCore.QRect(30, 240, 71, 31))
        self.Copy_Btn.setObjectName("Copy_Btn")

        # 退出按钮
        self.Quit_Btn = QtWidgets.QPushButton(MoneyTransform)
        self.Quit_Btn.setGeometry(QtCore.QRect(240, 240, 71, 31))
        self.Quit_Btn.setObjectName("Quit_Btn")

        self.retranslateUi(MoneyTransform)
        QtCore.QMetaObject.connectSlotsByName(MoneyTransform)

    def retranslateUi(self, MoneyTransform):
        _translate = QtCore.QCoreApplication.translate
        MoneyTransform.setWindowTitle(_translate("MoneyTransform", "金额大写转换"))
        self.Transform_Btn.setText(_translate("MoneyTransform", "转换"))
        self.Title_label.setText(_translate("MoneyTransform", "金额数字转换"))
        self.Copy_Btn.setText(_translate("MoneyTransform", "复制"))
        self.Clear_Btn.setText(_translate("MoneyTransform", "清除"))
        self.Quit_Btn.setText(_translate("MoneyTransform", "退出"))
        self.Quit_Btn.clicked.connect(lambda: QtWidgets.QApplication.instance().quit())
        self.Clear_Btn.clicked.connect(lambda: self.clearMoney())
        self.Transform_Btn.clicked.connect(lambda: self.getMoney())


    # 获取输入值
    def getMoney(self):
        money = str(self.Money_Edit.text()).replace(" ", "")
        if money == "":
            self.Result_Text.setText("不能为空")
        elif is_contain_chinese(money) is False:
            self.Result_Text.setText("格式有误")
        else:
            self.Money_Edit.setText(money)
            self.Result_Text.setText(digital_to_Upper(money))

    # 清空已输入
    def clearMoney(self):
        self.Money_Edit.setText("")
        self.Result_Text.setText("")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QMainWindow()
    ui = Ui_MoneyTransform()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())