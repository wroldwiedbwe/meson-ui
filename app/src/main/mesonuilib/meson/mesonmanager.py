#!/user/bin/env python3
###################################################################################
#                                                                                 #
# NAME: mesonmanager.py                                                           #
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
from PyQt5.QtCore import QObject
import json
import os, subprocess

from .mesonintro import MesonIntrospection
from .mesonbuilder import MesonBuilder
from .mesonconfig import MesonConfig


class Meson(QObject):
    def __init__(self, parent=None):
        super(Meson, self).__init__()
        self._project = parent
        self._process = QProcess(self)
        self.meson_intro = MesonIntrospection(self._project, self._process)
        self.meson_builder = MesonBuilder(self._project, self._process)
        self.meson_configs = MesonConfig(self._project, self._process)
        # Need to add Meson rewriter "MesonRewriter(self._project, self._process)"
    # end of method

    def introspection(self, key_string: str = '') -> any:
        return self.meson_intro.introspection(key=key_string)
    # end of method

    def setup(self, args: list = []) -> None:
        self.meson_builder.setup(args)
    # end of method

    def reconfigure(self, args: list = []) -> None:
        self.meson_builder.reconfigure(args)
    # end of method
    
    def wipe(self, args: list = []) -> None:
        self.meson_builder.wipe(args)
    # end of method

    def build(self) -> None:
        self.meson_builder.build()
    # end of method

    def clean(self) -> None:
        self.meson_builder.clean()
    # end of method

    def tests(self) -> None:
        self.meson_builder.tests()    
    # end of method

    def install(self) -> None:
        self.meson_builder.install()
    # end of method

    def configure(self, args: list = []) -> None:
        self.meson_configs.configure(args)
    # end of method

    def rewrite(self, args: list = []) -> None:
        pass
    # end of method
