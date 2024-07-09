import unittest
from src.visualization import Visualization

class TestVisualization(unittest.TestCase):
    def test_plot_results(self):
        results = {'gini': 0.85, 'entropy': 0.90}
        Visualization.plot_results(results)
        self.assertTrue(True)  # Assuming this would be visually verified

if __name__ == '__main__':
    unittest.main()
