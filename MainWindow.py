import sys
import multiprocessing
import os
import webbrowser
from PyQt5.QtWidgets import QMainWindow, QApplication,QFileDialog,QTreeWidgetItem
from PyQt5 import QtCore
from ui_mainwindow import Ui_MainWindow , QtGui
from subprocess import check_output
from subprocess import Popen ,PIPE
import  subprocess
from subprocess import call
import threading
import datetime
import MyThread
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.test.clicked.connect(self.show_files)
        self.ui.run.clicked.connect(self.run)
        self.ui.logs.clicked.connect(self.add_logs_to_screen)
        self.ui.stop.clicked.connect(self.terminate)
        self.ui.select_all.clicked.connect(self.select_all_check_boxes)
        self.ui.deselect_all.clicked.connect(self.deselect_all_check_boxes)
        self.ui.clear.clicked.connect(self.clear_text_browser)
        self.date =datetime.datetime.now().strftime('%d.%m.20%y')
        self.log_file = None
        self.procces = ""
        self.current_dir = ""
        self.path = "/home/liran/Documents/Bootcamp/projects/week5"
        self.items = []

    # This method open the file browser and let the user choose folder with tests to add as a checkboxes to the tree widget
    def show_files(self):
        self.current_dir= QFileDialog.getExistingDirectory(self,'Select',self.path)
        print(f'the tests on: {str(self.current_dir)} have been added to the tree')
        self.current_dir = str(self.current_dir)
        for i in (os.listdir(self.current_dir)):
            if i.endswith('Test.js'):
                item = QTreeWidgetItem(self.ui.tree,[i])
                self.items.append(item)
                item.setCheckState(0,QtCore.Qt.Unchecked)
        os.chdir(self.current_dir)

    # This method is run the selected tests
    def run(self):
        os.chdir(self.current_dir)
        tests_to_run = self.tests_selected()
        print(tests_to_run)
        counter=0
        full_command_list="node "
        for i in range(0,len(tests_to_run)):
            if(i!=0):
                full_command_list +=' && '+tests_to_run[i]
            else:
                full_command_list +=tests_to_run[i]
        print(full_command_list)
        self.procces = Popen(full_command_list, shell=True)
        print(self.procces.pid)

    # This method marks all checkboxes as checked
    def select_all_check_boxes(self):
        for item in self.items:
            item.setCheckState(0, QtCore.Qt.Checked)

    # This method marks all checkboxes as unchecked
    def deselect_all_check_boxes(self):
        for item in self.items:
            item.setCheckState(0, QtCore.Qt.Unchecked)

    # This method stop the node procces and the chrome procces
    def terminate(self):
        procces_pid = self.procces.pid+1
        child_procces_pid = procces_pid + 18
        procces_pid=str(procces_pid)
        print(procces_pid)
        kill_command = "kill -s 15 "
        print(kill_command + procces_pid)
        os.system(kill_command + procces_pid)
        os.system(kill_command + str(child_procces_pid))

    # This method print the content of the log file to the text browser
    def add_logs_to_screen(self):
        self.ui.textBrowser.clear()
        if os.path.exists(f"logs/{self.date}/log.log"):
            with open(f'logs/{self.date}/log.log','r') as self.log_file:
                log_file_content = self.log_file.read()
                if log_file_content:
                    self.ui.textBrowser.append(str(log_file_content))
                else:
                    self.ui.textBrowser.append('The log file is empty')
        else:
            self.ui.textBrowser.append("The log file does not exist")

    # This method will return an array of the tests that their check boxes were selected
    def tests_selected(self):
        print("Run clicked")
        tests = []
        for i in self.items:
            if i.checkState(0) == QtCore.Qt.Checked:
                test_name=QTreeWidgetItem.text(i,0)
                tests.append(str(test_name))
        return tests

    def clear_text_browser(self):
            self.ui.textBrowser.clear()

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())