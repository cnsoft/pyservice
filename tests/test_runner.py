import sys
import unittest

from pyservice import runner
from cStringIO import StringIO

sys.stdout = my_stdout = StringIO()
sys.stderr = my_stderr = StringIO()
sys.exit = lambda x: x


class RunnerTests(unittest.TestCase):
        
    def test_runner_check_version(self):
        sys.argv = list()    
        sys.argv.append('pyservice.py')
        sys.argv.append('-v')
        runner.run_service()

    def test_runner_show_help(self):
        sys.argv = list()    
        sys.argv.append('pyservice.py')
        sys.argv.append('-h')
        runner.run_service()

    def test_runner_by_pid(self):
        sys.argv = list()    
        sys.argv.append('pyservice.py')
        sys.argv.append('-p')
        sys.argv.append('1000')
        runner.run_service()

    def test_runner_by_process_name(self):
        sys.argv = list()    
        sys.argv.append('pyservice.py')
        sys.argv.append('dummy_process')
        sys.argv.append('start')
        runner.run_service()

    def test_runner_by_process_name_no_action(self):
        sys.argv = list()    
        sys.argv.append('pyservice.py')
        sys.argv.append('dummy_process')
        runner.run_service()


if __name__ == '__main__':
    unittest.main()        
    
