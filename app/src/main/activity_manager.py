#!/user/bin/env python3
###################################################################################
#                                                                                 #
# NAME: activity_manager.py                                                       #
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
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QFileInfo
from PyQt5.QtCore import QFile

from .view import main_activity


class MesonUi(QApplication):
    def __init__(self, sys_argv):
        super(self.__class__, self).__init__(sys_argv)
        self.main_view = main_activity.MainActivity()
        self.main_view.show()
    # end of method