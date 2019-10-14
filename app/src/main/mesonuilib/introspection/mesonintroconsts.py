#!/user/bin/env python3
###################################################################################
#                                                                                 #
# NAME: mesonintroconsts.py                                                       #
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


class MesonOptConst:
    def __init__(self):
        self.AUTO_FEATURE            = 0
        self.BACKEND                 = 1
        self.BUILDTYPE               = 2
        self.DEBUG                   = 3
        self.DEFAULT_LIBRARY         = 4
        self.INSTALL_UMASK           = 5
        self.LAYOUT                  = 6
        self.OPTIMIZATIONS           = 7
        self.STRIP                   = 8
        self.UNITY                   = 9
        self.WARNING_LEVEL           = 10
        self.WERROR                  = 11
        self.WRAP_MODE               = 12
        self.CMAKE_PREFIX_PATH       = 13
        self.PKG_CONFIG_PATH         = 14
        self.BUILD_CMAKE_PREFIX_PATH = 15
        self.BUILD_PKG_CONFIG_PATH   = 16
        self.BACKEND_MAX_LINKS       = 17
        self.B_ASNEEDED           = 18
        self.B_BITCODE            = 19
        self.B_COLOROUT           = 20
        self.B_COVERAGE           = 21
        self.B_LTO                = 22
        self.B_LUNDEF             = 23
        self.B_NDEBUG             = 24
        self.B_PCH                = 25
        self.B_PGO                = 26
        self.B_PIE                = 27
        self.B_SANITIZE           = 28
        self.B_STATICPIC          = 29
        self.C_ARGS               = 30
        self.LANG_STD             = 31
        self.LANG_LINK_ARGS       = 32
        self.BUILD_LANG_ARGS      = 33
        self.BUILD_LANG_STD       = 34
        self.BUILD_LANG_LINK_ARGS = 35
        self.BINDIR               = 36
        self.DATADIR              = 37
        self.INCLUDEDIR           = 38
        self.INFODIR              = 39
        self.LIBDIR               = 40
        self.LIBEXECDIR           = 41
        self.LOCALEDIR            = 42
        self.LOCALSTATEDIR        = 43
        self.MANDIR               = 44
        self.SBINDIR              = 45
        self.SHAREDSTATEDIR       = 46
        self.SYSCONFDIR           = 47
        self.ERRORLOGS            = 48
        self.STDSPLIT             = 49
    # end of method
