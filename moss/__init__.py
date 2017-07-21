import sys
import os

from moss.endpoint import Endpoint
from moss.module import module
from glob import glob

sys.path.append(os.getcwd())

for x in glob(os.path.join(os.getcwd(), '*.py')):
    if not x.startswith('__'):
        __import__(os.path.basename(x)[:-3], globals(), locals())
