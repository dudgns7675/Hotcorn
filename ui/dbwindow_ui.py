# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dbwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DBwindow(object):
    def setupUi(self, DBwindow):
        DBwindow.setObjectName("DBwindow")
        DBwindow.resize(421, 281)
        self.listWidget = QtWidgets.QListWidget(DBwindow)
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 281, 261))
        self.listWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget.setObjectName("listWidget")
        self.seeButton = QtWidgets.QPushButton(DBwindow)
        self.seeButton.setGeometry(QtCore.QRect(300, 10, 111, 61))
        self.seeButton.setObjectName("seeButton")
        self.cancelButton = QtWidgets.QPushButton(DBwindow)
        self.cancelButton.setGeometry(QtCore.QRect(300, 210, 111, 61))
        self.cancelButton.setObjectName("cancelButton")
        self.delButton = QtWidgets.QPushButton(DBwindow)
        self.delButton.setGeometry(QtCore.QRect(300, 80, 111, 61))
        self.delButton.setObjectName("delButton")

        self.retranslateUi(DBwindow)
        QtCore.QMetaObject.connectSlotsByName(DBwindow)

    def retranslateUi(self, DBwindow):
        _translate = QtCore.QCoreApplication.translate
        DBwindow.setWindowTitle(_translate("DBwindow", "Database"))
        self.seeButton.setText(_translate("DBwindow", "See Datamap"))
        self.cancelButton.setText(_translate("DBwindow", "Cancel"))
        self.delButton.setText(_translate("DBwindow", "Delete File"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DBwindow = QtWidgets.QDialog()
    ui = Ui_DBwindow()
    ui.setupUi(DBwindow)
    DBwindow.show()
    sys.exit(app.exec_())

