#!/user/bin/env python3
###################################################################################
#                                                                                 #
# NAME: appinfo.py                                                                #
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
import sys

class MesonUiPyPiInfo:
    @staticmethod
    def get_version() -> str:
        return '0.1.0'
    # end of method

    @staticmethod
    def get_name() -> str:
        return 'meson-ui'
    # end of method

    @staticmethod
    def get_license() -> str:
        return 'LGPL'
    # end of method

    @staticmethod
    def get_author() -> str:
        return 'Michael Brockus'
    # end of method

    @staticmethod
    def get_gmail() -> str:
        return 'michaelbrockus@gmail.com'
    # end of method

    @staticmethod
    def get_email() -> str:
        return 'michaelbrockus@icloud.com'
    # end of method

    @staticmethod
    def get_description() -> str:
        return 'GUI App for the Meson build system.'
    # end of method
    
    @staticmethod
    def required_version() -> None:
        if sys.version_info < (3, 6, 0):
            raise SystemExit(f'ERROR: Tried to install Meson with an unsupported Python version: {sys.version}'
                            '\n\nMeson requires Python 3.6.0 or greater')
