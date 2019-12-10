from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread, pyqtSignal
from ui.mainwindow_ui import Ui_Mainwindow
from ui.connectwindow_ui import Ui_Connect
from ui.dbwindow_ui import Ui_DBwindow
import os, sys, time
import shutil
import maps, server, vfs

class MainWindow(Ui_Mainwindow):
    def __init__(self, w):
        self.temppath = "temp/"
        self.slicepath = "slice/"

        self.AnalysisThread = darknet()
        self.AnalysisThread.printLog.connect(self.logPrint)

        Ui_Mainwindow.__init__(self)
        self.setupUi(w)
        self.initButton.clicked.connect(self.InitData)
        self.recvButton.clicked.connect(self.DataReceive)
        self.seeButton.clicked.connect(self.SeeDatamap)
        self.analButton.clicked.connect(self.DataAnalysis)
        self.closeButton.clicked.connect(QtCore.QCoreApplication.instance().quit)

    def InitData(self):
        self.logBrowser.append("Cache Initialize Start..."  )
        if os.path.isdir(self.temppath):
            filelist1 = os.listdir(self.temppath)

            for file in filelist1:
                os.remove(self.temppath + file)

        else:
            self.logBrowser.append("Cache Folder not exist!!")
            os.mkdir(self.temppath)
            self.logBrowser.append("Created Cache Folder!")

        if os.path.isdir(self.slicepath):
            filelist2 = os.listdir(self.slicepath)

            for file in filelist2:
                os.remove(self.slicepath + file)
        else:
            self.logBrowser.append("Cache Folder not exist!!")
            os.mkdir(self.slicepath)
            self.logBrowser.append("Created Cache Folder!")
        
        self.logBrowser.append("Cache Initialize Finished")

    def DataAnalysis(self):
        if self.AnalysisThread.workingFlag == 0:
            self.AnalysisThread.start()
        else:
            self.logBrowser.append("Please wait work finish")

    def DataReceive(self):
        w2 = QtWidgets.QDialog()
        ui = ConnectWindow(w2)
        w2.exec_()

        if ui.successFlag == 1:
            self.logPrint("Data Receive Success!")
        elif ui.successFlag == 2:
            self.logPrint("Data Receive Fail...")

    def SeeDatamap(self):
        w3 = QtWidgets.QDialog()
        ui = DBWindow(w3)
        w3.exec_()

        if ui.url != "":
            self.htmlBrowser.load(QtCore.QUrl(ui.url))

    def logPrint(self, text):
        self.logBrowser.append(text)

    

class ConnectWindow(Ui_Connect):
    def __init__(self, w2):
        self.IP = ""
        self.Port = ""
        self.workingFlag = 0
        self.successFlag = 0

        self.ConnectThread = DataRecvThread()
        self.ConnectThread.connectState.connect(self.connectLog)

        Ui_Connect.__init__(self)
        self.Dialog = w2
        self.setupUi(self.Dialog)

        self.connectButton.clicked.connect(self.RecvData)
        self.cancelButton.clicked.connect(self.CancelProcess)

    def RecvData(self):
        flist1 = os.listdir("temp/")
        flist2 = os.listdir("slice/")
        for f in flist1:
            os.remove("temp/" + f)
        for f in flist2:
            os.remove("slice/" + f)

        self.IP = self.IPplainTextEdit.toPlainText()
        self.Port = self.PortplainTextEdit.toPlainText()

        self.ConnectThread.IP = self.IP
        self.ConnectThread.Port = self.Port

        self.ConnectThread.start()

    def CancelProcess(self):
        if self.ConnectThread.workingFlag == 0:
            self.Dialog.close()
        elif self.ConnectThread.workingFlag == 1:
            self.connectLog(6)

    def connectLog(self, flag):
        if flag == 1:
            self.workingFlag = 1
            self.loglabel.setText("Receiving file...")
        elif flag == 2:
            self.loglabel.setText("Slicing video...")
        elif flag == 3:
            self.workingFlag = 0
            self.loglabel.setText("Data Receive Success!")
        elif flag == 4:
            self.loglabel.setText("Timeout! Please Reconnect.")
        elif flag == 5:
            self.loglabel.setText("Data Receive Fail...")
        elif flag == 6:
            self.loglabel.setText("Data Receiving now... Please Wait.")
        elif flag == 7:
            self.successFlag = 1 # receive success
        elif flag == 8:
            self.successFlag = 2 # receive fail


