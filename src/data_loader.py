# src/data_loader.py
import pandas as pd

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        try:
            return pd.read_csv(self.file_path)
        except pd.errors.EmptyDataError:
            print(f"Error: The file at {self.file_path} is empty or does not exist.")
            return pd.DataFrame()  # Return an empty DataFrame or handle as needed
        except FileNotFoundError:
            print(f"Error: The file at {self.file_path} was not found.")
            return pd.DataFrame()  # Return an empty DataFrame or handle as needed
