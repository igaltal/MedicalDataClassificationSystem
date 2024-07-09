# tests/test_data_loader.py
import unittest
from src.data_loader import DataLoader

class TestDataLoader(unittest.TestCase):
    def setUp(self):
        self.loader = DataLoader('/Users/igaltal/Desktop/Medical Data Classification System/data/data.csv')

    def test_load_data(self):
        data = self.loader.load_data()
        self.assertFalse(data.empty)

    def test_preprocess_data(self):
        data = self.loader.load_data()
        data = self.loader.preprocess_data(data)
        self.assertFalse(data.empty)

if __name__ == '__main__':
    unittest.main()
