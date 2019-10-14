#!/user/bin/env python3
###################################################################################
#                                                                                 #
# NAME: main_activity.py                                                          #
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
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui  import QDesktopServices
from PyQt5.QtCore import QUrl
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import QDir
from os.path import join as join_paths

from ..mesonuilib.console.outputexejob import MesonUiConsole
from ..mesonuilib.meson.mesonmanager import Meson
from ..mvc.mesonuimodle import MesonUiModule
from ..mvc.mesonuimvc import MesonUiController

from .info_activity import InfoActivity
from .setup_activity import SetupActivity
from ..ui.activity_main import Ui_MainWindow

EMPTY_STRING = ''


class MainActivity(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)

        self.setFixedSize(800, 600)
        self._data_model = MesonUiModule()
        self._controller = MesonUiController(self._data_model)
        
        self.meson = Meson(self._data_model)
        self.console = MesonUiConsole(self)
        
        self._data_model.meson_source_dir_changed.connect(self.source_dir_did_changed)
        self._data_model.meson_build_dir_changed.connect(self.build_dir_did_changed)
        
        self.on_create()
    # end of method

    pyqtSlot()
    def on_create(self) -> None:
   
        # Meson-ui menu bar.
        self.actionOpen_folder.triggered.connect(lambda: self.onclick_open())
        self.actionAbout_Meson_ui.triggered.connect(lambda: self.onclick_info())
        self.actionQuit_Meson_ui.triggered.connect(lambda: self.onclick_quit())
        
        # Meson-ui help.
        self.actionMeson_docs.triggered.connect(lambda: self.onclick_docs())
        self.actionMeson_QnA.triggered.connect(lambda: self.onclick_faqs())
        self.actionMeson_ui_issue.triggered.connect(lambda: self.onclick_mesonui_issue())
        self.actionMeson_issue.triggered.connect(lambda: self.onclick_meson_issue())

        # Mesnu-ui main view buttons.
        self.push_install.clicked.connect(lambda: self.onclick_install())
        self.push_setup.clicked.connect(lambda: self.onclick_setup())
        self.push_build.clicked.connect(lambda: self.onclick_build())
        self.push_tests.clicked.connect(lambda: self.onclick_tests())
        self.push_clean.clicked.connect(lambda: self.onclick_clean())
        self.push_clear.clicked.connect(lambda: self.onclick_clear())
        self.push_open.clicked.connect(lambda: self.onclick_open())
        self.push_docs.clicked.connect(lambda: self.onclick_docs())
        
    # end of method
    
    pyqtSlot()
    def onclick_setup(self) -> None:
        self._controller.meson_source_dir_did_changed(self.source_dir.text())
        self._controller.meson_script_dir_did_changed(join_paths(self.source_dir.text(), 'meson.build'))
        self._controller.meson_build_dir_did_changed(self.build_dir.text())

        self.intent_setup = SetupActivity(self, self._data_model, self._controller)
        self.intent_setup.show()
    # end of method

    pyqtSlot()
    def onclick_info(self) -> None:
        self.intent_info = InfoActivity()
        self.intent_info.show()
    # end of method

    pyqtSlot()
    def onclick_quit(self) -> None:
        QApplication.quit()
    # end of method

    pyqtSlot()
    def onclick_build(self) -> None:
        try:
            self.meson.build()
        except Exception as e:
            print(f'error: {e}')
    # end of method
        
    pyqtSlot()
    def onclick_clean(self) -> None:
        try:
            self.meson.clean()
        except Exception as e:
            print(f'error: {e}')
    # end of method
    
    pyqtSlot()
    def onclick_tests(self) -> None:
        try:
            self.meson.tests()
        except Exception as e:
            print(f'error: {e}')
    # end of method
        
    pyqtSlot()
    def onclick_install(self) -> None:
        try:
            self.meson.install()
        except Exception as e:
            print(f'error: {e}')
    # end of method

    pyqtSlot()
    def onclick_clear(self) -> None:
        self.source_dir_did_changed(EMPTY_STRING)
        self.build_dir_did_changed(EMPTY_STRING)
    # end of method

    pyqtSlot()
    def onclick_open(self) -> None:
        dir_path = str(QFileDialog.getExistingDirectory(self, 'Open project directory', QDir.homePath()))
        if dir_path != '':
            self._controller.meson_source_dir_did_changed(dir_path)
            self._controller.meson_script_dir_did_changed(join_paths(dir_path, 'meson.build'))
            self._controller.meson_build_dir_did_changed(join_paths(dir_path, 'builddir'))

        if self._data_model.get_source() != '' and self._data_model.get_build() != '':
            self.source_dir.setText(self._data_model.get_source())
            self.build_dir.setText(self._data_model.get_build())
    # end of method

    @pyqtSlot()
    def onclick_docs(self):
        self.open_url(QUrl('https://mesonbuild.com'))
    # end of method

    @pyqtSlot()
    def onclick_faqs(self):
        self.open_url(QUrl('https://mesonbuild.com/FAQ.html'))
    # end of method
        
    @pyqtSlot()
    def onclick_mesonui_issue(self):
        self.open_url(QUrl('https://github.com/michaelbadcrumble/meson-ui/issues'))
    # end of method

    @pyqtSlot()
    def onclick_meson_issue(self):
        self.open_url(QUrl('https://github.com/mesonbuild/meson/issues'))        
    # end of method

    def open_url(self, url: QUrl):
        QDesktopServices.openUrl(url=url)
    # end of method

    pyqtSlot(str)
    def source_dir_did_changed(self, value) -> str:
        self.source_dir.setText(value)
    # end of method
    
    pyqtSlot(str)
    def build_dir_did_changed(self, value) -> str:
        self.build_dir.setText(value)
    # end of method
