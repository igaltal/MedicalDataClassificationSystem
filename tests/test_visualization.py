import unittest
from src.visualization import Visualization

class TestVisualization(unittest.TestCase):
    def test_plot_results(self):
        results = {'gini': 0.8, 'entropy': 0.75}
        Visualization.plot_results(results)
        # Since this is a visual test, you would normally check for the creation of a plot file or similar

if __name__ == '__main__':
    unittest.main()
