#!/user/bin/env python3
###################################################################################
#                                                                                 #
# NAME: outputexejob.py                                                           #
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
from PyQt5.QtCore import QUrl


class MesonUiConsole:
    def __init__(self, parent=None):
        self._parent = parent

        self._parent.meson.meson_builder._process.setProcessChannelMode(self._parent.meson.meson_builder._process.SeparateChannels)
        self._parent.meson.meson_builder._process.readyReadStandardOutput.connect(lambda: self._child_process_stdout())
        self._parent.meson.meson_builder._process.readyReadStandardError.connect(lambda: self._child_process_stderr())
    # end of method

    def append_line(self, text: str) -> None:
        if text == '':
            return
        cursor = self._parent.mesonui_output_console.textCursor()
        self._parent.mesonui_output_console.setTextCursor(cursor)
        cursor.setPosition(cursor.Start)
        cursor.movePosition(cursor.Left, cursor.KeepAnchor, 3)
        self._parent.mesonui_output_console.ensureCursorVisible()
    # end of method

    def child_process_exited(self):
        self.append_line(str('*** Finished process ***', 'utf8'))
    # end of method

    def _child_process_stdout(self):
        out: str = str(self._parent.meson.meson_builder._process.readAllStandardOutput(), 'utf8')
        self._parent.mesonui_output_console.setText(out)
        self.append_line(out)
    # end of method

    def _child_process_stderr(self):
        err: str = str(self._parent.meson.meson_builder._process.readAllStandardError(), 'utf8')
        self._parent.mesonui_output_console.setText(err)
        self.append_line(err)
    # end of method
