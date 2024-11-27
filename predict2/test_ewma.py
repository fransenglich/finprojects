import unittest

import ewma

class TestSum(unittest.TestCase):

    def test_values(self):
        ans = ewma.compute_EWMA((1, 2, 3))
        baseline = (0.06, 0.2964, 0.8186)

        for i in list(range(len(ans))):
            self.assertAlmostEqual(ans[i], baseline[i])

if __name__ == '__main__':
    unittest.main()
