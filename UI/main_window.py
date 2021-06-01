# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\C_Projects\My-Github\Cryptography\Caeser cipher\UI\main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(495, 200)
        MainWindow.setMinimumSize(QtCore.QSize(495, 200))
        MainWindow.setMaximumSize(QtCore.QSize(495, 200))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(20, 0, 20, -1)
        self.horizontalLayout.setSpacing(50)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_encrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_encrypt.setEnabled(False)
        self.btn_encrypt.setStyleSheet("QPushButton{\n"
"    font: 75 16pt \"MS Shell Dlg 2\";\n"
"    height: 35px;\n"
"    color: rgb(90, 185, 234);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #e0e0e0;\n"
"    border-style: inset;\n"
"}\n"
"QPushButton:disabled {\n"
"    background-color:  rgb(208, 208, 208);\n"
"    color: rgb(173, 173, 173);\n"
"    border-style: inset;\n"
"}")
        self.btn_encrypt.setObjectName("btn_encrypt")
        self.horizontalLayout.addWidget(self.btn_encrypt)
        self.btn_decrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_decrypt.setEnabled(False)
        self.btn_decrypt.setStyleSheet("QPushButton{\n"
"    font: 75 16pt \"MS Shell Dlg 2\";\n"
"    height: 35px;\n"
"    color: rgb(90, 185, 234);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #e0e0e0;\n"
"    border-style: inset;\n"
"}\n"
"QPushButton:disabled {\n"
"    background-color:  rgb(208, 208, 208);\n"
"    color: rgb(173, 173, 173);\n"
"    border-style: inset;\n"
"}")
        self.btn_decrypt.setObjectName("btn_decrypt")
        self.horizontalLayout.addWidget(self.btn_decrypt)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 495, 21))
        self.menubar.setObjectName("menubar")
        self.menu_About = QtWidgets.QMenu(self.menubar)
        self.menu_About.setObjectName("menu_About")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_Open_File = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("d:\\C_Projects\\My-Github\\Cryptography\\Caeser cipher\\UI\\resources/046.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Open_File.setIcon(icon)
        self.action_Open_File.setObjectName("action_Open_File")
        self.action_Decrypt_File = QtWidgets.QAction(MainWindow)
        self.action_Decrypt_File.setIcon(icon)
        self.action_Decrypt_File.setObjectName("action_Decrypt_File")
        self.action_Exit = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("d:\\C_Projects\\My-Github\\Cryptography\\Caeser cipher\\UI\\resources/101.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Exit.setIcon(icon1)
        self.action_Exit.setObjectName("action_Exit")
        self.action_About = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("d:\\C_Projects\\My-Github\\Cryptography\\Caeser cipher\\UI\\resources/073.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_About.setIcon(icon2)
        self.action_About.setObjectName("action_About")
        self.menu_About.addAction(self.action_About)
        self.menu_File.addAction(self.action_Open_File)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Exit)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_About.menuAction())

        self.retranslateUi(MainWindow)
        self.action_About.triggered.connect(MainWindow.show)
        self.action_Exit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Caeser cipher"))
        self.btn_encrypt.setText(_translate("MainWindow", "Encrypt"))
        self.btn_decrypt.setText(_translate("MainWindow", "Decrypt"))
        self.menu_About.setTitle(_translate("MainWindow", "&Help"))
        self.menu_File.setTitle(_translate("MainWindow", "&File"))
        self.action_Open_File.setText(_translate("MainWindow", "&Open File "))
        self.action_Open_File.setToolTip(_translate("MainWindow", "Open file to Encrypt"))
        self.action_Open_File.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.action_Decrypt_File.setText(_translate("MainWindow", "&Decrypt File "))
        self.action_Decrypt_File.setToolTip(_translate("MainWindow", "Open file to Decrypt"))
        self.action_Decrypt_File.setShortcut(_translate("MainWindow", "Ctrl+D"))
        self.action_Exit.setText(_translate("MainWindow", "&Exit"))
        self.action_Exit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.action_About.setText(_translate("MainWindow", "&About"))
        self.action_About.setShortcut(_translate("MainWindow", "Ctrl+I"))