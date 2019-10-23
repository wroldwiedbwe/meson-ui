# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app/src/res/layout/activity_conf.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ConfDialog(object):
    def setupUi(self, ConfDialog):
        ConfDialog.setObjectName("ConfDialog")
        ConfDialog.resize(731, 459)
        ConfDialog.setStyleSheet("background-color: rgb(41, 41, 49);")
        self.layoutWidget = QtWidgets.QWidget(ConfDialog)
        self.layoutWidget.setGeometry(QtCore.QRect(120, 410, 481, 39))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(34)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.push_not_yet = QtWidgets.QPushButton(self.layoutWidget)
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
        self.push_setup = QtWidgets.QPushButton(self.layoutWidget)
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
        self.groupBox_2 = QtWidgets.QGroupBox(ConfDialog)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 159, 731, 231))
        self.groupBox_2.setAutoFillBackground(False)
        self.groupBox_2.setStyleSheet("QGroupBox {\n"
"    background-color: rgb(113, 113, 113);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    border-radius: 10px;\n"
"    border: 2px solid gray;\n"
"    padding: 0 50px;\n"
"    background-color: rgb(141, 141, 141);\n"
"}")
        self.groupBox_2.setObjectName("groupBox_2")
        self.frame_10 = QtWidgets.QFrame(self.groupBox_2)
        self.frame_10.setGeometry(QtCore.QRect(372, 30, 331, 201))
        self.frame_10.setStyleSheet("background-color: rgb(113, 113, 113);")
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.label_layout_5 = QtWidgets.QLabel(self.frame_10)
        self.label_layout_5.setStyleSheet("background-color: rgb(113, 113, 113);\n"
"color: rgb(255, 255, 255);\n"
"font: 15pt \"Gill Sans\"")
        self.label_layout_5.setObjectName("label_layout_5")
        self.horizontalLayout_26.addWidget(self.label_layout_5)
        self.combo_box_layout_5 = QtWidgets.QComboBox(self.frame_10)
        self.combo_box_layout_5.setStyleSheet("QComboBox {\n"
"    background-color: white;\n"
"    selection-color: rgb(34, 255, 12);\n"
"    color: rgb(28, 170, 2);\n"
"    border-width: 5px;\n"
"    border-radius: 10px;\n"
"    border: 2px solid gray;\n"
"    padding: 1px 10px 1px 50px;\n"
"    min-width: 10em;\n"
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
        self.combo_box_layout_5.setObjectName("combo_box_layout_5")
        self.combo_box_layout_5.addItem("")
        self.combo_box_layout_5.addItem("")
        self.horizontalLayout_26.addWidget(self.combo_box_layout_5)
        self.verticalLayout_7.addLayout(self.horizontalLayout_26)
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.label_17 = QtWidgets.QLabel(self.frame_10)
        self.label_17.setStyleSheet("background-color: rgb(113, 113, 113);\n"
"color: rgb(255, 255, 255);\n"
"font: 15pt \"Gill Sans\"")
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_27.addWidget(self.label_17)
        self.combo_box_warning_5 = QtWidgets.QComboBox(self.frame_10)
        self.combo_box_warning_5.setStyleSheet("QComboBox {\n"
"    background-color: white;\n"
"    selection-color: rgb(34, 255, 12);\n"
"    color: rgb(28, 170, 2);\n"
"    border-width: 5px;\n"
"    border-radius: 10px;\n"
"    border: 2px solid gray;\n"
"    padding: 1px 10px 1px 50px;\n"
"    min-width: 10em;\n"
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
        self.combo_box_warning_5.setObjectName("combo_box_warning_5")
        self.combo_box_warning_5.addItem("")
        self.combo_box_warning_5.addItem("")
        self.combo_box_warning_5.addItem("")
        self.horizontalLayout_27.addWidget(self.combo_box_warning_5)
        self.verticalLayout_7.addLayout(self.horizontalLayout_27)
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.label_4 = QtWidgets.QLabel(self.frame_10)
        self.label_4.setStyleSheet("background-color: rgb(113, 113, 113);\n"
"color: rgb(255, 255, 255);\n"
"font: 15pt \"Gill Sans\"")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_28.addWidget(self.label_4)
        self.combo_box_optimization_2 = QtWidgets.QComboBox(self.frame_10)
        self.combo_box_optimization_2.setStyleSheet("QComboBox {\n"
"    background-color: white;\n"
"    selection-color: rgb(34, 255, 12);\n"
"    color: rgb(28, 170, 2);\n"
"    border-width: 5px;\n"
"    border-radius: 10px;\n"
"    border: 2px solid gray;\n"
"    padding: 1px 10px 1px 50px;\n"
"    min-width: 10em;\n"
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
        self.combo_box_optimization_2.setObjectName("combo_box_optimization_2")
        self.combo_box_optimization_2.addItem("")
        self.combo_box_optimization_2.addItem("")
        self.horizontalLayout_28.addWidget(self.combo_box_optimization_2)
        self.verticalLayout_7.addLayout(self.horizontalLayout_28)
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.label_18 = QtWidgets.QLabel(self.frame_10)
        self.label_18.setStyleSheet("background-color: rgb(113, 113, 113);\n"
"color: rgb(255, 255, 255);\n"
"font: 15pt \"Gill Sans\"")
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_29.addWidget(self.label_18)
        self.combo_box_werror_6 = QtWidgets.QComboBox(self.frame_10)
        self.combo_box_werror_6.setStyleSheet("QComboBox {\n"
"    background-color: white;\n"
"    selection-color: rgb(34, 255, 12);\n"
"    color: rgb(28, 170, 2);\n"
"    border-width: 5px;\n"
"    border-radius: 10px;\n"
"    border: 2px solid gray;\n"
"    padding: 1px 10px 1px 50px;\n"
"    min-width: 10em;\n"
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
        self.combo_box_werror_6.setObjectName("combo_box_werror_6")
        self.combo_box_werror_6.addItem("")
        self.combo_box_werror_6.addItem("")
        self.combo_box_werror_6.addItem("")
        self.horizontalLayout_29.addWidget(self.combo_box_werror_6)
        self.verticalLayout_7.addLayout(self.horizontalLayout_29)
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.label_19 = QtWidgets.QLabel(self.frame_10)
        self.label_19.setStyleSheet("background-color: rgb(113, 113, 113);\n"
"color: rgb(255, 255, 255);\n"
"font: 15pt \"Gill Sans\"")
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_30.addWidget(self.label_19)
        self.combo_box_werror_7 = QtWidgets.QComboBox(self.frame_10)
        self.combo_box_werror_7.setStyleSheet("QComboBox {\n"
"    background-color: white;\n"
"    selection-color: rgb(34, 255, 12);\n"
"    color: rgb(28, 170, 2);\n"
"    border-width: 5px;\n"
"    border-radius: 10px;\n"
"    border: 2px solid gray;\n"
"    padding: 1px 10px 1px 50px;\n"
"    min-width: 10em;\n"
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
        self.combo_box_werror_7.setObjectName("combo_box_werror_7")
        self.combo_box_werror_7.addItem("")
        self.combo_box_werror_7.addItem("")
        self.combo_box_werror_7.addItem("")
        self.combo_box_werror_7.addItem("")
        self.combo_box_werror_7.addItem("")
        self.combo_box_werror_7.addItem("")
        self.horizontalLayout_30.addWidget(self.combo_box_werror_7)
        self.verticalLayout_7.addLayout(self.horizontalLayout_30)
        self.frame_9 = QtWidgets.QFrame(self.groupBox_2)
        self.frame_9.setGeometry(QtCore.QRect(10, 30, 341, 201))
        self.frame_9.setStyleSheet("background-color: rgb(113, 113, 113);")
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.label_layout_4 = QtWidgets.QLabel(self.frame_9)
        self.label_layout_4.setStyleSheet("background-color: rgb(113, 113, 113);\n"
"color: rgb(255, 255, 255);\n"
"font: 15pt \"Gill Sans\"")
        self.label_layout_4.setObjectName("label_layout_4")
        self.horizontalLayout_21.addWidget(self.label_layout_4)
        self.combo_box_layout_4 = QtWidgets.QComboBox(self.frame_9)
        self.combo_box_layout_4.setStyleSheet("QComboBox {\n"
"    background-color: white;\n"
"    selection-color: rgb(34, 255, 12);\n"
"    color: rgb(28, 170, 2);\n"
"    border-width: 5px;\n"
"    border-radius: 10px;\n"
"    border: 2px solid gray;\n"
"    padding: 1px 10px 1px 50px;\n"
"    min-width: 10em;\n"
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
        self.combo_box_layout_4.setObjectName("combo_box_layout_4")
        self.combo_box_layout_4.addItem("")
        self.combo_box_layout_4.addItem("")
        self.horizontalLayout_21.addWidget(self.combo_box_layout_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_21)
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.label_3 = QtWidgets.QLabel(self.frame_9)
        self.label_3.setStyleSheet("background-color: rgb(113, 113, 113);\n"
"color: rgb(255, 255, 255);\n"
"font: 15pt \"Gill Sans\"")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_22.addWidget(self.label_3)
        self.combo_box_backend_2 = QtWidgets.QComboBox(self.frame_9)
        self.combo_box_backend_2.setStyleSheet("QComboBox {\n"
"    background-color: white;\n"
"    selection-color: rgb(34, 255, 12);\n"
"    color: rgb(28, 170, 2);\n"
"    border-width: 5px;\n"
"    border-radius: 10px;\n"
"    border: 2px solid gray;\n"
"    padding: 1px 10px 1px 50px;\n"
"    min-width: 10em;\n"
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
        self.combo_box_backend_2.setObjectName("combo_box_backend_2")
        self.combo_box_backend_2.addItem("")
        self.combo_box_backend_2.addItem("")
        self.combo_box_backend_2.addItem("")
        self.combo_box_backend_2.addItem("")
        self.combo_box_backend_2.addItem("")
        self.combo_box_backend_2.addItem("")
        self.horizontalLayout_22.addWidget(self.combo_box_backend_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_22)
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.label_14 = QtWidgets.QLabel(self.frame_9)
        self.label_14.setStyleSheet("background-color: rgb(113, 113, 113);\n"
"color: rgb(255, 255, 255);\n"
"font: 15pt \"Gill Sans\"")
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_23.addWidget(self.label_14)
        self.combo_box_buildtype_2 = QtWidgets.QComboBox(self.frame_9)
        self.combo_box_buildtype_2.setStyleSheet("QComboBox {\n"
"    background-color: white;\n"
"    selection-color: rgb(34, 255, 12);\n"
"    color: rgb(28, 170, 2);\n"
"    border-width: 5px;\n"
"    border-radius: 10px;\n"
"    border: 2px solid gray;\n"
"    padding: 1px 10px 1px 50px;\n"
"    min-width: 10em;\n"
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
        self.combo_box_buildtype_2.setObjectName("combo_box_buildtype_2")
        self.combo_box_buildtype_2.addItem("")
        self.combo_box_buildtype_2.addItem("")
        self.combo_box_buildtype_2.addItem("")
        self.horizontalLayout_23.addWidget(self.combo_box_buildtype_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_23)
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.label_15 = QtWidgets.QLabel(self.frame_9)
        self.label_15.setStyleSheet("background-color: rgb(113, 113, 113);\n"
"color: rgb(255, 255, 255);\n"
"font: 15pt \"Gill Sans\"")
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_24.addWidget(self.label_15)
        self.combo_box_warning_4 = QtWidgets.QComboBox(self.frame_9)
        self.combo_box_warning_4.setStyleSheet("QComboBox {\n"
"    background-color: white;\n"
"    selection-color: rgb(34, 255, 12);\n"
"    color: rgb(28, 170, 2);\n"
"    border-width: 5px;\n"
"    border-radius: 10px;\n"
"    border: 2px solid gray;\n"
"    padding: 1px 10px 1px 50px;\n"
"    min-width: 10em;\n"
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
        self.combo_box_warning_4.setObjectName("combo_box_warning_4")
        self.combo_box_warning_4.addItem("")
        self.combo_box_warning_4.addItem("")
        self.horizontalLayout_24.addWidget(self.combo_box_warning_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_24)
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.label_16 = QtWidgets.QLabel(self.frame_9)
        self.label_16.setStyleSheet("background-color: rgb(113, 113, 113);\n"
"color: rgb(255, 255, 255);\n"
"font: 15pt \"Gill Sans\"")
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_25.addWidget(self.label_16)
        self.combo_box_werror_5 = QtWidgets.QComboBox(self.frame_9)
        self.combo_box_werror_5.setStyleSheet("QComboBox {\n"
"    background-color: white;\n"
"    selection-color: rgb(34, 255, 12);\n"
"    color: rgb(28, 170, 2);\n"
"    border-width: 5px;\n"
"    border-radius: 10px;\n"
"    border: 2px solid gray;\n"
"    padding: 1px 10px 1px 50px;\n"
"    min-width: 10em;\n"
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
        self.combo_box_werror_5.setObjectName("combo_box_werror_5")
        self.combo_box_werror_5.addItem("")
        self.combo_box_werror_5.addItem("")
        self.horizontalLayout_25.addWidget(self.combo_box_werror_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_25)
        self.label_logo = QtWidgets.QLabel(ConfDialog)
        self.label_logo.setGeometry(QtCore.QRect(30, 20, 81, 81))
        self.label_logo.setStyleSheet("QLineEdit {\n"
"    url(:/icons/icons/ic_app.png)\n"
"}")
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap(":/ic_res/icons/ic_app.png"))
        self.label_logo.setScaledContents(True)
        self.label_logo.setObjectName("label_logo")

        self.retranslateUi(ConfDialog)
        QtCore.QMetaObject.connectSlotsByName(ConfDialog)

    def retranslateUi(self, ConfDialog):
        _translate = QtCore.QCoreApplication.translate
        ConfDialog.setWindowTitle(_translate("ConfDialog", "Configure dialog"))
        self.push_not_yet.setText(_translate("ConfDialog", "Not yet"))
        self.push_setup.setText(_translate("ConfDialog", "Setup project"))
        self.groupBox_2.setTitle(_translate("ConfDialog", "Meson base options:"))
        self.label_layout_5.setText(_translate("ConfDialog", "b_lto:"))
        self.combo_box_layout_5.setItemText(0, _translate("ConfDialog", "false"))
        self.combo_box_layout_5.setItemText(1, _translate("ConfDialog", "true"))
        self.label_17.setText(_translate("ConfDialog", "b_ndebug:"))
        self.combo_box_warning_5.setItemText(0, _translate("ConfDialog", "false"))
        self.combo_box_warning_5.setItemText(1, _translate("ConfDialog", "true"))
        self.combo_box_warning_5.setItemText(2, _translate("ConfDialog", "if-release"))
        self.label_4.setText(_translate("ConfDialog", "b_pch:"))
        self.combo_box_optimization_2.setItemText(0, _translate("ConfDialog", "true"))
        self.combo_box_optimization_2.setItemText(1, _translate("ConfDialog", "false"))
        self.label_18.setText(_translate("ConfDialog", "b_pgo:"))
        self.combo_box_werror_6.setItemText(0, _translate("ConfDialog", "off"))
        self.combo_box_werror_6.setItemText(1, _translate("ConfDialog", "generate"))
        self.combo_box_werror_6.setItemText(2, _translate("ConfDialog", "use"))
        self.label_19.setText(_translate("ConfDialog", "b_sanitize:"))
        self.combo_box_werror_7.setItemText(0, _translate("ConfDialog", "none"))
        self.combo_box_werror_7.setItemText(1, _translate("ConfDialog", "address"))
        self.combo_box_werror_7.setItemText(2, _translate("ConfDialog", "thread"))
        self.combo_box_werror_7.setItemText(3, _translate("ConfDialog", "undefined"))
        self.combo_box_werror_7.setItemText(4, _translate("ConfDialog", "memory"))
        self.combo_box_werror_7.setItemText(5, _translate("ConfDialog", "address,undefined"))
        self.label_layout_4.setText(_translate("ConfDialog", "b_asneeded:"))
        self.combo_box_layout_4.setItemText(0, _translate("ConfDialog", "true"))
        self.combo_box_layout_4.setItemText(1, _translate("ConfDialog", "false"))
        self.label_3.setText(_translate("ConfDialog", "b_staticpic:"))
        self.combo_box_backend_2.setItemText(0, _translate("ConfDialog", "none"))
        self.combo_box_backend_2.setItemText(1, _translate("ConfDialog", "address"))
        self.combo_box_backend_2.setItemText(2, _translate("ConfDialog", "thread"))
        self.combo_box_backend_2.setItemText(3, _translate("ConfDialog", "undefined"))
        self.combo_box_backend_2.setItemText(4, _translate("ConfDialog", "memory"))
        self.combo_box_backend_2.setItemText(5, _translate("ConfDialog", "address,undefined"))
        self.label_14.setText(_translate("ConfDialog", "b_colorout:"))
        self.combo_box_buildtype_2.setItemText(0, _translate("ConfDialog", "always"))
        self.combo_box_buildtype_2.setItemText(1, _translate("ConfDialog", "auto"))
        self.combo_box_buildtype_2.setItemText(2, _translate("ConfDialog", "never"))
        self.label_15.setText(_translate("ConfDialog", "b_coverage:"))
        self.combo_box_warning_4.setItemText(0, _translate("ConfDialog", "false"))
        self.combo_box_warning_4.setItemText(1, _translate("ConfDialog", "true"))
        self.label_16.setText(_translate("ConfDialog", "b_lundef:"))
        self.combo_box_werror_5.setItemText(0, _translate("ConfDialog", "true"))
        self.combo_box_werror_5.setItemText(1, _translate("ConfDialog", "false"))
from . import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ConfDialog = QtWidgets.QDialog()
    ui = Ui_ConfDialog()
    ui.setupUi(ConfDialog)
    ConfDialog.show()
    sys.exit(app.exec_())
