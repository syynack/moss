import sys
import os

from moss.framework.core.endpoint import Endpoint
from moss.framework.core.module import ModuleResult, execute_device_operation
from moss.framework.decorators import register, run
from moss.framework.core.etc import diagnose_interfaces

from glob import glob

sys.path.append(os.getcwd())

for x in glob(os.path.join(os.getcwd(), '*.py')):
    if not x.startswith('__'):
        __import__(os.path.basename(x)[:-3], globals(), locals())
