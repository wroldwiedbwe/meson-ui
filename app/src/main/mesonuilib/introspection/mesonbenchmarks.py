#!/user/bin/env python3
###################################################################################
#                                                                                 #
# NAME: mesonbenchmarks.py                                                        #
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


class MesonIntroBenchmarks:
    '''
        This is a data class for Meson benchmark info
    '''
    def __init__(self, meson_info: MesonInfo = None):
        self._meson_info: MesonInfo = meson_info

    def get_command(self, index: int = 0):
        return self._meson_info.get_project_data(index, 'benchmarks', 'cmd')

    def get_environment(self, index: int = 0):
        return self._meson_info.get_project_data(index, 'benchmarks', 'env')

    def get_name(self, index: int = 0):
        return self._meson_info.get_project_data(index, 'benchmarks', 'name')

    def get_workdir(self, index: int = 0):
        return self._meson_info.get_project_data(index, 'benchmarks', 'workdir')

    def get_timeout(self, index: int = 0):
        return self._meson_info.get_project_data(index, 'benchmarks', 'timeout')

    def get_suite(self, index: int = 0):
        return self._meson_info.get_project_data(index, 'benchmarks', 'suite')

    def get_is_parallel(self, index: int = 0):
        return self._meson_info.get_project_data(index, 'benchmarks', 'is_parallel')

    def get_priority(self, index: int = 0):
        return self._meson_info.get_project_data(index, 'benchmarks', 'priority')
