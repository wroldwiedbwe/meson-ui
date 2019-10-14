#!/user/bin/env python3
###################################################################################
#                                                                                 #
# NAME: mesonprojectinfo.py                                                       #
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
import json
import os, subprocess
from ..introspection.imesonintro import InterfaceMesonIntro
from .imesonintro import InterfaceMesonIntro


MESON_INTRO_PROJ: set = (
    'version', 
    'descriptive_name', 
    'subproject_dir', 
    'subprojects')


class MesonIntroProject(InterfaceMesonIntro):
    def __init__(self, project=None):
        self._project = project
        InterfaceMesonIntro().__init__(project=self._project)
    # end of method

    def _intro_getter(self, value: str):
        intro_data = json.loads(self._intro_loader(['--projectinfo', self._project.get_build()]))
        return intro_data[value]
    # end of method
