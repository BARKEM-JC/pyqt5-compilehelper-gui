import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import shutil


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(180, 265)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.compile_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.compile_gui())
        self.compile_button.setGeometry(QtCore.QRect(10, 150, 75, 23))
        self.compile_button.setObjectName("compile_button")
        self.test_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.test_gui())
        self.test_button.setGeometry(QtCore.QRect(90, 150, 75, 23))
        self.test_button.setObjectName("test_button")
        self.filename_textbox = QtWidgets.QTextEdit(self.centralwidget)
        self.filename_textbox.setGeometry(QtCore.QRect(10, 20, 151, 21))
        self.filename_textbox.setObjectName("filename_textbox")
        self.filename_label = QtWidgets.QLabel(self.centralwidget)
        self.filename_label.setGeometry(QtCore.QRect(60, 0, 51, 16))
        self.filename_label.setAlignment(QtCore.Qt.AlignCenter)
        self.filename_label.setObjectName("filename_label")
        self.projectpath_label = QtWidgets.QLabel(self.centralwidget)
        self.projectpath_label.setGeometry(QtCore.QRect(50, 50, 71, 20))
        self.projectpath_label.setAlignment(QtCore.Qt.AlignCenter)
        self.projectpath_label.setObjectName("projectpath_label")
        self.projectpath_textbox = QtWidgets.QTextEdit(self.centralwidget)
        self.projectpath_textbox.setGeometry(QtCore.QRect(10, 70, 151, 21))
        self.projectpath_textbox.setObjectName("projectpath_textbox")
        self.uipath_textbox = QtWidgets.QTextEdit(self.centralwidget)
        self.uipath_textbox.setGeometry(QtCore.QRect(10, 120, 151, 21))
        self.uipath_textbox.setObjectName("uipath_textbox")
        self.uipath_label = QtWidgets.QLabel(self.centralwidget)
        self.uipath_label.setGeometry(QtCore.QRect(50, 100, 71, 20))
        self.uipath_label.setAlignment(QtCore.Qt.AlignCenter)
        self.uipath_label.setObjectName("uipath_label")
        self.transfer_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.transfer_gui())
        self.transfer_button.setGeometry(QtCore.QRect(10, 180, 151, 23))
        self.transfer_button.setObjectName("transfer_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 180, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.compile_button.setText(_translate("MainWindow", "Compile"))
        self.test_button.setText(_translate("MainWindow", "Test"))
        self.filename_label.setText(_translate("MainWindow", "Filename"))
        self.projectpath_label.setText(_translate("MainWindow", "Project Path"))
        self.uipath_label.setText(_translate("MainWindow", "UI File Path"))
        self.transfer_button.setText(_translate("MainWindow", "Transfer UI File"))

    def compile_gui(self):
        if self.filename_textbox.toPlainText() != "":
            path = self.projectpath_textbox.toPlainText()
            filename = self.filename_textbox.toPlainText()
            guisavepath = self.uipath_textbox.toPlainText()
            if guisavepath == "":
                guisavepath = f"{projectpath}\\GUISaves"
            if path == "":
                path = f"{projectpath}\\GUISaves"
            print(f'pyuic5 -x {guisavepath}\\{filename}.ui -o {path}\\{filename}.py')
            stream = os.popen(f'pyuic5 -x {guisavepath}\\{filename}.ui -o {path}\\{filename}.py')
            output = stream.read()
            print(output)
        else:
            print("ERROR: Invalid path or filename")

    def transfer_gui(self):
        if self.filename_textbox.toPlainText() != "" and self.projectpath_textbox.toPlainText() != "":
            path = self.projectpath_textbox.toPlainText()
            filename = self.filename_textbox.toPlainText()
            guisavepath = self.uipath_textbox.toPlainText()
            if guisavepath == "":
                guisavepath = f"{projectpath}\\GUISaves"
            shutil.copyfile(f'{guisavepath}\\{filename}.ui', f'{path}\\{filename}.ui')
        else:
            print("ERROR: Invalid path or filename")

    def test_gui(self):
        if self.filename_textbox.toPlainText():
            path = self.projectpath_textbox.toPlainText()
            if path == "":
                path = f"{projectpath}\\GUISaves"
            filename = self.filename_textbox.toPlainText()
            print(f'pyuic5 -x {path}\\{filename}.ui -o {path}\\{filename}.py')
            stream = os.popen(f'python {path}\\{filename}.py')
            output = stream.read()
            print(output)
        else:
            print("ERROR: Invalid path, filename or does not exist")


if __name__ == '__main__':
    projectpath = ""
    if getattr(sys, 'frozen', False):
        projectpath = os.path.dirname(sys.executable)
    elif __file__:
        projectpath = os.path.dirname(__file__)
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# command to compile gui to pythoh:
# pyuic5 -x C:\UE\CodeOnlyProj\pyqt5guidesigner\GUISaves\FILENAME.ui -o C:\UE\CodeOnlyProj\pyqt5guidesigner\GUISaves\FILENAME.py
# pyuic5 -x C:\UE\CodeOnlyProj\pyqt5guidesigner\GUISaves\FILENAME.ui -o C:\UE\CodeOnlyProj\pyqt5guidesigner\GUISaves\FILENAME.py
