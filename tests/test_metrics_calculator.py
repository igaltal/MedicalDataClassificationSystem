import unittest
import numpy as np
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

    def test_calculate_gain_ratio(self):
        data = np.array([1, 1, 0, 0])
        target = np.array([1, 0, 1, 0])
        gain_ratio = MetricsCalculator.calculate_gain_ratio(data, target)
        expected_gain_ratio = 0  # Adjust based on the actual calculation logic
        self.assertAlmostEqual(gain_ratio, expected_gain_ratio)

    def test_calculate_split_info(self):
        data = [1, 1, 0, 0]
        split_info = MetricsCalculator.calculate_split_info(data)
        expected_split_info = 1.0  # Adjust based on the actual calculation logic
        self.assertAlmostEqual(split_info, expected_split_info)

    def test_calculate_chi_square(self):
        data = np.array([1, 1, 0, 0])
        target = np.array([1, 0, 1, 0])
        chi2, p, dof, expected = MetricsCalculator.calculate_chi_square(data, target)
        self.assertAlmostEqual(chi2, 2.0, places=1)  # Adjust based on the actual calculation logic
        self.assertAlmostEqual(p, 0.157, places=3)  # Adjust based on the actual calculation logic
        self.assertEqual(dof, 1)
        self.assertEqual(expected.shape, (2, 2))

if __name__ == '__main__':
    unittest.main()
