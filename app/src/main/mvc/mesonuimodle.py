#!/user/bin/env python3
###################################################################################
#                                                                                 #
# NAME: mesonuimodle.py                                                           #
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
from ..mesonuilib.meson.mesonmanager import Meson
from PyQt5.QtCore import QObject
from PyQt5.QtCore import pyqtSignal


class MesonUiModule(QObject):
    meson_source_dir_changed = pyqtSignal(str)
    meson_build_dir_changed = pyqtSignal(str)
    meson_build_script_changed = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self._meson_project_build = ''
        self._meson_project_src = ''
        self._meson_build_script = ''
    # end of method
    
    def get_script(self) -> str:
        return self._meson_build_script
    # end of method

    def set_script(self, value: str) -> None:
        self._meson_build_script = value
        self.meson_build_script_changed.emit(value)
    # end of method

    def get_build(self) -> str:
        return self._meson_project_build
    # end of method

    def set_build(self, value: str) -> None:
        self._meson_project_build = value
        self.meson_build_dir_changed.emit(value)
    # end of method

    def get_source(self) -> str:
        return self._meson_project_src
    # end of method

    def set_source(self, value: str) -> None:
        self._meson_project_src = value
        self.meson_source_dir_changed.emit(value)
    # end of method
