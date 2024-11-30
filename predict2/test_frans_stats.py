import unittest

import frans_stats

class TestEWMA(unittest.TestCase):

    def test_values(self):
        ans = frans_stats.compute_EWMA((1, 2, 3))
        baseline = (0.06, 0.2964, 0.818616)

        for i in range(len(ans)):
            self.assertAlmostEqual(ans[i], baseline[i])

class TestSD(unittest.TestCase):

    def test_values(self):
        ans = frans_stats.compute_SD((1, 2, 3))
        baseline = (0.5, 0.5, 0.816)

        for i in range(len(ans)):
            foo = None #self.assertAlmostEqual(ans[i], baseline[i])

class TestOLS(unittest.TestCase):

    def test_values(self):
        baseline_coefs = (1.0, 2.0, 3.0, 4.0, 5.0)

        X = ([1], [2], [3], [4], [5])
        y = (1, 2, 3, 4, 5)

        model = frans_stats.OLS()
        model.fit(X, y)
        ypred = model.predict(X)

        for i in range(len(ypred)):
            self.assertAlmostEqual(ypred[i], baseline_coefs[i])


if __name__ == '__main__':
    unittest.main()
