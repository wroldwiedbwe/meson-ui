#!/user/bin/env python3
###################################################################################
#                                                                                 #
# NAME: configuremodle.py                                                         #
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


class ConfigureModule(QObject):
    auto_features_changed = pyqtSignal(str)
    backend_changed = pyqtSignal(str)
    buildtype_changed = pyqtSignal(str)
    default_library_changed = pyqtSignal(str)
    layout_changed = pyqtSignal(str)
    optimization_changed = pyqtSignal(str)
    unity_changed = pyqtSignal(str)
    warnlevel_changed = pyqtSignal(str)
    wrap_mode_changed = pyqtSignal(str)
    
    b_asneeded_changed = pyqtSignal(str)
    b_colorout_changed = pyqtSignal(str)
    b_coverage_changed = pyqtSignal(str)
    b_staticpic_changed = pyqtSignal(str)
    b_sanitize_changed = pyqtSignal(str)
    b_ndebug_changed = pyqtSignal(str)
    b_lundef_changed = pyqtSignal(str)
    b_pie_changed = pyqtSignal(str)
    b_pgo_changed = pyqtSignal(str)
    b_pch_changed = pyqtSignal(str)
    b_lto_changed = pyqtSignal(str)
    
    def __init__(self):
        super().__init__()
        self._auto_features: str = ''
        self._backend: str = ''
        self._buildtype: str = ''
        self._default_library: str = ''
        self._layout: str = ''
        self._optimization: str = ''
        self._unity: str = ''
        self._warnlevel: str = ''
        self._wrap_mode: str = ''
        
        self._b_asneeded: str = ''
        self._b_colorout: str = ''
        self._b_coverage: str = ''
        self._b_staticpic: str = ''
        self._b_sanitize: str = ''
        self._b_ndebug: str = ''
        self._b_lundef: str = ''
        self._b_pie: str = ''
        self._b_pgo: str = ''
        self._b_pch: str = ''
        self._b_lto: str = ''
    # end of method

    def get_auto_features(self) -> str:
        return self._auto_features
    # end of method

    def set_auto_features(self, value: str) -> None:
        self._auto_features = value
        self.auto_features_changed.emit(value)
    # end of method

    def get_backend(self) -> str:
        return self._backend
    # end of method

    def set_backend(self, value: str) -> None:
        backend_is: str = value
        if backend_is == 'Ninja build':
            backend_is = 'ninja'
        elif backend_is == 'Xcode':
            backend_is = 'xcode'
        elif backend_is == 'Visual Studio 2010':
            backend_is = 'vs2010'
        elif backend_is == 'Visual Studio 2015':
            backend_is = 'vs2015'
        elif backend_is == 'Visual Studio 2017':
            backend_is = 'vs2017'
        elif backend_is == 'Visual Studio 2019':
            backend_is = 'vs2019'
        self._backend = backend_is
        self.backend_changed.emit(backend_is)
    # end of method

    def get_buildtype(self) -> str:
        return self._buildtype
    # end of method

    def set_buildtype(self, value: str) -> None:
        self._buildtype = value
        self.buildtype_changed.emit(value)
    # end of method

    def get_default_library(self) -> str:
        return self._default_library
    # end of method

    def set_default_library(self, value: str) -> None:
        self._default_library = value
        self.default_library_changed.emit(value)
    # end of method

    def get_layout(self) -> str:
        return self._layout
    # end of method

    def set_layout(self, value: str) -> None:
        self._layout = value
        self.layout_changed.emit(value)
    # end of method

    def get_optimization(self) -> str:
        return self._optimization
    # end of method

    def set_optimization(self, value: str) -> None:
        self._optimization = value
        self.optimization_changed.emit(value)
    # end of method

    def get_unity(self) -> str:
        return self._unity
    # end of method

    def set_unity(self, value: str) -> None:
        self._unity = value
        self.unity_changed.emit(value)
    # end of method

    def get_warnlevel(self) -> str:
        return self._warnlevel
    # end of method

    def set_warnlevel(self, value: str) -> None:
        self._warnlevel = value
        self.warnlevel_changed.emit(value)
    # end of method

    def get_wrap_mode(self) -> str:
        return self._wrap_mode
    # end of method

    def set_wrap_mode(self, value: str) -> None:
        self._wrap_mode = value
        self.wrap_mode_changed.emit(value)
    # end of method

    def get_b_asneeded(self) -> str:
        return self._b_asneeded
    # end of method

    def set_b_asneeded(self, value: str) -> None:
        self._b_asneeded = value
        self.b_asneeded_changed.emit(value)
    # end of method

    def get_b_colorout(self) -> str:
        return self._b_colorout
    # end of method

    def set_b_colorout(self, value: str) -> None:
        self._b_colorout = value
        self.b_colorout_changed.emit(value)
    # end of method

    def get_b_coverage(self) -> str:
        return self._b_coverage
    # end of method

    def set_b_coverage(self, value: str) -> None:
        self._b_coverage = value
        self.b_coverage_changed.emit(value)
    # end of method

    def get_b_staticpic(self) -> str:
        return self._b_staticpic
    # end of method

    def set_b_staticpic(self, value: str) -> None:
        self._b_staticpic = value
        self.b_staticpic_changed.emit(value)
    # end of method

    def get_b_sanitize(self) -> str:
        return self._b_sanitize
    # end of method

    def set_b_sanitize(self, value: str) -> None:
        self._b_sanitize = value
        self.b_sanitize_changed.emit(value)
    # end of method

    def get_b_ndebug(self) -> str:
        return self._b_ndebug
    # end of method

    def set_b_ndebug(self, value: str) -> None:
        self._b_ndebug = value
        self.b_ndebug_changed.emit(value)
    # end of method

    def get_b_lundef(self) -> str:
        return self._b_lundef
    # end of method

    def set_b_lundef(self, value: str) -> None:
        self._b_lundef = value
        self.b_lundef_changed.emit(value)
    # end of method

    def get_b_pie(self) -> str:
        return self._b_pie
    # end of method

    def set_b_pie(self, value: str) -> None:
        self._b_pie = value
        self.b_pie_changed.emit(value)
    # end of method

    def get_b_pgo(self) -> str:
        return self._b_pgo
    # end of method

    def set_b_pgo(self, value: str) -> None:
        self._b_pgo = value
        self.b_pgo_changed.emit(value)
    # end of method

    def get_b_pch(self) -> str:
        return self._b_pch
    # end of method

    def set_b_pch(self, value: str) -> None:
        self._b_pch = value
        self.b_pch_changed.emit(value)
    # end of method

    def get_b_lto(self) -> str:
        return self._b_lto
    # end of method

    def set_b_lto(self, value: str) -> None:
        self._b_lto = value
        self.b_lto_changed.emit(value)
    # end of method