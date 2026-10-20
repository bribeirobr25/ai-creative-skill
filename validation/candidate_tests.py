"""Candidate suite. Original packaging tests remain owned by release_integrity."""
import sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
if __name__=='__main__':
    loader=unittest.TestLoader();suite=unittest.TestSuite()
    for path in sorted((ROOT/'tests').glob('test_*.py')):
        if path.name=='test_packaging.py':continue  # executed unchanged on pinned V2.5 in the separate required gate
        suite.addTests(unittest.TestLoader().discover(str(ROOT/'tests'),pattern=path.name))
    suite.addTests(unittest.TestLoader().discover(str(ROOT/'src/ai-creative-skill/web/tests'),pattern='test_*.py'))
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(not result.wasSuccessful())
