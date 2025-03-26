import pandas as pd

def fetch_data():
    try:
        path = 'all_macs/Known Mac address.xlsx'
        data = pd.read_excel(path)

        if 'Mac Address' not in data.columns:
            print("Mac Address column is missing in the data.")
            return pd.DataFrame()
        return data
    except FileNotFoundError:
        print('File Not Found')
        return pd.DataFrame()
    except Exception as e:
        print(f"An error occurred while fetching the data: {e}")
        return pd.DataFrame()
