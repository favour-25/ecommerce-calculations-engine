import sys
import os

# Force Python to see this folder so it can find 'src'
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import unittest

loader = unittest.TestLoader()
suite = loader.discover('tests')
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)