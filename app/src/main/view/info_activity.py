#!/user/bin/env python3
###################################################################################
#                                                                                 #
# NAME: info_activity.py                                                          #
#                                                                                 #
# AUTHOR: Michael Brockus.                                                        #
#                                                                                 #
# CONTACT: <mailto:michael@squidfarts.com>                                        #
#                                                                                 #
# NOTICES:                                                                        #
#                                                                                 #
# License: Apache 2.0 :http://www.apache.org/licenses/LICENSE-2.0                 #
#                                                                                 #
###################################################################################
from PyQt5.QtWidgets import QMainWindow
from ..ui.activity_info import Ui_InfoDialog


class InfoActivity(QMainWindow, Ui_InfoDialog):
    def __init__(self):
        super(QMainWindow, self).__init__()
        super(Ui_InfoDialog, self).__init__()
        self.setupUi(self)

        self.plainTextEdit.setReadOnly(True)
        self.setFixedSize(566, 421)
        self.push_ok.clicked.connect(lambda: self.onclick_ok_close())

    def onclick_ok_close(self):
        self.close()