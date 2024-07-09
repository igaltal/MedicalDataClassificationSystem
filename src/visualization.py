import matplotlib.pyplot as plt
import seaborn as sns

class Visualization:
    @staticmethod
    def plot_results(results):
        for criterion, score in results.items():
            plt.bar(criterion, score)
        plt.xlabel('Criterion')
        plt.ylabel('Accuracy')
        plt.title('Comparison of Decision Tree Criteria')
        plt.show()
