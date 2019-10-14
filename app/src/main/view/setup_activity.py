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
from PyQt5.QtCore import QSettings
from os import path


class SetupActivity(QMainWindow, Ui_SetupDialog):
    def __init__(self, parent=None, model=None, controller=None):
        super(QMainWindow, self).__init__()
        super(Ui_SetupDialog, self).__init__()
        self.setupUi(self)
        
        self.setFixedSize(715, 364)
        self._sub_controller = controller
        self._sub_model = model
        self._parent = parent
        
        self.curr_source_dir.setText(self._parent._data_model.get_source())
        self.curr_build_dir.setText(self._parent._data_model.get_build())

        self.push_setup.clicked.connect(lambda: self.onclick_setup())
        self.push_not_yet.clicked.connect(lambda: self.onclick_not_yet())
    # end of method

    def get_backend(self) -> str:
        backend_is: str = 'ninja'
        if self.combo_box_backend.currentText() == 'Ninja build':
            backend_is = 'ninja'
        elif self.combo_box_backend.currentText() == 'Xcode':
            backend_is = 'xcode'
        elif self.combo_box_backend.currentText() == 'Visual Studio 2010':
            backend_is = 'vs2010'
        elif self.combo_box_backend.currentText() == 'Visual Studio 2015':
            backend_is = 'vs2015'
        elif self.combo_box_backend.currentText() == 'Visual Studio 2017':
            backend_is = 'vs2017'
        elif self.combo_box_backend.currentText() == 'Visual Studio 2019':
            backend_is = 'vs2019'
        return backend_is
    # end of method

    def get_werror(self) -> str:
        return 'true' if self.combo_box_werror.currentText() == 'true' else 'false'
    # end of method

    def onclick_setup(self):
        self.close()
        if self.curr_build_dir.text() != '':
            meson_args = [
                f'--backend={self.get_backend()}',
                f'--buildtype={self.combo_box_buildtype.currentText()}',
                f'--warnlevel={self.combo_box_warning.currentText()}',
                f'--layout={self.combo_box_layout.currentText()}',
                f'--optimization={self.combo_box_optimization.currentText()}']
                #
                # Need to add more options from Meson built in core group 
                #

            if self.get_werror() == 'true':
                meson_args.extend(['--werror'])
            
            self._parent.meson.setup(meson_args)
    # end of method

    def onclick_not_yet(self):
        self.close()
    # end of method
