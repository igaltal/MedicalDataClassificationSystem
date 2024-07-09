# src/metrics_calculator.py
import numpy as np
from scipy.stats import chi2_contingency

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
    def calculate_gain_ratio(data, target):
        def calculate_information_gain(data, target):
            total_entropy = MetricsCalculator.calculate_entropy(target)
            values, counts = np.unique(data, return_counts=True)
            weighted_entropy = np.sum([
                (counts[i] / np.sum(counts)) * MetricsCalculator.calculate_entropy(target[data == values[i]])
                for i in range(len(values))
            ])
            information_gain = total_entropy - weighted_entropy
            return information_gain

        def calculate_split_info(data):
            _, counts = np.unique(data, return_counts=True)
            probabilities = counts / counts.sum()
            split_info = -np.sum(probabilities * np.log2(probabilities))
            return split_info

        information_gain = calculate_information_gain(data, target)
        split_info = calculate_split_info(data)
        gain_ratio = information_gain / split_info if split_info != 0 else 0
        return gain_ratio

    @staticmethod
    def calculate_split_info(data):
        _, counts = np.unique(data, return_counts=True)
        probabilities = counts / counts.sum()
        split_info = -np.sum(probabilities * np.log2(probabilities))
        return split_info

    @staticmethod
    def calculate_chi_square(data, target):
        contingency_table = np.array([
            np.histogram(data[target == t], bins=np.unique(data))[0]
            for t in np.unique(target)
        ])
        chi2, p, dof, expected = chi2_contingency(contingency_table)
        return chi2, p, dof, expected
