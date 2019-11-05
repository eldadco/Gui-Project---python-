# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(810, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.run = QtWidgets.QPushButton(self.centralwidget)
        self.run.setGeometry(QtCore.QRect(150, 10, 99, 27))
        self.run.setObjectName("run")
        self.stop = QtWidgets.QPushButton(self.centralwidget)
        self.stop.setGeometry(QtCore.QRect(270, 10, 99, 27))
        self.stop.setObjectName("stop")
        self.logs = QtWidgets.QPushButton(self.centralwidget)
        self.logs.setGeometry(QtCore.QRect(400, 10, 99, 27))
        self.logs.setObjectName("logs")
        self.test = QtWidgets.QPushButton(self.centralwidget)
        self.test.setGeometry(QtCore.QRect(20, 10, 99, 27))
        self.test.setObjectName("test")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(240, 50, 481, 501))
        self.textBrowser.setObjectName("textBrowser")
        self.tree = QtWidgets.QTreeWidget(self.centralwidget)
        self.tree.setGeometry(QtCore.QRect(10, 50, 221, 431))
        self.tree.setObjectName("tree")
        self.tree.headerItem().setText(0, "1")
        self.select_all = QtWidgets.QPushButton(self.centralwidget)
        self.select_all.setGeometry(QtCore.QRect(120, 450, 99, 27))
        self.select_all.setObjectName("select_all")
        self.deselect_all = QtWidgets.QPushButton(self.centralwidget)
        self.deselect_all.setGeometry(QtCore.QRect(10, 450, 99, 27))
        self.deselect_all.setObjectName("deselect_all")
        self.clear = QtWidgets.QPushButton(self.centralwidget)
        self.clear.setGeometry(QtCore.QRect(530, 10, 99, 27))
        self.clear.setObjectName("clear")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 810, 25))
        self.menubar.setObjectName("menubar")
        self.menuGui_project = QtWidgets.QMenu(self.menubar)
        self.menuGui_project.setObjectName("menuGui_project")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuGui_project.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.run.setText(_translate("MainWindow", "Run"))
        self.stop.setText(_translate("MainWindow", "Stop"))
        self.logs.setText(_translate("MainWindow", "Logs"))
        self.test.setText(_translate("MainWindow", "Tests"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#00aa00;\">Click on Logs button to show up the tests results</span></p></body></html>"))
        self.select_all.setText(_translate("MainWindow", "Select all"))
        self.deselect_all.setText(_translate("MainWindow", "Deselect all"))
        self.clear.setText(_translate("MainWindow", "Clear"))
        self.menuGui_project.setTitle(_translate("MainWindow", "Gui project"))

