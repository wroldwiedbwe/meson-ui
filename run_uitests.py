#!/user/bin/env python3
###################################################################################
#                                                                                 #
# NAME: run_uitests.py                                                            #
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
from app.src.main.view.main_activity import MainActivity
from app.src.main.mvc.mesonuimodle import MesonUiModule
from app.src.main.mvc.mesonuimvc import MesonUiController
from PyQt5.QtCore import Qt
from os.path import join as join_paths
from os import path
import pytestqt
import pytest


def test_mesonui_app(qtbot):
    main_view = MainActivity()
    qtbot.addWidget(main_view)


def test_trivial_setup(qtbot):
    main_view = MainActivity()
    qtbot.addWidget(main_view)

    main_view.source_dir.clear()
    qtbot.keyClicks(main_view.source_dir, join_paths('test-cases', 'trivial-prog'))

    main_view.build_dir.clear()
    qtbot.keyClicks(main_view.build_dir, join_paths('test-cases', 'trivial-prog', 'builddir'))

    qtbot.mouseClick(main_view.push_setup, Qt.LeftButton)
    qtbot.mouseClick(main_view.intent_setup.push_setup, Qt.LeftButton)
    qtbot.mouseClick(main_view.push_build, Qt.LeftButton)
    qtbot.mouseClick(main_view.push_clean, Qt.LeftButton)
    
    assert main_view.source_dir.text() == join_paths('test-cases', 'trivial-prog')
    assert main_view.build_dir.text() == join_paths('test-cases', 'trivial-prog', 'builddir')
    assert path.isfile(join_paths('test-cases', 'trivial-prog', 'builddir', 'build.ninja'))