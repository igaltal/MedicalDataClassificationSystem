import numpy as np

class MetricsCalculator:
    @staticmethod
    def calculate_gini(data):
        _, counts = np.unique(data, return_counts=True)
        probabilities = counts / counts.sum()
        gini = 1 - np.sum(probabilities**2)
        return gini

    @staticmethod
    def calculate_entropy(data):
        _, counts = np.unique(data, return_counts=True)
        probabilities = counts / counts.sum()
        entropy = -np.sum(probabilities * np.log2(probabilities))
        return entropy

    @staticmethod
    def calculate_gain_ratio(data):
        # Placeholder function
        pass

    @staticmethod
    def calculate_split_info(data):
        # Placeholder function
        pass

    @staticmethod
    def calculate_chi_square(data):
        # Placeholder function
        pass
