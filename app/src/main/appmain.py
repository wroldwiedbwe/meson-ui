#!/user/bin/env python3
###################################################################################
#                                                                                 #
# NAME: appmain.py                                                                #
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
from .activity_manager import MesonUi
import sys


def mesonui_main():
    app = MesonUi(sys_argv=sys.argv)
    sys.exit(app.exec_())
# end of function mesonui_main


if __name__ == "__main__":
    mesonui_main()
