import os
import pandas as pd


class GetData:
    def get_data(self):
        """
        Return a Python dict containing required csv files
        Its values should be pandas.DataFrames loaded from csv files
        """
        root_dir = os.path.dirname(os.path.dirname(__file__))
        csv_path = os.path.join(root_dir, "data")
        
        # Check if data folder is empty
        assert len(os.listdir(csv_path)) > 0, "No file in data folder, please check!"
        
        # Generate file name list
        file_names = [f for f in os.listdir(csv_path) if f.endswith(".csv")]
        
        key_names = [
            key_name.replace(".csv", "")
            for key_name in file_names
        ]

        # Create the dictionary
        data = {}
        for k, f in zip(key_names, file_names):
            data[k] = pd.read_csv(os.path.join(csv_path, f))
        
        print("Data dictionary generated")
        return data