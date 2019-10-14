#!/user/bin/env python3
###################################################################################
#                                                                                 #
# NAME: run_install.py                                                            #
#                                                                                 #
# AUTHOR: Michael Brockus.                                                        #
#                                                                                 #
# CONTACT: <mailto:michaelbrockus@icloud.com>                                     #
#                                                                                 #
# NOTICES:                                                                        #
#                                                                                 #
# License: Apache 2.0 :http://www.apache.org/licenses/LICENSE-2.0                 #
#                                                                                 #
###################################################################################
import subprocess

apt_get_deps = [
    'git', 
    'gcc',
    'unzip',
    'libcurl3',
    'python3',
    'pkg-config', 
    'python3-pyqt5',
    'ninja-build',
    'build-essential']
    
pip_get_deps = [
    'meson',
    'PyQt5', 
    'codecov', 
    'pytest', 
    'pytest-qt', 
    'pyinstaller']

if __name__ == "__main__":
    for dep in apt_get_deps:
        subprocess.check_call(['apt-get', '-y', 'install', dep])

    subprocess.check_call(['pip3', 'install', '--upgrade', 'pip'])

    for dep in pip_get_deps:
        subprocess.check_call(['pip3', 'install', dep])