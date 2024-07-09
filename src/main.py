#System/src/main.py
from sklearn.model_selection import train_test_split
from data_loader import DataLoader
from decision_tree_model import DecisionTreeModel
from visualization import Visualization

class Main:
    @staticmethod
    def run(file_path):
        data_loader = DataLoader(file_path)
        data = data_loader.load_data()
        data = data_loader.preprocess_data(data)

        # Assuming the last column is the target variable
        X = data.iloc[:, :-1]
        y = data.iloc[:, -1]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        criteria = ['gini', 'entropy']
        results = {}

        for criterion in criteria:
            model = DecisionTreeModel(criterion=criterion)
            model.train(X_train, y_train)
            score = model.evaluate(X_test, y_test)
            results[criterion] = score
            model.visualize_tree(feature_names=X.columns, class_names=y.unique().astype(str))

        Visualization.plot_results(results)

if __name__ == "__main__":
    Main.run('data/data.csv')
