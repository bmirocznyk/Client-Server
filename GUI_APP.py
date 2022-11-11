# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_APP.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QFileDialog
from PyQt5.QtGui import QMovie,QIcon


class Ui_MainWindow(QDialog):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 442)
        font = QtGui.QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QTextEdit(self.centralwidget)
        self.title.setEnabled(False)
        self.title.setGeometry(QtCore.QRect(-1, -1, 601, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.title.setFont(font)
        self.title.setAccessibleName("")
        self.title.setAccessibleDescription("")
        self.title.setAutoFillBackground(False)
        self.title.setStyleSheet("background-image: url(:/BackGround/35024.jpg);")
        self.title.setReadOnly(True)
        self.title.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.title.setObjectName("title")
        self.messagesBox = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.messagesBox.setGeometry(QtCore.QRect(0, 300, 601, 131))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setItalic(True)
        self.messagesBox.setFont(font)
        self.messagesBox.setStyleSheet("background-color: rgb(0, 0, 255);\n"
        "color: rgb(255, 255, 255);")
        self.messagesBox.setUndoRedoEnabled(False)
        self.messagesBox.setReadOnly(True)
        self.messagesBox.setPlainText("")
        self.messagesBox.setBackgroundVisible(False)
        self.messagesBox.setObjectName("messagesBox")
        self.connectButton = QtWidgets.QPushButton(self.centralwidget)
        self.connectButton.setGeometry(QtCore.QRect(200, 210, 231, 23))
        self.connectButton.setObjectName("connectButton")
        self.browse = QtWidgets.QPushButton(self.centralwidget)
        self.browse.setGeometry(QtCore.QRect(330, 170, 231, 21))
        self.browse.setObjectName("browse")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 170, 41, 21))
        self.label_2.setAutoFillBackground(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.fileName = QtWidgets.QLineEdit(self.centralwidget)
        self.fileName.setGeometry(QtCore.QRect(60, 170, 241, 21))
        self.fileName.setObjectName("fileName")
        self.ipLabel = QtWidgets.QLabel(self.centralwidget)
        self.ipLabel.setGeometry(QtCore.QRect(10, 120, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ipLabel.setFont(font)
        self.ipLabel.setAutoFillBackground(True)
        self.ipLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ipLabel.setWordWrap(False)
        self.ipLabel.setObjectName("ipLabel")
        self.ipField = QtWidgets.QLineEdit(self.centralwidget)
        self.ipField.setGeometry(QtCore.QRect(40, 120, 261, 21))
        self.ipField.setInputMask("")
        self.ipField.setText("")
        self.ipField.setObjectName("ipField")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 260, 601, 41))
        self.frame.setStyleSheet("background-color: rgb(0, 0, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 10, 111, 16))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("color: rgb(255, 255, 0);")
        self.label.setObjectName("label")
        self.ipLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.ipLabel_2.setGeometry(QtCore.QRect(310, 120, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ipLabel_2.setFont(font)
        self.ipLabel_2.setAutoFillBackground(True)
        self.ipLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.ipLabel_2.setWordWrap(False)
        self.ipLabel_2.setObjectName("ipLabel_2")
        self.ipField_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.ipField_2.setGeometry(QtCore.QRect(360, 120, 231, 21))
        self.ipField_2.setInputMask("")
        self.ipField_2.setText("")
        self.ipField_2.setObjectName("ipField_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.browse.clicked.connect(self.browseFiles)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; text-decoration: underline;\">CONEXION CON </span></p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; text-decoration: underline;\">EL SERVIDOR</span></p></body></html>"))
        self.connectButton.setText(_translate("MainWindow", "Conectar"))
        self.browse.setText(_translate("MainWindow", "Buscar Archivo"))
        self.label_2.setText(_translate("MainWindow", "Archivo"))
        self.ipLabel.setText(_translate("MainWindow", "IP:"))
        self.ipField.setPlaceholderText(_translate("MainWindow", "Ingrese la ip del Server al que se quiere conectar"))
        self.label.setText(_translate("MainWindow", "Mensajes del servidor:"))
        self.ipLabel_2.setText(_translate("MainWindow", "PORT:"))
        self.ipField_2.setPlaceholderText(_translate("MainWindow", "Ingrese el puerto a utilizar"))
    
    def browseFiles(self):
        fName = QFileDialog.getOpenFileName(self, 'Abrir Archivo', 'D:')
        self.fileName.setText(fName[0])


import image_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setWindowTitle('Cliente')
    MainWindow.setWindowIcon(QIcon('C:/Users/Usuario/Pictures/clientIcon.png'))
    MainWindow.show()
    sys.exit(app.exec_())

