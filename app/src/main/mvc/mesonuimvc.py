#!/user/bin/env python3
###################################################################################
#                                                                                 #
# NAME: mesonuimvc.py                                                             #
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
from .mesonuimodle import MesonUiModule
from PyQt5.QtCore import QObject
from PyQt5.QtCore import pyqtSlot



class MesonUiController(QObject):
    def __init__(self, model: MesonUiModule = None):
        super().__init__()
        self._model: MesonUiModule = model
    # end of method

    @pyqtSlot(str)
    def meson_source_dir_did_changed(self, value) -> None:
        self._model.set_source(value)
    # end of method

    @pyqtSlot(str)
    def meson_script_dir_did_changed(self, value) -> None:
        self._model.set_script(value)
    # end of method
    
    @pyqtSlot(str)
    def meson_build_dir_did_changed(self, value) -> None:
        self._model.set_build(value)
    # end of method
