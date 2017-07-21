
import os
from glob import glob

for x in glob(os.path.join(os.path.dirname(__file__), '*.py')):
    if not x.startswith('__'):
        __import__(os.path.basename(x)[:-3], globals(), locals())
