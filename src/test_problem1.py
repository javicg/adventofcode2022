import unittest

import src.problem1 as problem


class TestProblem(unittest.TestCase):
    def test_sample1(self):
        self.assertEqual(problem.solve("resources/samples/sample1.csv"), "99")
