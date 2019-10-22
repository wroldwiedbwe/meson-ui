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
from ..introspection.mesonprojectinfo import MesonIntroProjectInfo
from ..introspection.mesonbenchmarks import MesonIntroBenchmarks
from ..introspection.mesonoptions import MesonIntroOptions
from ..introspection.mesontargets import MesonIntroTargets
from ..introspection.mesontargets import MesonIntroTargetSources
from ..introspection.mesonoptions import MesonIntroOptions
from ..introspection.mesoninfo import MesonInfo
from ..introspection.mesontests import MesonIntroTests
from .imesoncomponent import InterfaceMesonComponent

from PyQt5.QtCore import QProcess


class MesonIntrospection(InterfaceMesonComponent):
    def __init__(self, project=None, process: QProcess = None):
        self._meson_info = MesonInfo(project=project)
        self._intro_proj = MesonIntroProjectInfo(self._meson_info)
        self._intro_opts = MesonIntroOptions(self._meson_info)
        self._intro_test = MesonIntroTests(self._meson_info)
        self._intro_target = MesonIntroTargets(self._meson_info)
        self._intro_target_src = MesonIntroTargetSources(self._meson_info)
        self._intro_benchmarks = MesonIntroBenchmarks(self._meson_info)
        super().__init__(project=project)
    # end of method

    def introspection(self, key: str = 'projectinfo') -> any:
        if key == 'buildoptions':
            return self._intro_opts
        elif key == 'projectinfo':
            return self._intro_proj
        elif key == 'targets':
            return self._intro_target
        elif key == 'targets-sources':
            return self._intro_target_src
        elif key == 'benchmark':
            return self._intro_benchmarks
        elif key == 'tests':
            return self._intro_test
        else:
            RuntimeError('Unknon introspection key:')
        return []
    # end of method
