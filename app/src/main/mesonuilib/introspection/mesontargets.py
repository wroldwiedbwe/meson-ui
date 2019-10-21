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
import subprocess
from os.path import join as join_paths
from .mesoninfo import MesonInfo


class MesonIntroTargets:
    '''
        This is a data class for Meson target info
    '''
    def __init__(self, meson_info: MesonInfo = None):
        self._meson_info: MesonInfo = meson_info

    def get_name(self, index: int = 0):
        return self._meson_info.get_project_data(index, 'targets', 'name')

    def get_id(self, index: int = 0):
        return self._meson_info.get_project_data(index, 'targets', 'id')

    def get_type(self, index: int = 0):
        return self._meson_info.get_project_data(index, 'targets', 'type')

    def get_defined_in(self, index: int = 0):
        return self._meson_info.get_project_data(index, 'targets', 'defined_in')

    def get_filename(self, index: int = 0):
        return self._meson_info.get_project_data(index, 'targets', 'filename')

    def get_build_by_default(self, index: int = 0):
        return self._meson_info.get_project_data(index, 'targets', 'build_by_default')

    def get_target_sources(self, index: int = 0):
        return self._meson_info.get_project_data(index, 'targets', 'target_sources')

    def get_language(self, index: int = 0):
        return self._meson_info.get_project_data(index, 'targets', 'language')

    def get_compiler(self, index: int = 0):
        return self._meson_info.get_project_data(index, 'targets', 'compiler')

    def get_parameters(self, index: int = 0):
        return self._meson_info.get_project_data(index, 'targets', 'parameters')

    def get_sources(self, index: int = 0):
        return self._meson_info.get_project_data(index, 'targets', 'sources')

    def get_generated_sources(self, index: int = 0):
        return self._meson_info.get_project_data(index, 'targets', 'generated_sources')

    def get_subproject(self, index: int = 0):
        return self._meson_info.get_project_data(index, 'targets', 'subproject')

    def get_installed(self, index: int = 0):
        return self._meson_info.get_project_data(index, 'targets', 'installed')
