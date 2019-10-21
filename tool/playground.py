#!/user/bin/env python3
###################################################################################
#                                                                                 #
# NAME: playground.py                                                             #
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
import os

#
# Mock the data modle only for build directory
#
class Fake:
    def get_build(self) -> str:
        return 'prog/builddir'


#
# This class should be built to manage getting info from the intro
# data from Meson generated intro-*.json files.
# 
# NOTE: I may need to have an inmemory 'meson-info.json' to make
#       the app work for older version of meson. 
#
class MesonIntrospection:
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
    
    def get_option(self, index: int, key: str, value: str):
        with open(join_paths(self._intro_load_infodir(), self._intro_load_data(key)), 'r') as f:
            prog_info = json.load(f)
        return prog_info[index][value]

    def get_dir(self, value: str) -> any:
        with open(self._meson_info_dir(), 'r') as f:
            dirs = json.load(f)
        return dirs["directories"][value]



opts: map = {
    'auto_features': 0,
    'backend': 1,
    'buildtype': 2,
    'debug': 3,
    'default_library': 4,
    'install_umask': 5,
    'layout': 6,
    'optimization': 7,
    'strip': 8,
    'unity': 9,
    'warning_level': 10,
    'werror': 11,
    'wrap_mode': 12,
    'cmake_prefix_path': 13,
    'pkg_config_path': 14,
    'build.cmake_prefix_path': 15,
    'build.pkg_config_path': 16,
    'backend_max_links': 17,
    'b_asneeded': 18,
    'b_bitcode': 19,
    'b_colorout': 20,
    'b_coverage': 21,
    'b_lto': 22,
    'b_lundef': 23,
    'b_ndebug': 24,
    'b_pch': 25,
    'b_pgo': 26,
    'b_pie': 27,
    'b_sanitize': 28,
    'b_staticpic': 29,
    'c_args': 30,
    'c_link_args': 31,
    'c_std': 32,
    'build.c_args': 33,
    'build.c_link_args': 34,
    'build.c_std': 35,
    'bindir': 36,
    'datadir': 37,
    'includedir': 38,
    'infodir': 39,
    'libdir': 40,
    'libexecdir': 41,
    'localedir': 42,
    'localstatedir': 43,
    'mandir': 44,
    'prefix': 45,
    'sbindir': 46,
    'sharedstatedir': 47,
    'sysconfdir': 48
}


class MesonIntroOptions:
    def __init__(self, meson_info: MesonIntrospection = None):
        self._meson_info: MesonIntrospection = meson_info

    def get_auto_feature(self, value: str):
        return self._meson_info.get_option(opts['auto_features'], 'buildoptions', value)

#
# Testing the class here.
prog = Fake()
info = MesonIntrospection(prog)
prog_opt = MesonIntroOptions(info)

print(prog_opt.get_auto_feature('name'))