import unittest
from src.metrics_calculator import MetricsCalculator

class TestMetricsCalculator(unittest.TestCase):
    def test_calculate_gini(self):
        data = [1, 1, 0, 0]
        gini = MetricsCalculator.calculate_gini(data)
        self.assertAlmostEqual(gini, 0.5)

    def test_calculate_entropy(self):
        data = [1, 1, 0, 0]
        entropy = MetricsCalculator.calculate_entropy(data)
        self.assertAlmostEqual(entropy, 1.0)

if __name__ == '__main__':
    unittest.main()
