#!/user/bin/env python3
###################################################################################
#                                                                                 #
# NAME: configuremvc.py                                                           #
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
from .configuremodle import ConfigureModule
from PyQt5.QtCore import QObject
from PyQt5.QtCore import pyqtSlot


class ConfigureController(QObject):
    def __init__(self, model: ConfigureModule = None):
        super().__init__()
        self._model: ConfigureModule = model
    # end of method

    @pyqtSlot(str)
    def auto_feature_did_changed(self, value) -> None:
        self._model.set_auto_features(value)
    # end of method

    @pyqtSlot(str)
    def backend_did_changed(self, value) -> None:
        self._model.set_backend(value)
    # end of method
    
    @pyqtSlot(str)
    def buildtype_did_changed(self, value) -> None:
        self._model.set_buildtype(value)
    # end of method

    @pyqtSlot(str)
    def default_library_did_changed(self, value) -> None:
        self._model.set_default_library(value)
    # end of method
    
    @pyqtSlot(str)
    def optimization_did_changed(self, value) -> None:
        self._model.set_optimization(value)
    # end of method
    
    @pyqtSlot(str)
    def unity_did_changed(self, value) -> None:
        self._model.set_unity(value)
    # end of method
    
    @pyqtSlot(str)
    def warnlevel_did_changed(self, value) -> None:
        self._model.set_warnlevel(value)
    # end of method
    
    @pyqtSlot(str)
    def wrap_mode_did_changed(self, value) -> None:
        self._model.set_wrap_mode(value)
    # end of method

    @pyqtSlot(str)
    def b_asneeded_did_changed(self, value) -> None:
        self._model.set_b_asneeded(value)
    # end of method
    
    @pyqtSlot(str)
    def b_colorout_did_changed(self, value) -> None:
        self._model.set_b_colorout(value)
    # end of method

    @pyqtSlot(str)
    def b_coverage_did_changed(self, value) -> None:
        self._model.set_b_coverage(value)
    # end of method

    @pyqtSlot(str)
    def b_staticpic_did_changed(self, value) -> None:
        self._model.set_b_staticpic(value)
    # end of method


    @pyqtSlot(str)
    def b_sanitize_did_changed(self, value) -> None:
        self._model.set_b_sanitize(value)
    # end of method

    @pyqtSlot(str)
    def b_ndebug_did_changed(self, value) -> None:
        self._model.set_b_ndebug(value)
    # end of method

    @pyqtSlot(str)
    def b_lundef_did_changed(self, value) -> None:
        self._model.set_b_lundef(value)
    # end of method
    
    @pyqtSlot(str)
    def b_pie_did_changed(self, value) -> None:
        self._model.set_b_pie(value)
    # end of method

    @pyqtSlot(str)
    def b_pgo_did_changed(self, value) -> None:
        self._model.set_b_pgo(value)
    # end of method

    @pyqtSlot(str)
    def b_pch_did_changed(self, value) -> None:
        self._model.set_b_pch(value)
    # end of method

    @pyqtSlot(str)
    def b_lto_did_changed(self, value) -> None:
        self._model.set_b_lto(value)
    # end of method