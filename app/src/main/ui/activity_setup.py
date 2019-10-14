# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app/src/res/layout/activity_setup.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SetupDialog(object):
    def setupUi(self, SetupDialog):
        SetupDialog.setObjectName("SetupDialog")
        SetupDialog.resize(715, 364)
        SetupDialog.setStyleSheet("background-color: rgb(41, 41, 49);")
        self.layoutWidget = QtWidgets.QWidget(SetupDialog)
        self.layoutWidget.setGeometry(QtCore.QRect(158, 10, 531, 118))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_curr_source = QtWidgets.QLabel(self.layoutWidget)
        self.label_curr_source.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 15pt \"Gill Sans\"")
        self.label_curr_source.setObjectName("label_curr_source")
        self.verticalLayout_5.addWidget(self.label_curr_source)
        self.curr_source_dir = QtWidgets.QLineEdit(self.layoutWidget)
        self.curr_source_dir.setStyleSheet("QLineEdit {\n"
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
        self.curr_source_dir.setObjectName("curr_source_dir")
        self.verticalLayout_5.addWidget(self.curr_source_dir)
        self.verticalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lable_curr_build = QtWidgets.QLabel(self.layoutWidget)
        self.lable_curr_build.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 15pt \"Gill Sans\"")
        self.lable_curr_build.setObjectName("lable_curr_build")
        self.verticalLayout_6.addWidget(self.lable_curr_build)
        self.curr_build_dir = QtWidgets.QLineEdit(self.layoutWidget)
        self.curr_build_dir.setStyleSheet("QLineEdit {\n"
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
        self.curr_build_dir.setObjectName("curr_build_dir")
        self.verticalLayout_6.addWidget(self.curr_build_dir)
        self.verticalLayout_4.addLayout(self.verticalLayout_6)
        self.label_logo = QtWidgets.QLabel(SetupDialog)
        self.label_logo.setGeometry(QtCore.QRect(30, 21, 81, 81))
        self.label_logo.setStyleSheet("QLineEdit {\n"
"    url(:/icons/icons/ic_app.png)\n"
"}")
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap(":/ic_res/icons/ic_app.png"))
        self.label_logo.setScaledContents(True)
        self.label_logo.setObjectName("label_logo")
        self.layoutWidget1 = QtWidgets.QWidget(SetupDialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(120, 300, 471, 39))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.push_not_yet = QtWidgets.QPushButton(self.layoutWidget1)
        self.push_not_yet.setStyleSheet("QPushButton {\n"
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
        self.push_not_yet.setObjectName("push_not_yet")
        self.horizontalLayout_2.addWidget(self.push_not_yet)
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
        self.horizontalLayout_2.addWidget(self.push_setup)
        self.layoutWidget2 = QtWidgets.QWidget(SetupDialog)
        self.layoutWidget2.setGeometry(QtCore.QRect(31, 130, 658, 151))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 15pt \"Gill Sans\"")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_7.addWidget(self.label_2)
        self.combo_box_backend = QtWidgets.QComboBox(self.layoutWidget2)
        self.combo_box_backend.setStyleSheet("QComboBox {\n"
"    background-color: white;\n"
"    selection-color: rgb(34, 255, 12);\n"
"    color: rgb(28, 170, 2);\n"
"    border-width: 5px;\n"
"    border-radius: 10px;\n"
"    border: 2px solid gray;\n"
"    padding: 1px 10px 1px 50px;\n"
"    min-width: 6em;\n"
"    font: 13pt \"Gill Sans\";\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"/* shift the arrow when popup is open */\n"
"QComboBox::down-arrow:on {\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    url(:/ic_res/icons/down_arrow.png)\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}")
        self.combo_box_backend.setObjectName("combo_box_backend")
        self.combo_box_backend.addItem("")
        self.combo_box_backend.addItem("")
        self.combo_box_backend.addItem("")
        self.combo_box_backend.addItem("")
        self.combo_box_backend.addItem("")
        self.combo_box_backend.addItem("")
        self.verticalLayout_7.addWidget(self.combo_box_backend)
        self.horizontalLayout.addLayout(self.verticalLayout_7)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 15pt \"Gill Sans\"")
        self.label_10.setObjectName("label_10")
        self.verticalLayout_13.addWidget(self.label_10)
        self.combo_box_buildtype = QtWidgets.QComboBox(self.layoutWidget2)
        self.combo_box_buildtype.setStyleSheet("QComboBox {\n"
"    background-color: white;\n"
"    selection-color: rgb(34, 255, 12);\n"
"    color: rgb(28, 170, 2);\n"
"    border-width: 5px;\n"
"    border-radius: 10px;\n"
"    border: 2px solid gray;\n"
"    padding: 1px 10px 1px 50px;\n"
"    min-width: 6em;\n"
"    font: 13pt \"Gill Sans\";\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"/* shift the arrow when popup is open */\n"
"QComboBox::down-arrow:on {\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    url(:/ic_res/icons/down_arrow.png)\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}")
        self.combo_box_buildtype.setObjectName("combo_box_buildtype")
        self.combo_box_buildtype.addItem("")
        self.combo_box_buildtype.addItem("")
        self.combo_box_buildtype.addItem("")
        self.combo_box_buildtype.addItem("")
        self.combo_box_buildtype.addItem("")
        self.combo_box_buildtype.addItem("")
        self.verticalLayout_13.addWidget(self.combo_box_buildtype)
        self.horizontalLayout.addLayout(self.verticalLayout_13)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget2)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 15pt \"Gill Sans\"")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.combo_box_optimization = QtWidgets.QComboBox(self.layoutWidget2)
        self.combo_box_optimization.setStyleSheet("QComboBox {\n"
"    background-color: white;\n"
"    selection-color: rgb(34, 255, 12);\n"
"    color: rgb(28, 170, 2);\n"
"    border-width: 5px;\n"
"    border-radius: 10px;\n"
"    border: 2px solid gray;\n"
"    padding: 1px 10px 1px 50px;\n"
"    min-width: 6em;\n"
"    font: 13pt \"Gill Sans\";\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"/* shift the arrow when popup is open */\n"
"QComboBox::down-arrow:on {\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    url(:/ic_res/icons/down_arrow.png)\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}")
        self.combo_box_optimization.setObjectName("combo_box_optimization")
        self.combo_box_optimization.addItem("")
        self.combo_box_optimization.addItem("")
        self.combo_box_optimization.addItem("")
        self.combo_box_optimization.addItem("")
        self.combo_box_optimization.addItem("")
        self.combo_box_optimization.addItem("")
        self.verticalLayout.addWidget(self.combo_box_optimization)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_11.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 15pt \"Gill Sans\"")
        self.label_8.setObjectName("label_8")
        self.verticalLayout_10.addWidget(self.label_8)
        self.combo_box_werror = QtWidgets.QComboBox(self.layoutWidget2)
        self.combo_box_werror.setStyleSheet("QComboBox {\n"
"    background-color: white;\n"
"    selection-color: rgb(34, 255, 12);\n"
"    color: rgb(28, 170, 2);\n"
"    border-width: 5px;\n"
"    border-radius: 10px;\n"
"    border: 2px solid gray;\n"
"    padding: 1px 10px 1px 50px;\n"
"    min-width: 6em;\n"
"    font: 13pt \"Gill Sans\";\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"/* shift the arrow when popup is open */\n"
"QComboBox::down-arrow:on {\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    url(:/ic_res/icons/down_arrow.png)\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}")
        self.combo_box_werror.setObjectName("combo_box_werror")
        self.combo_box_werror.addItem("")
        self.combo_box_werror.addItem("")
        self.verticalLayout_10.addWidget(self.combo_box_werror)
        self.horizontalLayout_3.addLayout(self.verticalLayout_10)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 15pt \"Gill Sans\"")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_8.addWidget(self.label_6)
        self.combo_box_warning = QtWidgets.QComboBox(self.layoutWidget2)
        self.combo_box_warning.setStyleSheet("QComboBox {\n"
"    background-color: white;\n"
"    selection-color: rgb(34, 255, 12);\n"
"    color: rgb(28, 170, 2);\n"
"    border-width: 5px;\n"
"    border-radius: 10px;\n"
"    border: 2px solid gray;\n"
"    padding: 1px 10px 1px 50px;\n"
"    min-width: 6em;\n"
"    font: 13pt \"Gill Sans\";\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"/* shift the arrow when popup is open */\n"
"QComboBox::down-arrow:on {\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    url(:/ic_res/icons/down_arrow.png)\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}")
        self.combo_box_warning.setObjectName("combo_box_warning")
        self.combo_box_warning.addItem("")
        self.combo_box_warning.addItem("")
        self.combo_box_warning.addItem("")
        self.combo_box_warning.addItem("")
        self.verticalLayout_8.addWidget(self.combo_box_warning)
        self.horizontalLayout_3.addLayout(self.verticalLayout_8)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_layout = QtWidgets.QLabel(self.layoutWidget2)
        self.label_layout.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 15pt \"Gill Sans\"")
        self.label_layout.setObjectName("label_layout")
        self.verticalLayout_9.addWidget(self.label_layout)
        self.combo_box_layout = QtWidgets.QComboBox(self.layoutWidget2)
        self.combo_box_layout.setStyleSheet("QComboBox {\n"
"    background-color: white;\n"
"    selection-color: rgb(34, 255, 12);\n"
"    color: rgb(28, 170, 2);\n"
"    border-width: 5px;\n"
"    border-radius: 10px;\n"
"    border: 2px solid gray;\n"
"    padding: 1px 10px 1px 50px;\n"
"    min-width: 6em;\n"
"    font: 13pt \"Gill Sans\";\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"/* shift the arrow when popup is open */\n"
"QComboBox::down-arrow:on {\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    url(:/ic_res/icons/down_arrow.png)\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}")
        self.combo_box_layout.setObjectName("combo_box_layout")
        self.combo_box_layout.addItem("")
        self.combo_box_layout.addItem("")
        self.verticalLayout_9.addWidget(self.combo_box_layout)
        self.horizontalLayout_3.addLayout(self.verticalLayout_9)
        self.verticalLayout_11.addLayout(self.horizontalLayout_3)

        self.retranslateUi(SetupDialog)
        QtCore.QMetaObject.connectSlotsByName(SetupDialog)

    def retranslateUi(self, SetupDialog):
        _translate = QtCore.QCoreApplication.translate
        SetupDialog.setWindowTitle(_translate("SetupDialog", "Setup dialog"))
        self.label_curr_source.setText(_translate("SetupDialog", "Source directory:"))
        self.lable_curr_build.setText(_translate("SetupDialog", "Build directory:"))
        self.push_not_yet.setText(_translate("SetupDialog", "Not yet"))
        self.push_setup.setText(_translate("SetupDialog", "Setup project"))
        self.label_2.setText(_translate("SetupDialog", "Backend:"))
        self.combo_box_backend.setItemText(0, _translate("SetupDialog", "Ninja build"))
        self.combo_box_backend.setItemText(1, _translate("SetupDialog", "Xcode"))
        self.combo_box_backend.setItemText(2, _translate("SetupDialog", "Visual Studio 2010"))
        self.combo_box_backend.setItemText(3, _translate("SetupDialog", "Visual Studio 2015"))
        self.combo_box_backend.setItemText(4, _translate("SetupDialog", "Visual Studio 2017"))
        self.combo_box_backend.setItemText(5, _translate("SetupDialog", "Visual Studio 2019"))
        self.label_10.setText(_translate("SetupDialog", "buildtype:"))
        self.combo_box_buildtype.setItemText(0, _translate("SetupDialog", "debug"))
        self.combo_box_buildtype.setItemText(1, _translate("SetupDialog", "debugoptimized"))
        self.combo_box_buildtype.setItemText(2, _translate("SetupDialog", "release"))
        self.combo_box_buildtype.setItemText(3, _translate("SetupDialog", "plain"))
        self.combo_box_buildtype.setItemText(4, _translate("SetupDialog", "minsize"))
        self.combo_box_buildtype.setItemText(5, _translate("SetupDialog", "custom"))
        self.label.setText(_translate("SetupDialog", "optimization:"))
        self.combo_box_optimization.setItemText(0, _translate("SetupDialog", "0"))
        self.combo_box_optimization.setItemText(1, _translate("SetupDialog", "g"))
        self.combo_box_optimization.setItemText(2, _translate("SetupDialog", "1"))
        self.combo_box_optimization.setItemText(3, _translate("SetupDialog", "2"))
        self.combo_box_optimization.setItemText(4, _translate("SetupDialog", "3"))
        self.combo_box_optimization.setItemText(5, _translate("SetupDialog", "s"))
        self.label_8.setText(_translate("SetupDialog", "werror:"))
        self.combo_box_werror.setItemText(0, _translate("SetupDialog", "false"))
        self.combo_box_werror.setItemText(1, _translate("SetupDialog", "true"))
        self.label_6.setText(_translate("SetupDialog", "warning_level:"))
        self.combo_box_warning.setItemText(0, _translate("SetupDialog", "0"))
        self.combo_box_warning.setItemText(1, _translate("SetupDialog", "1"))
        self.combo_box_warning.setItemText(2, _translate("SetupDialog", "2"))
        self.combo_box_warning.setItemText(3, _translate("SetupDialog", "3"))
        self.label_layout.setText(_translate("SetupDialog", "layout:"))
        self.combo_box_layout.setItemText(0, _translate("SetupDialog", "mirror"))
        self.combo_box_layout.setItemText(1, _translate("SetupDialog", "flat"))
from . import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SetupDialog = QtWidgets.QDialog()
    ui = Ui_SetupDialog()
    ui.setupUi(SetupDialog)
    SetupDialog.show()
    sys.exit(app.exec_())
