#!/user/bin/env python3
###################################################################################
#                                                                                 #
# NAME: mesoninfo.py                                                              #
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


class MesonInfo:
    '''
        This works on getting the data from Meson 'intro-*.json' files.
        and feeds it to the data wrappers classes.
    '''
    def __init__(self, project = None):
        self._project = project
    # end of method
    
    def _meson_info_dir(self) -> str:
        return join_paths(f'{self._project.get_build()}', 'meson-info', 'meson-info.json')

    def _intro_load_data(self, key: str) -> any:
        with open(self._meson_info_dir(), 'r') as f:
            data = json.load(f)
        return data["introspection"]["information"][key]["file"]

    def _intro_load_infodir(self) -> list:
        with open(self._meson_info_dir(), 'r') as f:
            info = json.load(f)
        return info["directories"]["info"]

    def get_project_data(self, index: int, key: str , value: str) -> any:
        with open(join_paths(self._intro_load_infodir(), self._intro_load_data(key)), 'r') as f:
            prog_info = json.load(f)
        return prog_info[index][value]

    def get_intro(self, key: str , value: str) -> any:
        with open(join_paths(self._intro_load_infodir(), self._intro_load_data(key)), 'r') as f:
            prog_info = json.load(f)
        return prog_info[value]

    def get_dir(self, value: str) -> any:
        with open(self._meson_info_dir(), 'r') as f:
            dirs = json.load(f)
        return dirs["directories"][value]
