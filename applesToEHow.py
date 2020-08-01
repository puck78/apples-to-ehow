import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QPushButton, QMessageBox
from PyQt5.QtGui import *
import PyQt5.QtGui
# from PyQt5.QtGui import QPixmap, QRect
from PyQt5 import QtWidgets
#from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, QFile, QTextStream, QTimer
import qdarkstyle
import qdarkgraystyle

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

import praw
import wget
import time
from PIL import Image

import random
import re
from glob import glob



import os

app = QApplication(sys.argv)
Ui_MainWindow, QtBaseClass = uic.loadUiType('qtdesigner1.ui')

class MyPopup(QWidget):


    def __init__(self, image_file, title):
        self.image_file = image_file
        self.title = title
        widget = QWidget.__init__(self)

        self.label = QLabel()
        cwd = os.getcwd()
        # print(dir + '\\' + image_file)
        pixmap = QPixmap(image_file)
        self.label.setPixmap(pixmap)
        self.label.show()

        QTimer.singleShot(5000, self.closePopup)

    def closePopup(self):


        self.msgBox = QMessageBox()
        self.msgBox.setIcon(QMessageBox.Information)
        self.msgBox.setText(self.title)
        self.msgBox.setWindowTitle("QMessageBox Example")
        self.msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        os.remove(self.image_file)
        self.msgBox.show()
        self.label.close()

    def paintEvent(self, e):
        dc = QPainter(self)
        dc.drawLine(0, 0, 100, 100)
        dc.drawLine(100, 0, 0, 100)

        print("Test")
        # print("closed")
        # self.msgBox = QMessageBox()
        # self.msgBox.setIcon(QMessageBox.Information)
        # self.msgBox.setText("hi")
        # self.msgBox.setWindowTitle("What it actually was")
        # self.msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        # self.msgBox.show()




class my_win(QtWidgets.QMainWindow, Ui_MainWindow):


    def __init__(self):
        image_filename = ""
        #self.Form, self.Window = uic.loadUiType('qtdesigner1.ui',self)
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # print(self.ui[1])
        # self.form = self.Form()
        # self.win = self.Window()
        # self.form.setupUi(self.win)
        self.app = app

        file = open("example.qss")
        qss = file.read()
        self.app.setStyleSheet(qss)
        file.close()
        self.show()
        # self.button = self.findChild(QtWidgets.QPushButton, 'pushButton_2')
        # self.button.clicked.connect(self.primeImages)

        self.button = self.findChild(QtWidgets.QPushButton, 'pushButton')
        self.button.clicked.connect(self.play)




        # # self.button.click(print("successS"))
        sys.exit(self.app.exec_())

