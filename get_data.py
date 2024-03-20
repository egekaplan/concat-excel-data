import os
import pandas as pd
import pickle

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

    print("Reading files in '{}' folder:".format(folder_name))
    for filename in files_in_folder:
        excel_files.append(filename)
else:
    print("Folder '{}' does not exist or is not a directory.".format(folder_name))

print(f"Files to read: {excel_files}")

# My static excel df start column, also sheet name... you may change as u wish
sheet_name = "Files"
header_row = 9

def read_excel_file(file):
    """Read single excel data, generate df
    """
    try:
        df = pd.read_excel(f"{folder_path}/{file}", sheet_name=sheet_name,
                           header=header_row-1, index_col=1, engine='openpyxl')
    except FileNotFoundError:
        print(f"Error: File '{file}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred while reading the Excel file '{file}': {e}")
        return None
    return df

def read_concat_excel_files(files):
    """Concat df's
    """
    dfs = []
    for file in files:
        df = read_excel_file(file)
        if df is not None:
            dfs.append(df)

    concatenated_df = pd.concat(dfs)
    return concatenated_df

# Check if cached file exists
cached_file = "cached_df.pkl"
if os.path.exists(cached_file):
    print("Loading DataFrame from cache...")
    with open(cached_file, "rb") as f:
        concatenated_df = pickle.load(f)
else:
    print("Cached DataFrame not found. Generating and caching...")
    concatenated_df = read_concat_excel_files(excel_files)
    with open(cached_file, "wb") as f:
        pickle.dump(concatenated_df, f)

print(concatenated_df)

print('test branch')
