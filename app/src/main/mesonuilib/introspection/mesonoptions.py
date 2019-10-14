#!/user/bin/env python3
###################################################################################
#                                                                                 #
# NAME: mesonoptions.py                                                           #
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
from .imesonintro import InterfaceMesonIntro
from os import path

MESON_INTRO_OPTS: set = (
    'name',
    'value',
    'section',
    'machine',
    'type',
    'description')


class MesonIntroOption(InterfaceMesonIntro):
    def __init__(self, project = None):
        self._project = project
        InterfaceMesonIntro().__init__(project=self._project)
    # end of method

    def _intro_getter(self, key: int = 0, value: str = 'name'):
        if path.exists(self._project.get_build()):
            intro_data = json.loads(self._intro_loader(['--buildoptions', self._project.get_build()]))
        else:
            intro_data = json.loads(self._intro_loader(['--buildoptions', self._project.get_script()]))
        return intro_data[key][value]
    # end of method
