# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1408, 875)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 750, 131, 71))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(13)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(260, 0, 20, 831))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(280, 10, 1111, 801))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setIconSize(QtCore.QSize(40, 40))
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setAutoFillBackground(False)
        self.tab.setObjectName("tab")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(990, 700, 101, 51))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(13)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(10, 700, 951, 51))
        self.lineEdit.setObjectName("lineEdit")
        self.listWidget = QtWidgets.QListWidget(self.tab)
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 1081, 671))
        self.listWidget.setObjectName("listWidget")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.listWidget_2 = QtWidgets.QListWidget(self.tab_2)
        self.listWidget_2.setGeometry(QtCore.QRect(10, 10, 1081, 671))
        self.listWidget_2.setObjectName("listWidget_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 700, 951, 51))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4.setGeometry(QtCore.QRect(990, 700, 101, 51))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(13)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.tabWidget.addTab(self.tab_2, "")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 20, 101, 101))
        self.label.setText("")
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 340, 251, 391))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox.setObjectName("groupBox")
        self.cha1 = QtWidgets.QPushButton(self.groupBox)
        self.cha1.setGeometry(QtCore.QRect(30, 30, 81, 81))
        self.cha1.setText("")
        self.cha1.setObjectName("cha1")
        self.cha2 = QtWidgets.QPushButton(self.groupBox)
        self.cha2.setGeometry(QtCore.QRect(140, 30, 81, 81))
        self.cha2.setText("")
        self.cha2.setObjectName("cha2")
        self.cha3 = QtWidgets.QPushButton(self.groupBox)
        self.cha3.setGeometry(QtCore.QRect(30, 120, 81, 81))
        self.cha3.setText("")
        self.cha3.setObjectName("cha3")
        self.cha4 = QtWidgets.QPushButton(self.groupBox)
        self.cha4.setGeometry(QtCore.QRect(140, 120, 81, 81))
        self.cha4.setText("")
        self.cha4.setObjectName("cha4")
        self.cha5 = QtWidgets.QPushButton(self.groupBox)
        self.cha5.setGeometry(QtCore.QRect(30, 210, 81, 81))
        self.cha5.setText("")
        self.cha5.setObjectName("cha5")
        self.cha6 = QtWidgets.QPushButton(self.groupBox)
        self.cha6.setGeometry(QtCore.QRect(140, 210, 81, 81))
        self.cha6.setText("")
        self.cha6.setObjectName("cha6")
        self.cha7 = QtWidgets.QPushButton(self.groupBox)
        self.cha7.setGeometry(QtCore.QRect(30, 300, 81, 81))
        self.cha7.setText("")
        self.cha7.setObjectName("cha7")
        self.more = QtWidgets.QPushButton(self.groupBox)
        self.more.setGeometry(QtCore.QRect(140, 300, 81, 81))
        self.more.setText("")
        self.more.setObjectName("more")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 110, 251, 221))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.progressBar = QtWidgets.QProgressBar(self.groupBox_2)
        self.progressBar.setGeometry(QtCore.QRect(90, 190, 151, 5))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.progressBar.setFont(font)
        self.progressBar.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.progressBar.setProperty("value", 70)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(90, 110, 131, 22))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(70, 60, 161, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(130, 160, 41, 22))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(40, 110, 31, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(40, 60, 31, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(40, 160, 31, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.groupBox_2.raise_()
        self.tabWidget.raise_()
        self.pushButton.raise_()
        self.line.raise_()
        self.label.raise_()
        self.groupBox.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1408, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_3 = QtWidgets.QMenu(self.menu)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menu)
        self.menu_4.setObjectName("menu_4")
        MainWindow.setMenuBar(self.menubar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_GPT = QtWidgets.QAction(MainWindow)
        self.action_GPT.setObjectName("action_GPT")
        self.actionV_1_0_0 = QtWidgets.QAction(MainWindow)
        self.actionV_1_0_0.setObjectName("actionV_1_0_0")
        self.actionli_ji_dong_sjtu_edu_cn = QtWidgets.QAction(MainWindow)
        self.actionli_ji_dong_sjtu_edu_cn.setObjectName("actionli_ji_dong_sjtu_edu_cn")
        self.menu_3.addAction(self.actionV_1_0_0)
        self.menu_4.addAction(self.actionli_ji_dong_sjtu_edu_cn)
        self.menu.addAction(self.menu_3.menuAction())
        self.menu.addAction(self.menu_4.menuAction())
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.pushButton_2.clicked.connect(MainWindow.Query)
        self.pushButton.clicked.connect(MainWindow.EditInfo)
        self.pushButton_4.clicked.connect(MainWindow.Query2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Galaxy Findie"))
        self.pushButton.setText(_translate("MainWindow", "修改信息"))
        self.pushButton_2.setText(_translate("MainWindow", "发送"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "数据库机器人"))
        self.pushButton_4.setText(_translate("MainWindow", "发送"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "ChatGPT"))
        self.groupBox.setTitle(_translate("MainWindow", "常用角色"))
        self.label_7.setText(_translate("MainWindow", "54749110"))
        self.label_6.setText(_translate("MainWindow", "小白"))
        self.label_8.setText(_translate("MainWindow", "55"))
        self.menu.setTitle(_translate("MainWindow", "帮助"))
        self.menu_3.setTitle(_translate("MainWindow", "软件版本"))
        self.menu_4.setTitle(_translate("MainWindow", "联系我们"))
        self.action.setText(_translate("MainWindow", "导出Robot查询记录"))
        self.action_2.setText(_translate("MainWindow", "更改账户信息"))
        self.action_GPT.setText(_translate("MainWindow", "导出GPT查询内容"))
        self.actionV_1_0_0.setText(_translate("MainWindow", "V 1.0.0"))
        self.actionli_ji_dong_sjtu_edu_cn.setText(_translate("MainWindow", "li.ji.dong@sjtu.edu.cn"))
