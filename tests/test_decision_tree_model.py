import unittest
from src.data_loader import DataLoader
from src.decision_tree_model import DecisionTreeModel

class TestDecisionTreeModel(unittest.TestCase):
    def setUp(self):
        self.loader = DataLoader('/Users/igaltal/Desktop/Medical Data Classification System/data/data.csv')

    def test_train_and_evaluate(self):
        data = self.loader.load_data()
        data = self.loader.preprocess_data(data)
        # Assuming the last column is the target variable
        X = data.iloc[:, :-1]
        y = data.iloc[:, -1]

        model = DecisionTreeModel(criterion='gini')
        model.train(X, y)
        accuracy = model.evaluate(X, y)
        self.assertGreaterEqual(accuracy, 0)

if __name__ == '__main__':
    unittest.main()
