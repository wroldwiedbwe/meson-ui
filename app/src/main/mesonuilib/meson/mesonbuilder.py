#!/user/bin/env python3
###################################################################################
#                                                                                 #
# NAME: mesonbuilder.py                                                           #
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
import subprocess
import os
import json

from .imesoncomponent import InterfaceMesonComponent
from ..ninjabuilder.ninjabuilder import NinjaBuilder


class MesonBuilder(InterfaceMesonComponent):
    def __init__(self, project=None, process: QProcess = None):
        self._ninjabuild = NinjaBuilder(self)
        self._process: QProcess = process
        self._project = project
        super().__init__(project=self._project)
    # end of method

    def setup(self, args: list = []) -> None:
        meson_args: list = ['setup', self._project.get_source(), self._project.get_build()]
        meson_args.extend(args)
        self._run(meson_args)
    # end of method

    def reconfigure(self, args: list = []) -> None:
        meson_args: list = ['setup', self._project.get_source(), self._project.get_build()]
        meson_args.extend(args)
        meson_args.extend('--reconfigure')
        self._run(meson_args)
    # end of method

    def wipe(self, args: list = []) -> None:
        meson_args: list = ['setup', self._project.get_source(), self._project.get_build()]
        meson_args.extend(args)
        meson_args.extend('--wipe')
        self._run(meson_args)
    # end of method

    def tests(self) -> None:
        meson_args: list = ['test', '-C', self._project.get_build()]
        self._run(meson_args)
    # end of method

    def build(self) -> None:
        self._ninjabuild.build()
    # end of method

    def clean(self) -> None:
        self._ninjabuild.clean()
    # end of method

    def install(self) -> None:
        self._ninjabuild.install()
    # end of method

    def _run(self, args: list) -> None:
        self._process.start('meson', args)
        self._process.waitForFinished()
    # end of method
