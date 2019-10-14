# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app/src/res/layout/activity_main.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(41, 41, 49);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_logo = QtWidgets.QLabel(self.centralwidget)
        self.label_logo.setGeometry(QtCore.QRect(30, 34, 81, 81))
        self.label_logo.setStyleSheet("QLineEdit {\n"
"    url(:/icons/icons/ic_app.png)\n"
"}")
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap(":/ic_res/icons/ic_app.png"))
        self.label_logo.setScaledContents(True)
        self.label_logo.setObjectName("label_logo")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(130, 30, 571, 118))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_source = QtWidgets.QLabel(self.layoutWidget)
        self.label_source.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 15pt \"Gill Sans\"")
        self.label_source.setObjectName("label_source")
        self.verticalLayout_2.addWidget(self.label_source)
        self.source_dir = QtWidgets.QLineEdit(self.layoutWidget)
        self.source_dir.setStyleSheet("QLineEdit {\n"
"    border-width: 5px;\n"
"    border-radius: 15px;\n"
"    font: 13pt \"Gill Sans\";\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 2 10px;\n"
"    background: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"    selection-background-color: rgb(233, 233, 233);\n"
"}")
        self.source_dir.setObjectName("source_dir")
        self.verticalLayout_2.addWidget(self.source_dir)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lable_build = QtWidgets.QLabel(self.layoutWidget)
        self.lable_build.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 15pt \"Gill Sans\"")
        self.lable_build.setObjectName("lable_build")
        self.verticalLayout_3.addWidget(self.lable_build)
        self.build_dir = QtWidgets.QLineEdit(self.layoutWidget)
        self.build_dir.setStyleSheet("QLineEdit {\n"
"    border-width: 5px;\n"
"    border-radius: 15px;\n"
"    font: 13pt \"Gill Sans\";\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 2 10px;\n"
"    background: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"    selection-background-color: rgb(233, 233, 233);\n"
"}")
        self.build_dir.setObjectName("build_dir")
        self.verticalLayout_3.addWidget(self.build_dir)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.push_open = QtWidgets.QPushButton(self.centralwidget)
        self.push_open.setGeometry(QtCore.QRect(722, 53, 36, 30))
        self.push_open.setStyleSheet("QPushButton {\n"
"    background-color: rgb(105, 105, 105);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(127, 127, 127);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 13pt \"Gill Sans\";\n"
"    min-width: 2em;\n"
"    padding: 1px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(127, 127, 127);\n"
"    border-style: inset;\n"
"    color: rgb(36, 255, 6);\n"
"}")
        self.push_open.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ic_res/icons/open_dir.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.push_open.setIcon(icon)
        self.push_open.setObjectName("push_open")
        self.mesonui_output_console = QtWidgets.QTextEdit(self.centralwidget)
        self.mesonui_output_console.setGeometry(QtCore.QRect(38, 230, 721, 301))
        self.mesonui_output_console.setStyleSheet("QTextEdit {\n"
"    background-attachment: scroll;\n"
"    background-color: rgb(63, 63, 63);\n"
"    border-color: rgb(245, 251, 251);\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    padding: 6px;\n"
"    color: rgb(63, 255, 6);\n"
"    font: 13pt \"Monaco\";\n"
"}")
        self.mesonui_output_console.setReadOnly(True)
        self.mesonui_output_console.setObjectName("mesonui_output_console")
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(40, 170, 721, 51))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.push_setup = QtWidgets.QPushButton(self.layoutWidget1)
        self.push_setup.setStyleSheet("QPushButton {\n"
"    background-color: rgb(105, 105, 105);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(127, 127, 127);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 13pt \"Gill Sans\";\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(127, 127, 127);\n"
"    border-style: inset;\n"
"    color: rgb(36, 255, 6);\n"
"}")
        self.push_setup.setObjectName("push_setup")
        self.horizontalLayout.addWidget(self.push_setup)
        self.push_build = QtWidgets.QPushButton(self.layoutWidget1)
        self.push_build.setStyleSheet("QPushButton {\n"
"    background-color: rgb(105, 105, 105);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(127, 127, 127);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 13pt \"Gill Sans\";\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(127, 127, 127);\n"
"    border-style: inset;\n"
"    color: rgb(36, 255, 6);\n"
"}")
        self.push_build.setObjectName("push_build")
        self.horizontalLayout.addWidget(self.push_build)
        self.push_tests = QtWidgets.QPushButton(self.layoutWidget1)
        self.push_tests.setStyleSheet("QPushButton {\n"
"    background-color: rgb(105, 105, 105);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(127, 127, 127);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 13pt \"Gill Sans\";\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(127, 127, 127);\n"
"    border-style: inset;\n"
"    color: rgb(36, 255, 6);\n"
"}")
        self.push_tests.setObjectName("push_tests")
        self.horizontalLayout.addWidget(self.push_tests)
        self.push_install = QtWidgets.QPushButton(self.layoutWidget1)
        self.push_install.setStyleSheet("QPushButton {\n"
"    background-color: rgb(105, 105, 105);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(127, 127, 127);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 13pt \"Gill Sans\";\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(127, 127, 127);\n"
"    border-style: inset;\n"
"    color: rgb(36, 255, 6);\n"
"}")
        self.push_install.setObjectName("push_install")
        self.horizontalLayout.addWidget(self.push_install)
        self.push_clean = QtWidgets.QPushButton(self.centralwidget)
        self.push_clean.setGeometry(QtCore.QRect(593, 540, 166, 31))
        self.push_clean.setStyleSheet("QPushButton {\n"
"    background-color: rgb(105, 105, 105);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(127, 127, 127);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 13pt \"Gill Sans\";\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(127, 127, 127);\n"
"    border-style: inset;\n"
"    color: rgb(36, 255, 6);\n"
"}")
        self.push_clean.setObjectName("push_clean")
        self.push_docs = QtWidgets.QPushButton(self.centralwidget)
        self.push_docs.setGeometry(QtCore.QRect(35, 540, 166, 31))
        self.push_docs.setStyleSheet("QPushButton {\n"
"    background-color: rgb(105, 105, 105);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(127, 127, 127);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 13pt \"Gill Sans\";\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(127, 127, 127);\n"
"    border-style: inset;\n"
"    color: rgb(36, 255, 6);\n"
"}")
        self.push_docs.setObjectName("push_docs")
        self.push_clear = QtWidgets.QPushButton(self.centralwidget)
        self.push_clear.setGeometry(QtCore.QRect(720, 120, 36, 30))
        self.push_clear.setStyleSheet("QPushButton {\n"
"    background-color: rgb(105, 105, 105);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(127, 127, 127);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 13pt \"Gill Sans\";\n"
"    min-width: 2em;\n"
"    padding: 1px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(127, 127, 127);\n"
"    border-style: inset;\n"
"    color: rgb(36, 255, 6);\n"
"}")
        self.push_clear.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/ic_res/icons/clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.push_clear.setIcon(icon1)
        self.push_clear.setObjectName("push_clear")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuMeson_ui = QtWidgets.QMenu(self.menuBar)
        self.menuMeson_ui.setObjectName("menuMeson_ui")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menuBar)
        self.actionMeson_docs = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/ic_res/icons/ic_docs.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMeson_docs.setIcon(icon2)
        self.actionMeson_docs.setObjectName("actionMeson_docs")
        self.actionMeson_QnA = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/ic_res/icons/qna_ic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMeson_QnA.setIcon(icon3)
        self.actionMeson_QnA.setObjectName("actionMeson_QnA")
        self.actionMeson_ui_issue = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/ic_res/icons/github_ic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMeson_ui_issue.setIcon(icon4)
        self.actionMeson_ui_issue.setObjectName("actionMeson_ui_issue")
        self.actionMeson_issue = QtWidgets.QAction(MainWindow)
        self.actionMeson_issue.setIcon(icon4)
        self.actionMeson_issue.setObjectName("actionMeson_issue")
        self.actionAbout_Meson_ui = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/ic_res/icons/info_ic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout_Meson_ui.setIcon(icon5)
        self.actionAbout_Meson_ui.setObjectName("actionAbout_Meson_ui")
        self.actionQuit_Meson_ui = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/ic_res/icons/quit_ic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit_Meson_ui.setIcon(icon6)
        self.actionQuit_Meson_ui.setObjectName("actionQuit_Meson_ui")
        self.actionOpen_folder = QtWidgets.QAction(MainWindow)
        self.actionOpen_folder.setIcon(icon)
        self.actionOpen_folder.setObjectName("actionOpen_folder")
        self.menuMeson_ui.addAction(self.actionAbout_Meson_ui)
        self.menuMeson_ui.addAction(self.actionOpen_folder)
        self.menuMeson_ui.addAction(self.actionQuit_Meson_ui)
        self.menuHelp.addAction(self.actionMeson_docs)
        self.menuHelp.addAction(self.actionMeson_QnA)
        self.menuHelp.addAction(self.actionMeson_ui_issue)
        self.menuHelp.addAction(self.actionMeson_issue)
        self.menuBar.addAction(self.menuMeson_ui.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Meson-ui"))
        self.label_source.setText(_translate("MainWindow", "Source directory:"))
        self.lable_build.setText(_translate("MainWindow", "Build directory:"))
        self.push_setup.setText(_translate("MainWindow", "Setup project"))
        self.push_build.setText(_translate("MainWindow", "Build project"))
        self.push_tests.setText(_translate("MainWindow", "Test project"))
        self.push_install.setText(_translate("MainWindow", "Install project"))
        self.push_clean.setText(_translate("MainWindow", "Clean project"))
        self.push_docs.setText(_translate("MainWindow", "Meson docs"))
        self.menuMeson_ui.setTitle(_translate("MainWindow", "Meson-ui"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionMeson_docs.setText(_translate("MainWindow", "Meson docs"))
        self.actionMeson_QnA.setText(_translate("MainWindow", "Meson QnA"))
        self.actionMeson_ui_issue.setText(_translate("MainWindow", "Meson-ui issue"))
        self.actionMeson_issue.setText(_translate("MainWindow", "Meson issue"))
        self.actionAbout_Meson_ui.setText(_translate("MainWindow", "Info Meson-ui"))
        self.actionQuit_Meson_ui.setText(_translate("MainWindow", "Exit Meson-ui"))
        self.actionOpen_folder.setText(_translate("MainWindow", "Open folder"))
from . import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
