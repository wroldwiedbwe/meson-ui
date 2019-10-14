#!/user/bin/env python3
###################################################################################
#                                                                                 #
# NAME: ninjabuilder.py                                                           #
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


class NinjaBuilder:
    def __init__(self, parent = None):
        self._parent = parent
    # end of method

    def build(self) -> None:
        self._run(['-C', self._parent._project.get_build()])
    # end of method

    def clean(self) -> None:
        self._run(['-C', self._parent._project.get_build(), 'clean'])
    # end of method

    def install(self) -> None:
        self._run(['-C', self._parent._project.get_build(), 'install'])
    # end of method

    def _run(self, args: list) -> None:
        self._parent._process.waitForStarted()
        self._parent._process.start('ninja', args)
        self._parent._process.waitForFinished()
    # end of method