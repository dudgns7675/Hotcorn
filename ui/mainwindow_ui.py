# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
# from PyQt5.QtWebEngineWidgets import QWebEngineView

class Ui_Mainwindow(object):
    def setupUi(self, Mainwindow):
        Mainwindow.setObjectName("Mainwindow")
        Mainwindow.resize(601, 640)
        self.logBrowser = QtWidgets.QTextBrowser(Mainwindow)
        self.logBrowser.setGeometry(QtCore.QRect(10, 10, 450, 160))
        self.logBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.logBrowser.setObjectName("logBrowser")
        self.htmlBrowser = QtWebEngineWidgets.QWebEngineView(Mainwindow)
        self.htmlBrowser.setGeometry(QtCore.QRect(10, 180, 450, 450))
        # self.htmlBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        # self.htmlBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.htmlBrowser.setObjectName("htmlBrowser")
        self.initButton = QtWidgets.QPushButton(Mainwindow)
        self.initButton.setGeometry(QtCore.QRect(470, 10, 120, 60))
        self.initButton.setObjectName("initButton")
        self.recvButton = QtWidgets.QPushButton(Mainwindow)
        self.recvButton.setGeometry(QtCore.QRect(470, 80, 120, 60))
        self.recvButton.setObjectName("recvButton")
        self.analButton = QtWidgets.QPushButton(Mainwindow)
        self.analButton.setGeometry(QtCore.QRect(470, 150, 120, 60))
        self.analButton.setObjectName("analButton")
        self.seeButton = QtWidgets.QPushButton(Mainwindow)
        self.seeButton.setGeometry(QtCore.QRect(470, 220, 120, 60))
        self.seeButton.setObjectName("seeButton")
        self.closeButton = QtWidgets.QPushButton(Mainwindow)
        self.closeButton.setGeometry(QtCore.QRect(470, 570, 120, 60))
        self.closeButton.setObjectName("closeButton")

        self.retranslateUi(Mainwindow)
        QtCore.QMetaObject.connectSlotsByName(Mainwindow)

    def retranslateUi(self, Mainwindow):
        _translate = QtCore.QCoreApplication.translate
        Mainwindow.setWindowTitle(_translate("Mainwindow", "Hotcorn"))
        self.logBrowser.setHtml(_translate("Mainwindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.initButton.setText(_translate("Mainwindow", "Cache Clear"))
        self.recvButton.setText(_translate("Mainwindow", "Data Receive"))
        self.analButton.setText(_translate("Mainwindow", "Data Analysis"))
        self.seeButton.setText(_translate("Mainwindow", "See Datamap"))
        self.closeButton.setText(_translate("Mainwindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Mainwindow = QtWidgets.QDialog()
    ui = Ui_Mainwindow()
    ui.setupUi(Mainwindow)
    Mainwindow.show()

    # # Load datamap test
    # protocol = "file://"
    # path = "/home/lyh/hotcorn/"
    # filename = "result.html"
    # ui.htmlBrowser.load(QtCore.QUrl(protocol + path + filename))

    sys.exit(app.exec_())

