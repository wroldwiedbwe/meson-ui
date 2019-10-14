#!/user/bin/env python3
###################################################################################
#                                                                                 #
# NAME: testrun.py                                                                #
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
import subprocess


subprocess.check_call(['pytest', '-v', 'run_utests.py'])
subprocess.check_call(['pytest', '-v', 'run_uitests.py'])