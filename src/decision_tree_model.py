from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import matplotlib.pyplot as plt

class DecisionTreeModel:
    def __init__(self, criterion='gini'):
        self.criterion = criterion
        self.model = DecisionTreeClassifier(criterion=self.criterion)

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def evaluate(self, X_test, y_test):
        return self.model.score(X_test, y_test)

    def visualize_tree(self, feature_names, class_names):
        plt.figure(figsize=(20,10))
        tree.plot_tree(self.model, feature_names=feature_names, class_names=class_names, filled=True)
        plt.show()
