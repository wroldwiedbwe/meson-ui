#!/user/bin/env python3
###################################################################################
#                                                                                 #
# NAME: imesonintro.py                                                            #
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


class InterfaceMesonIntro:
    def __init__(self, project = None):
        self._project = project
    # end of method

    def _intro_loader(self, args: list) -> any:
        cmd = ['meson', 'introspect']
        cmd.extend(args)
        return subprocess.check_output(cmd, stderr=subprocess.STDOUT)
    # end of method
