import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def load_data(file_path):
    """Load the dataset."""
    data = pd.read_csv(file_path)
    return data

def preprocess_data(data):
    # Selects only numeric columns
    numeric_columns = data.select_dtypes(include=["number"])
    # Fill NaN in numeric columns with the mean
    data[numeric_columns.columns] = numeric_columns.apply(lambda col: col.fillna(col.mean()), axis=0)

    # Optionally handle non-numeric columns if needed 
    non_numeric_columns = data.select_dtypes(exclude=["number"])
    data[non_numeric_columns.columns] = non_numeric_columns.fillna("Unknown")  

    return data

    # Calculate Heat Index (HI)
    def calculate_heat_index(temp, humidity):
        return -42.379 + 2.04901523 * temp + 10.14333127 * humidity - \
               0.22475541 * temp * humidity - 6.83783e-3 * temp**2 - \
               5.481717e-2 * humidity**2 + 1.22874e-3 * temp**2 * humidity + \
               8.5282e-4 * temp * humidity**2 - 1.99e-6 * temp**2 * humidity**2

    data['Heat_Index'] = data.apply(lambda x: calculate_heat_index(x['Temperature'], x['Humidity']), axis=1)

    # Normalize data
    scaler = MinMaxScaler()
    data[['Temperature', 'Humidity', 'Heat_Index']] = scaler.fit_transform(data[['Temperature', 'Humidity', 'Heat_Index']])
    return data
