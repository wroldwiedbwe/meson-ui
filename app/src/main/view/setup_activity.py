#!/user/bin/env python3
###################################################################################
#                                                                                 #
# NAME: setup_activity.py                                                         #
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
from ..ui.activity_setup import Ui_SetupDialog
from ..mvc.configuremodle import ConfigureModule
from ..mvc.configuremvc import ConfigureController
from os import path


class SetupActivity(QMainWindow, Ui_SetupDialog):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__()
        super(Ui_SetupDialog, self).__init__()
        self.setupUi(self)
        
        self.setFixedSize(730, 464)
        self._data_model = ConfigureModule()
        self._controller = ConfigureController(self._data_model)
        self._parent = parent
        
        self.curr_source_dir.setText(self._parent._data_model.get_source())
        self.curr_build_dir.setText(self._parent._data_model.get_build())

        self._data_model.set_auto_features(self.combo_box_auto_feature.currentText())
        self._data_model.set_backend(self.combo_box_backend.currentText())
        self._data_model.set_buildtype(self.combo_box_buildtype.currentText())
        self._data_model.set_default_library(self.combo_box_default_library.currentText())
        self._data_model.set_layout(self.combo_box_layout.currentText())
        self._data_model.set_optimization(self.combo_box_optimization.currentText())
        self._data_model.set_unity(self.combo_box_unity.currentText())
        self._data_model.set_warnlevel(self.combo_box_warning.currentText())
        self._data_model.set_wrap_mode(self.combo_box_wrap_mode.currentText())
        self._data_model.set_b_asneeded(self.combo_box_b_asneeded.currentText())
        self._data_model.set_b_colorout(self.combo_box_b_colorout.currentText())
        self._data_model.set_b_coverage(self.combo_box_b_coverage.currentText())
        self._data_model.set_b_lto(self.combo_box_b_lto.currentText())
        self._data_model.set_b_lundef(self.combo_box_b_lundef.currentText())
        self._data_model.set_b_ndebug(self.combo_box_b_ndebug.currentText())
        self._data_model.set_b_pch(self.combo_box_b_pch.currentText())
        self._data_model.set_b_pgo(self.combo_box_b_pgo.currentText())
        self._data_model.set_b_pie(self.combo_box_b_pie.currentText())
        self._data_model.set_b_sanitize(self.combo_box_b_sanitize.currentText())
        self._data_model.set_b_staticpic(self.combo_box_b_staticpic.currentText())

        self.push_setup.clicked.connect(lambda: self.onclick_setup())
        self.push_not_yet.clicked.connect(lambda: self.onclick_not_yet())
    # end of method

    def get_werror(self) -> str:
        return 'true' if self.combo_box_werror.currentText() == 'true' else 'false'
    # end of method

    def get_debug(self) -> str:
        return 'true' if self.combo_box_debug.currentText() == 'true' else 'false'
    # end of method

    def get_strip(self) -> str:
        return 'true' if self.combo_box_strip.currentText() == 'true' else 'false'
    # end of method
    
    def onclick_setup(self):
        self.close()

        if self.curr_build_dir.text() != '':
            meson_args = [
                f'--auto-features={self._data_model.get_auto_features()}',
                f'--backend={self._data_model.get_backend()}',
                f'--buildtype={self._data_model.get_buildtype()}',
                f'--default-library={self._data_model.get_default_library()}',
                f'--layout={self._data_model.get_layout()}',
                f'--optimization={self._data_model.get_optimization()}',
                f'--unity={self._data_model.get_unity()}',
                f'--warnlevel={self._data_model.get_warnlevel()}',
                f'--wrap-mode={self._data_model.get_wrap_mode()}',
                f'-Db_asneeded={self._data_model.get_b_asneeded()}',
                f'-Db_colorout={self._data_model.get_b_colorout()}',
                f'-Db_coverage={self._data_model.get_b_coverage()}',
                f'-Db_lto={self._data_model.get_b_lto()}',
                f'-Db_lundef={self._data_model.get_b_lundef()}',
                f'-Db_ndebug={self._data_model.get_b_ndebug()}',
                f'-Db_pch={self._data_model.get_b_pch()}',
                f'-Db_pgo={self._data_model.get_b_pgo()}',
                f'-Db_pie={self._data_model.get_b_pie()}',
                f'-Db_sanitize={self._data_model.get_b_sanitize()}',
                f'-Db_staticpic={self._data_model.get_b_staticpic()}']

        if self.get_werror() == 'true':
            meson_args.extend(['--werror'])
        
        if self.get_debug() == 'true':
            meson_args.extend(['--debug'])

        if self.get_strip() == 'true':
            meson_args.extend(['--strip'])
                    
        if path.exists(self.curr_build_dir.text()):
            self._parent.meson.wipe(meson_args)
        else:
            self._parent.meson.setup(meson_args)
    # end of method

    def onclick_not_yet(self):
        self.close()
    # end of method
