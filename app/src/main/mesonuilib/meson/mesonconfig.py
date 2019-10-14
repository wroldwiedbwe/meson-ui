#!/user/bin/env python3
###################################################################################
#                                                                                 #
# NAME: mesonconfig.py                                                            #
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

from .imesoncomponent import InterfaceMesonComponent


class MesonConfig(InterfaceMesonComponent):
    def __init__(self, project = None, process: QProcess = None):
        self._process: QProcess = process
        self._project = project
        super().__init__(project=self._project)
    # end of method

    def configure(self, args: list):
        meson_args: list = ['configure', self._project.get_build()]
        meson_args.extend(args)
        self._run(meson_args)
    # end of method

    def _run(self, args: list) -> None:
        self._process.waitForFinished()
        self._process.start('meson', args)
        self._process.waitForFinished()
    # end of method
