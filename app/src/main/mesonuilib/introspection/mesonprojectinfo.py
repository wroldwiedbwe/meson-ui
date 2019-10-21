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
import subprocess
from os.path import join as join_paths
from .mesoninfo import MesonInfo


class MesonIntroProjectInfo:
    '''
        This is a data class for Meson project info
    '''
    def __init__(self, meson_info: MesonInfo = None):
        self._meson_info: MesonInfo = meson_info

    def get_name(self):
        return self._meson_info.get_intro('projectinfo', 'descriptive_name')

    def get_version(self):
        return self._meson_info.get_intro('projectinfo', 'version')
    
    def get_subprojects(self):
        return self._meson_info.get_intro('projectinfo', 'subprojects')
    
    def get_subproject_dir(self):
        return self._meson_info.get_intro('projectinfo', 'subproject_dir')

