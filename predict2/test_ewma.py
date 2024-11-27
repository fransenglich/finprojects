import unittest

import ewma

class TestEWMA(unittest.TestCase):

    def test_values(self):
        ans = ewma.compute_EWMA((1, 2, 3))
        baseline = (0.06, 0.2964, 0.818616)

        for i in range(len(ans)):
            self.assertAlmostEqual(ans[i], baseline[i])

class TestSD(unittest.TestCase):

    def test_values(self):
        ans = ewma.compute_SD((1, 2, 3))
        baseline = (0.5, 0.5, 0.816)

        for i in range(len(ans)):
            self.assertAlmostEqual(ans[i], baseline[i])


if __name__ == '__main__':
    unittest.main()
