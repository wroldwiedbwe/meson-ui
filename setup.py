#!/user/bin/env python3
###################################################################################
#                                                                                 #
# NAME: setup.py                                                                  #
#                                                                                 #
# AUTHOR: Michael Brockus.                                                        #
#                                                                                 #
# CONTACT: <mailto:michael@squidfarts.com>                                        #
#                                                                                 #
# NOTICES:                                                                        #
#                                                                                 #
# License: LGPL                                                                   #
#                                                                                 #
###################################################################################
from setuptools import setup
from app.src.main.appinfo import MesonUiPyPiInfo

pypi_info: MesonUiPyPiInfo = MesonUiPyPiInfo()

pypi_info.required_version()

package_list = [
    'app',
    'app.src',
    'app.src.main.view',
    'app.src.main.mvc',
    'app.src.main.ui',
    'app.src.main.mesonuilib.introspection',
    'app.src.main.mesonuilib.ninjabuilder',
    'app.src.main.mesonuilib.backends',
    'app.src.main.mesonuilib.console',
    'app.src.main.mesonuilib.meson'
]


setup(
    name        =pypi_info.get_name(),
    version     =pypi_info.get_version(),
    description =pypi_info.get_description(),
    author      =pypi_info.get_author(),
    author_email=pypi_info.get_gmail(),
    license     =pypi_info.get_license(),
    zip_safe=True,
    include_package_data=True,
    packages=package_list,
    entry_points={
        'gui_scripts': ['meson-ui=app.__main__:mesonui_main']
    },
    install_requires=['PyQt5']
)
