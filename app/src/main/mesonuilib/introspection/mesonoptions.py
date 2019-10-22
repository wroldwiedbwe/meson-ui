#!/user/bin/env python3
###################################################################################
#                                                                                 #
# NAME: mesonoptions.py                                                           #
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
from .mesonoptconsts import opts


class MesonIntroOptions:
    '''
        This is a data class for Meson built-in options
    '''
    def __init__(self, meson_info: MesonInfo = None):
        self._meson_info: MesonInfo = meson_info

    def get_auto_feature(self, value: str):
        return self._meson_info.get_option(opts['auto_features'], 'buildoptions', value)

    def get_backend(self, value: str):
        return self._meson_info.get_option(opts['backend'], 'buildoptions', value)

    def get_buildtype(self, value: str):
        return self._meson_info.get_option(opts['buildtype'], 'buildoptions', value)

    def get_debug(self, value: str):
        return self._meson_info.get_option(opts['debug'], 'buildoptions', value)

    def get_default_library(self, value: str):
        return self._meson_info.get_option(opts['default_library'], 'buildoptions', value)

    def get_install_umask(self, value: str):
        return self._meson_info.get_option(opts['install_umask'], 'buildoptions', value)

    def get_layout(self, value: str):
        return self._meson_info.get_option(opts['layout'], 'buildoptions', value)

    def get_optimization(self, value: str):
        return self._meson_info.get_option(opts['optimization'], 'buildoptions', value)

    def get_strip(self, value: str):
        return self._meson_info.get_option(opts['strip'], 'buildoptions', value)

    def get_unity(self, value: str):
        return self._meson_info.get_option(opts['unity'], 'buildoptions', value)

    def get_warning_level(self, value: str):
        return self._meson_info.get_option(opts['warning_level'], 'buildoptions', value)

    def get_werror(self, value: str):
        return self._meson_info.get_option(opts['werror'], 'buildoptions', value)

    def get_wrap_mode(self, value: str):
        return self._meson_info.get_option(opts['wrap_mode'], 'buildoptions', value)

    def get_cmake_prefix_path(self, value: str):
        return self._meson_info.get_option(opts['cmake_prefix_path'], 'buildoptions', value)

    def get_pkg_config_path(self, value: str):
        return self._meson_info.get_option(opts['pkg_config_path'], 'buildoptions', value)

    def get_build_cmake_prefix_path(self, value: str):
        return self._meson_info.get_option(opts['build.cmake_prefix_path'], 'buildoptions', value)

    def get_build_pkg_config_path(self, value: str):
        return self._meson_info.get_option(opts['build.pkg_config_path'], 'buildoptions', value)

    def get_backend_max_links(self, value: str):
        return self._meson_info.get_option(opts['backend_max_links'], 'buildoptions', value)

    def get_b_asneeded(self, value: str):
        return self._meson_info.get_option(opts['b_asneeded'], 'buildoptions', value)

    def get_b_bitcode(self, value: str):
        return self._meson_info.get_option(opts['b_bitcode'], 'buildoptions', value)

    def get_b_colorout(self, value: str):
        return self._meson_info.get_option(opts['b_colorout'], 'buildoptions', value)

    def get_b_coverage(self, value: str):
        return self._meson_info.get_option(opts['b_coverage'], 'buildoptions', value)

    def get_b_lto(self, value: str):
        return self._meson_info.get_option(opts['b_lto'], 'buildoptions', value)

    def get_b_lundef(self, value: str):
        return self._meson_info.get_option(opts['b_lundef'], 'buildoptions', value)

    def get_b_ndebug(self, value: str):
        return self._meson_info.get_option(opts['b_ndebug'], 'buildoptions', value)

    def get_b_pch(self, value: str):
        return self._meson_info.get_option(opts['b_pch'], 'buildoptions', value)

    def get_b_pgo(self, value: str):
        return self._meson_info.get_option(opts['b_pgo'], 'buildoptions', value)

    def get_b_pie(self, value: str):
        return self._meson_info.get_option(opts['b_pie'], 'buildoptions', value)

    def get_b_sanitize(self, value: str):
        return self._meson_info.get_option(opts['b_sanitize'], 'buildoptions', value)

    def get_b_staticpi(self, value: str):
        return self._meson_info.get_option(opts['b_staticpi'], 'buildoptions', value)