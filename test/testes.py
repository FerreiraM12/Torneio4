from src.projeto import projeto
import unittest


class projetoTest(unittest.TestCase):

    def test_projeto_1(self):
        with test_timeout(self, 2):
            m = [[None, None, None, None],
                 [None, 4, None, None],
                 [None, None, None, None],
                 [None, None, None, 3]]
            v = ([3, 2, 2, 1], [1, 3, 2, 2], [4, 2, 3, 1], [1, 2, 2, 2])
            self.assertEqual(projeto(m, *v), [[1, 2, 3, 4], [3, 4, 1, 2], [2, 3, 4, 1], [4, 1, 2, 3]])

    def test_projeto_2(self):
        with test_timeout(self, 2):
            m = [[None, None, 2],
                 [None, 3, None],
                 [None, None, None]]
            v = ([None, None, None], [None, None, None], [None, None, None], [None, None, None])
            self.assertEqual(projeto(m, *v), [[3, 1, 2], [2, 3, 1], [1, 2, 3]])


if __name__ == '__main__':
    unittest.main()

import time
import signal


class TestTimeout(Exception):
    pass


class test_timeout:
    def __init__(self, test, seconds, error_message=None):
        if error_message is None:
            error_message = 'test timed out after {}s.'.format(seconds)
        self.seconds = seconds
        self.error_message = error_message
        self.test = test

    def handle_timeout(self, signum, frame):
        raise TestTimeout(self.error_message)

    def __enter__(self):
        signal.signal(signal.SIGALRM, self.handle_timeout)
        signal.alarm(self.seconds)

    def __exit__(self, exc_type, exc_val, exc_tb):
        signal.alarm(0)
        if exc_type is not None and exc_type is not AssertionError:
            self.test.fail("execution error")