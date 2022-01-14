from semid.app import Semid
from semid.app.argapp import SemidArgs
from colorama import init
import sys
init()
if len(sys.argv) < 1:
    __app__ = Semid()
else:
    __app__ = SemidArgs()
author = "Hima"
date = "01/13/22"
