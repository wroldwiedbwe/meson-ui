#!/user/bin/env python3
###################################################################################
#                                                                                 #
# NAME: mesontests.py                                                             #
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


class MesonIntroTests:
    '''
        This is a data class for Meson project test info
    '''
    def __init__(self, meson_info: MesonInfo = None):
        self._meson_info: MesonInfo = meson_info

    def get_command(self, index: int = 0):
        return self._meson_info.get_project_data(index, 'tests', 'cmd')

    def get_environment(self, index: int = 0):
        return self._meson_info.get_project_data(index, 'tests', 'env')

    def get_name(self, index: int = 0):
        return self._meson_info.get_project_data(index, 'tests', 'name')

    def get_workdir(self, index: int = 0):
        return self._meson_info.get_project_data(index, 'tests', 'workdir')

    def get_timeout(self, index: int = 0):
        return self._meson_info.get_project_data(index, 'tests', 'timeout')

    def get_suite(self, index: int = 0):
        return self._meson_info.get_project_data(index, 'tests', 'suite')

    def get_is_parallel(self, index: int = 0):
        return self._meson_info.get_project_data(index, 'tests', 'is_parallel')

    def get_priority(self, index: int = 0):
        return self._meson_info.get_project_data(index, 'tests', 'priority')