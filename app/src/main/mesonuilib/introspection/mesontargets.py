#!/user/bin/env python3
###################################################################################
#                                                                                 #
# NAME: mesontarget.py                                                            #
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


MESON_INTRO_TARGET: set = (
    'name', 
    'id', 
    'type', 
    'defined_in', 
    'filename', 
    'build_by_default', 
    'subproject', 
    'installed')

MESON_INTRO_TARGET_SOURCES: set = (
    'language', 
    'compiler', 
    'parameters', 
    'sources', 
    'generated_sources')


class MesonIntroTargetSources(InterfaceMesonIntro):
    def __init__(self, project=None):
        self._project = project
        InterfaceMesonIntro().__init__(project=self._project)

    def _intro_getter(self, value: str):
        intro_data = json.loads(self._intro_loader(['--targets', self._project.get_build()]))
        subdata = intro_data[0]['target_sources']
        return subdata[0][value]
    # end of method


class MesonIntroTarget(InterfaceMesonIntro):
    def __init__(self, project=None):
        self._project = project
        InterfaceMesonIntro().__init__(project=self._project)

    def _intro_getter(self, value: str):
        intro_data = json.loads(self._intro_loader(['--targets', self._project.get_build()]))
        return intro_data[0][value]
    # end of method
