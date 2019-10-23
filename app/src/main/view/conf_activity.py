#!/user/bin/env python3
###################################################################################
#                                                                                 #
# NAME: conf_activity.py                                                          #
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
from ..ui.activity_conf import Ui_ConfDialog


class ConfigureActivity(QMainWindow, Ui_ConfDialog):
    def __init__(self):
        super(QMainWindow, self).__init__()
        super(Ui_ConfDialog, self).__init__()
        self.setupUi(self)
        
        self.setFixedSize(730, 464)
