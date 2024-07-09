import pandas as pd

# Define the sample data
data = {
    'Age': [25, 35, 45, 50, 23, 31, 46, 57, 29, 41],
    'BloodPressure': [120, 130, 140, 135, 118, 128, 135, 142, 130, 133],
    'Cholesterol': [200, 210, 220, 215, 198, 205, 210, 220, 207, 213],
    'Diabetes': [0, 1, 0, 1, 0, 0, 1, 1, 0, 1]
}

# Convert the data to a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
file_path = '/Users/igaltal/Desktop/Medical Data Classification System/data/data.csv'
df.to_csv(file_path, index=False)

print(f"Data has been successfully saved to {file_path}")
