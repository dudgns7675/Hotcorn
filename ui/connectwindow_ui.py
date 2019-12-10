# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connectwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Connect(object):
    def setupUi(self, Connect):
        Connect.setObjectName("Connect")
        Connect.resize(350, 133)
        self.IPlabel = QtWidgets.QLabel(Connect)
        self.IPlabel.setGeometry(QtCore.QRect(20, 20, 61, 31))
        self.IPlabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.IPlabel.setLineWidth(1)
        self.IPlabel.setTextFormat(QtCore.Qt.AutoText)
        self.IPlabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.IPlabel.setObjectName("IPlabel")
        self.Portlabel = QtWidgets.QLabel(Connect)
        self.Portlabel.setGeometry(QtCore.QRect(10, 60, 67, 31))
        self.Portlabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Portlabel.setObjectName("Portlabel")
        self.loglabel = QtWidgets.QLabel(Connect)
        self.loglabel.setGeometry(QtCore.QRect(10, 100, 231, 16))
        self.loglabel.setObjectName("loglabel")
        self.connectButton = QtWidgets.QPushButton(Connect)
        self.connectButton.setGeometry(QtCore.QRect(250, 60, 89, 25))
        self.connectButton.setObjectName("connectButton")
        self.cancelButton = QtWidgets.QPushButton(Connect)
        self.cancelButton.setGeometry(QtCore.QRect(250, 90, 89, 25))
        self.cancelButton.setObjectName("cancelButton")
        self.IPplainTextEdit = QtWidgets.QPlainTextEdit(Connect)
        self.IPplainTextEdit.setGeometry(QtCore.QRect(90, 20, 131, 31))
        self.IPplainTextEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.IPplainTextEdit.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.IPplainTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.IPplainTextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.IPplainTextEdit.setTabChangesFocus(True)
        self.IPplainTextEdit.setPlainText("")
        self.IPplainTextEdit.setObjectName("IPplainTextEdit")
        self.PortplainTextEdit = QtWidgets.QPlainTextEdit(Connect)
        self.PortplainTextEdit.setGeometry(QtCore.QRect(90, 60, 131, 31))
        self.PortplainTextEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.PortplainTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.PortplainTextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.PortplainTextEdit.setTabChangesFocus(True)
        self.PortplainTextEdit.setPlainText("")
        self.PortplainTextEdit.setObjectName("PortplainTextEdit")

        self.retranslateUi(Connect)
        QtCore.QMetaObject.connectSlotsByName(Connect)

    def retranslateUi(self, Connect):
        _translate = QtCore.QCoreApplication.translate
        Connect.setWindowTitle(_translate("Connect", "Connect"))
        self.IPlabel.setText(_translate("Connect", "<html><head/><body><p><span style=\" font-size:14pt;\">IP</span></p></body></html>"))
        self.Portlabel.setText(_translate("Connect", "<html><head/><body><p><span style=\" font-size:14pt;\">Port</span></p></body></html>"))
        self.loglabel.setText(_translate("Connect", "Please input IP and Port number"))
        self.connectButton.setText(_translate("Connect", "Connect"))
        self.cancelButton.setText(_translate("Connect", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Connect = QtWidgets.QDialog()
    ui = Ui_Connect()
    ui.setupUi(Connect)
    Connect.show()
    sys.exit(app.exec_())

