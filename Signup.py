# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import res, sys
from Ulogin import *
from Ulogin import Ui_login
import MySQLdb



class Ui_Signup(object):
    def setupUi(self, Signup):
        Signup.setObjectName("Signup")
        Signup.resize(682, 677)
        self.widget = QtWidgets.QWidget(Signup)
        self.widget.setGeometry(QtCore.QRect(30, 30, 621, 631))
        self.widget.setStyleSheet("QPushButton#registerbtn{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477,stop:0 rgba(11,131,120,219),stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255,255,255,210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#registerbtn:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));}\n"
"QPushButton#registerbtn:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"background-color:rgba(150, 123, 111,255);}\n"
"\n"
"QPushButton#logbtn{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477,stop:0 rgba(11,131,200,219),stop:1 rgba(150, 98, 112, 226));\n"
"    color:rgba(255,255,255,210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#logbtn:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));}\n"
"QPushButton#logbtn:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"background-color:rgba(150, 123, 111,255);}\n"
"")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(19, 30, 301, 571))
        self.label.setStyleSheet("\n"
"border-image: url(:/pics/pics/kl.jpg);\n"
"border-top-left-radius:50px;\n"
"border-bottom-right-radius:50px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 281, 571))
        self.label_2.setStyleSheet("\n"
"background-color:rgba(0,0,0,80);\n"
"border-top-left-radius:50px;\n"
"border-bottom-right-radius:50px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(270, 20, 331, 571))
        self.label_3.setStyleSheet("background-color:rgba(255,255,255,255);\n"
"border-bottom-right-radius: 50px;\n"
"border-top-left-radius: 50px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(360, 110, 151, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgba(0,0,0,200);")
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(300, 180, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom: 7px;")
        self.lineEdit.setObjectName("lineEdit")
        self.password = QtWidgets.QLineEdit(self.widget)
        self.password.setGeometry(QtCore.QRect(300, 320, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.password.setFont(font)
        self.password.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom: 7px;")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.registerbtn = QtWidgets.QPushButton(self.widget)
        self.registerbtn.setGeometry(QtCore.QRect(330, 480, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.registerbtn.setFont(font)
        self.registerbtn.setObjectName("registerbtn")
        self.registerbtn.clicked.connect(self.register)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(19, 80, 251, 130))
        self.label_5.setStyleSheet("background-color:rgba(0,0,0,75);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(20, 80, 211, 40))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:rgba(255,255,255,210);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(30, 130, 220, 50))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:rgba(255,255,255,200);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.email = QtWidgets.QLineEdit(self.widget)
        self.email.setGeometry(QtCore.QRect(300, 250, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.email.setFont(font)
        self.email.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom: 7px;")
        self.email.setObjectName("email")
        self.Cpassword = QtWidgets.QLineEdit(self.widget)
        self.Cpassword.setGeometry(QtCore.QRect(300, 390, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Cpassword.setFont(font)
        self.Cpassword.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom: 7px;")
        self.Cpassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Cpassword.setObjectName("Cpassword")
        self.logbtn = QtWidgets.QPushButton(self.widget)
        self.logbtn.setGeometry(QtCore.QRect(160, 140, 91, 31))
        self.logbtn.clicked.connect(self.log)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.logbtn.setFont(font)
        self.logbtn.setObjectName("logbtn")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(20, 120, 201, 16))
        self.label_8.setStyleSheet("color:rgba(255,255,255,210);")
        self.label_8.setObjectName("label_8")
        self.error = QtWidgets.QLabel(self.widget)
        self.error.setGeometry(QtCore.QRect(344, 550, 171, 20))
        self.error.setText("")
        self.error.setObjectName("error")

        self.retranslateUi(Signup)
        QtCore.QMetaObject.connectSlotsByName(Signup)

    def retranslateUi(self, Signup):
        _translate = QtCore.QCoreApplication.translate
        Signup.setWindowTitle(_translate("Signup", "Sign Up"))
        self.label_4.setText(_translate("Signup", "Sign Up"))
        self.lineEdit.setPlaceholderText(_translate("Signup", " user name"))
        self.password.setPlaceholderText(_translate("Signup", " password"))
        self.registerbtn.setText(_translate("Signup", "Sign Up"))
        self.label_6.setText(_translate("Signup", "Cars RENTAL"))
        self.email.setPlaceholderText(_translate("Signup", "email"))
        self.Cpassword.setPlaceholderText(_translate("Signup", " Confirm password"))
        self.logbtn.setText(_translate("Signup", "login"))
        self.label_8.setText(_translate("Signup", "if you allready have an account"))
    
    def log(self):
          signup.close()
          self.Principe = QtWidgets.QMainWindow()
          self.uui=Ui_login()
          self.uui.setupUi(self.Principe) 
          self.Principe.show() 
              
    def register(self):
        self.db = MySQLdb.connect(host='localhost' ,user='root' ,password='Houssam@2002' ,db='carrental')
        self.cur= self.db.cursor()
        name = self.lineEdit.text().lower()
        email = self.email.text()
        password = self.password.text()
        Cpassword = self.Cpassword.text()
        
        if name=="" or email=="" or password=="" or Cpassword=="":
                M=QtWidgets.QMessageBox.warning(signup,"empty input", "please fill in ur information!!")
                return
        if password==Cpassword:  
                self.cur.execute('''insert into users (nomp,email,password) values((%s), (%s), (%s))''', (name, email, password))
                self.db.commit()

                signup.close()
                self.Principe = QtWidgets.QMainWindow()
                self.uui=Ui_login()
                self.uui.setupUi(self.Principe) 
                self.Principe.show() 
                            
        else:
                M=QtWidgets.QMessageBox.warning(signup,"erreur", "password doesnt match")
                self.lineEdit.setText("")
                self.email.setText("")
                self.password.setText("")
                self.Cpassword.setText("")


if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        signup= QtWidgets.QWidget()
        ui = Ui_Signup()
        ui.setupUi(signup)
        signup.show()
        sys.exit(app.exec_())

