#!/user/bin/env python3
###################################################################################
#                                                                                 #
# NAME: mesonintro.py                                                             #
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
from ..introspection.mesonprojectinfo import MesonIntroProject
from ..introspection.mesontargets import MesonIntroTarget
from ..introspection.mesontargets import MesonIntroTargetSources
from ..introspection.mesontests import MesonIntroTests
from ..introspection.mesonoptions import MesonIntroOption
from .imesoncomponent import InterfaceMesonComponent

from PyQt5.QtCore import QProcess


class MesonIntrospection(InterfaceMesonComponent):
    def __init__(self, project=None, process: QProcess = None):
        self._intro_proj = MesonIntroProject(project=project)
        self._intro_opts = MesonIntroOption(project=project)
        self._intro_test = MesonIntroTests(project=project)
        self._intro_target = MesonIntroTarget(project=project)
        self._intro_target_src = MesonIntroTargetSources(project=project)
        self._process: QProcess = process
        super().__init__(project=project)
    # end of method

    def introspection(self, key_string: str = '', value: str = '', option: int = 0) -> any:
        if key_string == 'intro-build-option':
            return self._intro_opts._intro_getter(option, value)
        elif key_string == 'intro-projectinfo':
            return self._intro_proj._intro_getter(value)
        elif key_string == 'intro-target':
            return self._intro_target._intro_getter(value)
        elif key_string == 'intro-target-sources':
            return self._intro_target_src._intro_getter(value)
        elif key_string == 'intro-tests':
            return self._intro_test._intro_getter(value)
        else:
            self.error('Unknon introspection key:')
        return []
    # end of method

    def _run(self, args) -> None:
        self._process.waitForStarted()
        self._process.start('meson', args)
        self._process.waitForFinished()
    # end of method
