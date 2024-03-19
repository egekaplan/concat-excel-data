import pandas as pd
import matplotlib.pyplot as plt
import os

# Get pwd, current directory
current_folder = os.getcwd()
print("Current Folder:", current_folder)
folder_name = "files_here"

# Path to folder
folder_path = os.path.join(current_folder, folder_name)

excel_files = []

# Check if the folder exists
if os.path.exists(folder_path) and os.path.isdir(folder_path):
    files_in_folder = os.listdir(folder_path)

    print("Filenames in the '{}' folder:".format(folder_name))
    for filename in files_in_folder:
        excel_files.append(filename)
else:
    print("Folder '{}' does not exist or is not a directory.".format(folder_name))

print(f"files to read: {excel_files}")

# My static excel df start column, also sheet name... you may change as u wish
sheet_name = "Sayfa1"  
header_row = 9  

def read_excel_file(file):
    """read single excel data, generate df
    """
    try:
        df = pd.read_excel(f"{folder_path}/{file}", sheet_name=sheet_name, header=header_row-1, index_col=1, engine='openpyxl')
    except FileNotFoundError:
        print(f"Error: File '{file}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred while reading the Excel file '{file}': {e}")
        return None
    return df

def read_concat_excel_files(files):
    """concat df's
    """
    dfs = []
    for file in files:
        df = read_excel_file(file)
        if df is not None:
            dfs.append(df)

    concatenated_df = pd.concat(dfs)
    return concatenated_df

# Concat all dfs in "files_here" folder into a single df (for excel cells B9 to H9 incl. headers)
concatenated_df = read_concat_excel_files(excel_files)

print(concatenated_df)