# def window():
    # set stylesheet


    # file = QFile("BreezeStyleSheets/light.qss")
    # file.open(QFile.ReadOnly | QFile.Text)
    # stream = QTextStream(file)
    # app.setStyleSheet(stream.readAll())


    # app.setStyleSheet(qdarkstyle.load_stylesheet())
    # app.setStyleSheet(qdarkgraystyle.load_stylesheet())
    # Form, Window = uic.loadUiType("qtdesigner1.ui")
    # form = Form()
    # win = Window()
    # form.setupUi(win)
    # button = pushButton
    # button.clicked.connect(showDialog)
    # win = QWidget()
    # button1 = QPushButton(win)
    # button1.setText("Show dialog!")
    # button1.move(50,50)
    # button1.clicked.connect(showDialog)
    # win.setWindowTitle("Click button")

    def primeImages(self):
        import time
        import praw
        import wget
        import re
        import os
        import sys

        import shutil


        r = praw.Reddit(client_id='oi8xE60CLDdltQ',
                             client_secret='CTZADqfxChc37no9ff7j4cynDhc',
                             user_agent='python/urllib')
        already_done = []
        checkWords = ['i.imgur.com',  'jpg', 'png', 'gif', 'gfycat.com', 'webm',]
        gyfwords = ['gfycat.com']

        oDir = "./Output"
        if not os.path.isdir(oDir) or not os.path.exists(oDir):
        	os.makedirs(oDir)
        else:
            shutil.rmtree(oDir)

        while True:
            sub = 'disneyvacation'
            subreddit = r.subreddit(sub)
            print(type(subreddit))
            # print(subreddit)
            # sys.exit()
            for submission in subreddit.hot(limit=400):
                url_text = submission.url

                filename = re.sub(r'^https\:\/\/(.+\/)*([^\.]+)(\..+)$', r'\2', url_text)
                extension = re.sub(r'^https\:\/\/(.+\/)*(.+)(\..+)$', r'\3', url_text)
                #text_filename = re.sub(r'^https\:\/\/(.+\/)*(.+)\..+$', r'\1', url_text)

                print("Filename: " + str(filename) + "\n")
                # print("Without extension: " + str(text_filename) + "\n")
                has_domain = any(string in url_text for string in checkWords)
                print('[LOG] Getting url:  ' + url_text)
                is_gifcat = any(string in url_text for string in gyfwords)
                if submission.id not in already_done and has_domain:
                   if is_gifcat:
                      url = re.sub('http://.*gfycat.com/', '', url_text)
                      url_text = 'http://giant.gfycat.com/' + url + '.gif'
                   print("Before mkdir - filename: " + str(filename) + "\n")
                   # try:
                   cwd = os.getcwd()
                   os.mkdir(cwd + '\\Output\\' + filename)
                   wget.download(url_text, cwd + '\\Output\\' + filename + '\\' + filename + extension)

                   title = submission.comments.list()
                   file = open(cwd + '\\Output\\' + filename + '\\' + filename + '.txt', "w+")
                   for comment in title:
                       try:
                           file.write(comment.body.encode('utf-8').decode('utf-8') + "\n")
                       except:
                           print("can't get comment")
                   file.close()
                   already_done.append(submission.id)
                   print('[LOG] Done Getting ' + url_text)
                   # except:
                   #     print("Error")
        # msgBox = QMessageBox()
        # msgBox.setIcon(QMessageBox.Information)
        # msgBox.setText("Message box pop up window")
        # msgBox.setWindowTitle("QMessageBox Example")
        # msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        # msgBox.buttonClicked.connect(msgButtonClick)

    def play(self):
        r = praw.Reddit(client_id='oi8xE60CLDdltQ',
                             client_secret='CTZADqfxChc37no9ff7j4cynDhc',
                             user_agent='python/urllib')

        already_done = []
        checkWords = ['i.imgur.com',  'jpg', 'png', 'gif', 'gfycat.com', 'webm',]
        gyfwords = ['gfycat.com']
        sub = 'disneyvacation'
        subreddit = r.subreddit(sub)
        submission = subreddit.random()

        url_text = submission.url

        filename = re.sub(r'^https\:\/\/(.+\/)*([^\.]+)(\..+)$', r'\2', url_text)
        extension = re.sub(r'^https\:\/\/(.+\/)*(.+)(\..+)$', r'\3', url_text)

        image_file = wget.download(url_text)

        comments = submission.comments.list()
        print(comments)
        # file = open(cwd + '\\Output\\' + filename + '\\' + filename + '.txt', "w+")
        # title = ""
        for comment in comments:
            if 'http' in comment.body.encode('utf-8').decode('utf-8'):
                title = comment.body.encode('utf-8').decode('utf-8')

        self.openPopup(image_file, title)

    def pickDirectory(self):
        cwd = os.getcwd()
        print(cwd + '\\Output\\')

        # dir = glob(cwd + '\\Output\\')

        dir = random.choice(glob(cwd + '\\Output\\*'))
        print("Dir: " + str(dir))

        contents = os.listdir(dir)
        image_file = ""
        for filename_2 in contents:
            if re.search(r'\.[^t][^x][^t]$', filename_2):
                print(filename_2)
                image_file = filename_2

        print(image_file)
        # self.w = None
        self.openPopup(image_file, dir)




        number_panel = self.findChild(QtWidgets.QLCDNumber, 'lcdNumber')
        # self.lcd = PyQt5.QtWidgets.QLCDNumber(self)
        # self.lcd.setGeometry(30, 40, 200, 25)
        #
        # self.btn = PyQt5.QtGui.QPushButton('Start', self)
        # self.btn.move(40, 80)
        # self.btn.clicked.connect(self.doAction)


    def openPopup(self, image_file, title):
        print("Opening a new popup window...")
        self.w = MyPopup(image_file, title)





    def showDialog(self):
        print("success")
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Message box pop up window")
        msgBox.setWindowTitle("QMessageBox Example")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msgBox.buttonClicked.connect(msgButtonClick)

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
          print('OK clicked')



def msgButtonClick(i):
    print("Button clicked is:",i.text())

if __name__ == '__main__':
   my_win()
