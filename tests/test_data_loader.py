import unittest
from src.data_loader import DataLoader

class TestDataLoader(unittest.TestCase):
    def test_load_data(self):
        loader = DataLoader('data/data.csv')
        data = loader.load_data()
        self.assertFalse(data.empty)

    def test_preprocess_data(self):
        loader = DataLoader('data/data.csv')
        data = loader.load_data()
        preprocessed_data = loader.preprocess_data(data)
        self.assertFalse(preprocessed_data.isnull().values.any())

if __name__ == '__main__':
    unittest.main()
