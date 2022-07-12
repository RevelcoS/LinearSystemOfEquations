import unittest
from eq_solver import solve

class TestEq(unittest.TestCase):

    def test_4by4(self):
        A = [
            [7, -6, -4, -8],
            [10, -9, 2, -3],
            [-5, 7, 1, 5],
            [-2, 8, -3, 1]
        ]

        X = [56, 70, -52, -45]
        self.assertEqual(solve(A, X), (2, -3, 4, -5))

    def test_3by3(self):
        A = [
            [1, 2, 3],
            [2, -3, 4],
            [4, -2, 3]
        ]

        X = [14, 8, 9]
        self.assertEqual(solve(A, X), (1, 2, 3))
    
    def test_2by2(self):
        A = [
            [2, 1],
            [3, -2]
        ]

        X = [8, -2]
        self.assertEqual(solve(A, X), (2, 4))
    
    def test_1by1(self):
        A = [
            [2]
        ]

        X = [2]
        self.assertEqual(solve(A, X), (1, ))

    def test_float(self):
        A = [
            [7, 3],
            [-14, 6]
        ]

        X = [3, 2]
        self.assertEqual(solve(A, X), (1/7, 2/3))

if __name__ == "__main__":
    unittest.main()