class DBWindow(Ui_DBwindow):
    def __init__(self, w3):
        self.url = ""

        Ui_DBwindow.__init__(self)
        self.Dialog = w3
        self.setupUi(self.Dialog)

        self.seeButton.clicked.connect(self.DataSee)
        self.delButton.clicked.connect(self.DataDelete)
        self.cancelButton.clicked.connect(self.Dialog.close)

        self.DBList = [file.replace(".html",'') for file in os.listdir("DBResult/")]
        self.DBList.sort()
        for dbfile in self.DBList:
            self.listWidget.addItem(dbfile)

    def DataSee(self):
        dbfilename = self.listWidget.currentItem().text()+".html"
        protocol = "file://"
        dbfilepath = os.getcwd()+"/DBResult/"
        self.url = protocol + dbfilepath + dbfilename
        self.Dialog.close()

    def DataDelete(self):
        dbfilename = self.listWidget.currentItem().text()+".html"
        os.remove("DBResult/"+dbfilename)
        self.listWidget.takeItem(self.listWidget.currentRow())


# ===============================================================================================
# Thread functions
class darknet(QThread):
    printLog = pyqtSignal(str)
    workingFlag = 0
    mapfunc = maps.datamap()

    def run(self):
        try:
            self.workingFlag = 1
            self.printLog.emit("Analysis Initializing...")
            sys.path.append(os.path.join(os.getcwd(),'darknet/python/'))
            sys.path.append(os.path.join(os.getcwd()))
            import darknet as dn
            import pdb

            dn.set_gpu(0)
            net = dn.load_net("darknet/cfg/yolov3.cfg".encode('utf-8'), "darknet/backup_corn/yolov3_34000.weights".encode('utf-8'), 0)
            meta = dn.load_meta("darknet/cfg/coco.data".encode('utf-8'))


            path = 'slice/'
            file_list = os.listdir(path)
            if ".DS_Store" in file_list:
                file_list.remove(".DS_Store")

            total_file_num = len(file_list)
            current_file_num = int()

            if os.path.isfile('detection_result.txt'):
                os.remove('detection_result.txt')
            f = open('detection_result.txt', 'a')
                
            self.printLog.emit("Start Analysis...")
            for file_name in file_list:
                self.printLog.emit("Analysing... " + str(current_file_num) + '/' + str(total_file_num))
                filepath = path + file_name
                r = dn.detect(net, meta, filepath.encode('utf-8'))

                current_file_num = current_file_num + 1
                print(str(current_file_num) + '///' + str(total_file_num))
                
                if r:
                    print(r)
                    print(file_name)
                    
                    
                    f.write(file_name)
                    f.write('\n')

            f.close()
            self.printLog.emit("Analysing... " + str(current_file_num) + '/' + str(total_file_num))

            self.printLog.emit("Detect Finished! Making datamap...")
            self.mapfunc.create_map()
            self.printLog.emit("Analysing Finished! Please check DB")
            self.workingFlag = 0
            print("darknet END")

        except OSError:
            self.printLog.emit("Darknet Faild to start!")
            self.printLog.emit("Darknet Reinitializing...")

            if os.path.isfile("darknet/libdarknet.so"):
                os.remove("darknet/libdarknet.so")
            if os.path.isfile("darknet/libdarknet.a"):
                os.remove("darknet/libdarknet.a")
            if os.path.isfile("darknet/darknet"):
                os.remove("darknet/darknet")
            if os.path.isdir("darknet/obj/"):
                shutil.rmtree("darknet/obj/")

            makepath = os.getcwd() + "/darknet"
            os.system("make -C " + makepath)

            self.printLog.emit("Darknet Reinitializing Finished")
            self.printLog.emit("Please try again Analysis")
            self.workingFlag = 0

class DataRecvThread(QThread):
    connectState = pyqtSignal(int)
    IP = ""
    Port = ""
    workingFlag = 0
    def run(self):
        try:
            self.workingFlag = 1
            self.connectState.emit(1)
            server.so(self.IP, int(self.Port))
            self.connectState.emit(2)
            vfs.capture()
            self.connectState.emit(3)
            self.connectState.emit(7)
            self.workingFlag = 0
        except:
            self.connectState.emit(5)
            self.connectState.emit(8)
            self.workingFlag = 0


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QMainWindow()
    ui = MainWindow(w)
    w.show()
    sys.exit(app.exec_())


