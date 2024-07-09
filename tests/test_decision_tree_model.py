import unittest
from sklearn.model_selection import train_test_split
from src.data_loader import DataLoader
from src.decision_tree_model import DecisionTreeModel

class TestDecisionTreeModel(unittest.TestCase):
    def test_train_and_evaluate(self):
        loader = DataLoader('data/data.csv')
        data = loader.load_data()
        data = loader.preprocess_data(data)

        X = data.iloc[:, :-1]
        y = data.iloc[:, -1]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model = DecisionTreeModel(criterion='gini')
        model.train(X_train, y_train)
        score = model.evaluate(X_test, y_test)
        self.assertGreater(score, 0.5)

if __name__ == '__main__':
    unittest.main()
