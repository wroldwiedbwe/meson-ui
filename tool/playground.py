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
import os.path

#
# Mock the data modle only for build directory
#
class Fake:
    def get_build(self):
        return 'prog/builddir'


#
# This class should be built to manage getting info from the intro
# data from Meson generated intro-*.json files.
# 
# NOTE: I may need to have an inmemory 'meson-info.json' to make
#       the app work for older version of meson. 
#
class MesonIntrospection:
    def __init__(self, project = None):
        self._project = project
    # end of method

    def _intro_load_infodir(self):
        with open(f'{self._project.get_build()}/meson-info/meson-info.json', 'r') as f:
            datastore = json.load(f)
        return datastore["directories"]["info"]

    def _intro_load_data(self, key):
        with open(f'{self._project.get_build()}/meson-info/meson-info.json', 'r') as f:
            datastore = json.load(f)
        return datastore["introspection"]["information"][key]["file"]

    def _intro_getter(self, key: str = 'projectinfo'):
        key_value = self._intro_load_data(key)
        info_path = os.path.join(self._intro_load_infodir, key_value)
        return info_path
    # end of method

    def intro_get(self, key, value):
        with open(self._intro_getter(key=key), 'r') as f:
            prog_info = json.load(f)
            print(prog_info[value])


#
# Testing the class here.
# #
prog = Fake()
info = MesonIntrospection(prog)

print(info.intro_get('projectinfo', 'descriptive_name'))


#
# NOTE: Just some notes for me to use.
#

# MESON_INTRO = (
#     'buildoptions', 
#     'buildsystem_files', 
#     'dependencies', 
#     'installed', 
#     'projectinfo', 
#     'targets', 
#     'tests')

# 'directories': 
#     {
#          'source': '/Users/shnitzel/Developer/workspaces/python/subprojects/meson-ui/tool/prog', 
#          'build': '/Users/shnitzel/Developer/workspaces/python/subprojects/meson-ui/tool/prog/builddir', 
#          'info': '/Users/shnitzel/Developer/workspaces/python/subprojects/meson-ui/tool/prog/builddir/meson-info'
#     },