#!/user/bin/env python3
###################################################################################
#                                                                                 #
# NAME: imesoncomponent.py                                                        #
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
from PyQt5.QtCore import QProcess
import subprocess
import os
import json


class InterfaceMesonComponent:
    def __init__(self, project = None, process: QProcess = None):
        self._project = project
    # end of method

    def message(self, message: str):
        print(f'[ Message ]: {message}')
    # end of method

    def error(self, message: str) -> None:
        raise RuntimeError(f'Meson Component Error: {message}')
    # end of method
