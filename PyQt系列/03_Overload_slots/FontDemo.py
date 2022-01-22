# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(393, 241)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.fontColor = QtWidgets.QGroupBox(self.centralWidget)
        self.fontColor.setGeometry(QtCore.QRect(20, 10, 351, 58))
        self.fontColor.setObjectName("fontColor")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.fontColor)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.black = QtWidgets.QRadioButton(self.fontColor)
        self.black.setChecked(True)
        self.black.setObjectName("black")
        self.horizontalLayout.addWidget(self.black)
        self.red = QtWidgets.QRadioButton(self.fontColor)
        self.red.setObjectName("red")
        self.horizontalLayout.addWidget(self.red)
        self.blue = QtWidgets.QRadioButton(self.fontColor)
        self.blue.setObjectName("blue")
        self.horizontalLayout.addWidget(self.blue)
        self.textEdit = QtWidgets.QPlainTextEdit(self.centralWidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 140, 351, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.groupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 70, 351, 63))
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.bold = QtWidgets.QCheckBox(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setBold(True)
        font.setWeight(75)
        self.bold.setFont(font)
        self.bold.setObjectName("bold")
        self.horizontalLayout_2.addWidget(self.bold)
        self.italic = QtWidgets.QCheckBox(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setItalic(True)
        self.italic.setFont(font)
        self.italic.setObjectName("italic")
        self.horizontalLayout_2.addWidget(self.italic)
        self.underline = QtWidgets.QCheckBox(self.groupBox)
        self.underline.setObjectName("underline")
        self.horizontalLayout_2.addWidget(self.underline)
        MainWindow.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "简易文字样式设置器"))
        self.fontColor.setTitle(_translate("MainWindow", "选择字体颜色"))
        self.black.setText(_translate("MainWindow", "黑色"))
        self.red.setText(_translate("MainWindow", "红色"))
        self.blue.setText(_translate("MainWindow", "蓝色"))
        self.textEdit.setPlainText(_translate("MainWindow", "人生苦短，我用python"))
        self.groupBox.setTitle(_translate("MainWindow", "选择字体样式"))
        self.bold.setText(_translate("MainWindow", "加粗"))
        self.italic.setText(_translate("MainWindow", "倾斜"))
        self.underline.setText(_translate("MainWindow", "下划线"))
