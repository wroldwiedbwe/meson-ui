#!/user/bin/env python3
###################################################################################
#                                                                                 #
# NAME: run_uitests.py                                                            #
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
from app.src.main.mesonuilib.meson.mesonmanager import Meson
from os import path
import pytest

#
# This class is faking the apps projetc data
#
class FakeProg:
    dir_src = ''
    dir_build = ''
    def set_source(self, value: str) -> str:
        self.dir_src = value
    
    def set_build(self, value: str) -> str:
        self.dir_build = value
    
    def get_source(self) -> str:
        return self.dir_src
    
    def get_build(self) -> str:
        return self.dir_build



def test_meson_setup():
    prog = FakeProg()
    prog.set_source('test-cases/01-setup')
    prog.set_build('test-cases/01-setup/builddir')

    meson = Meson(prog)
    meson.setup()

    assert path.isdir('test-cases/01-setup/builddir')


def test_meson_build():
    prog = FakeProg()
    prog.set_source('test-cases/02-build')
    prog.set_build('test-cases/02-build/builddir')

    meson = Meson(prog)
    meson.setup()
    meson.build()

    assert path.isdir('test-cases/02-build/builddir')
    assert path.isfile('test-cases/02-build/builddir/build.ninja')


def test_meson_clean():
    prog = FakeProg()
    prog.set_source('test-cases/03-clean')
    prog.set_build('test-cases/03-clean/builddir')

    meson = Meson(prog)
    meson.setup()
    meson.build()
    # assert path.isfile('test-cases/03-clean/builddir/prog/src/c-exe')
    meson.clean()
    
    assert path.isdir('test-cases/03-clean/builddir')
    assert path.isfile('test-cases/03-clean/builddir/build.ninja')


def test_meson_configure():
    prog = FakeProg()
    prog.set_source('test-cases/04-configure')
    prog.set_build('test-cases/04-configure/builddir')

    meson = Meson(prog)
    meson.setup()
    meson.build()
    meson.configure(['--buildtype=minsize'])
    
    assert (meson.introspection('buildoptions').get_buildtype('value') == 'minsize')
    
    assert path.isdir('test-cases/04-configure/builddir')
    assert path.isfile('test-cases/04-configure/builddir/build.ninja')


def test_meson_introspection():
   prog = FakeProg()
   prog.set_source('test-cases/05-introspection')
   prog.set_build('test-cases/05-introspection/builddir')

   meson = Meson(prog)
   meson.setup()
   meson.build()

   assert (meson.introspection('projectinfo').get_name() == 'c-exe')
   assert (meson.introspection('targets-sources').get_language(0) == 'c')
   assert (meson.introspection('buildoptions').get_buildtype('value') == 'debug')

   assert path.isdir('test-cases/05-introspection/builddir')
   assert path.isfile('test-cases/05-introspection/builddir/build.ninja')
