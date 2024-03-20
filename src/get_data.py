import os
import pickle
import pandas as pd

from pathlib import Path

# Get pwd, current directory
CURRENT_FOLDER = os.getcwd()
print("Current Folder:", CURRENT_FOLDER)

FOLDER_NAME = "files_here"

# Path to folder
FOLDER_PATH = os.path.join(CURRENT_FOLDER, FOLDER_NAME)

EXCEL_FILES = []

# Check if the folder exists
if os.path.exists(FOLDER_PATH) and os.path.isdir(FOLDER_PATH):
    files_in_folder = os.listdir(FOLDER_PATH)

    print("Reading files in '{}' folder:".format(FOLDER_NAME))
    for filename in files_in_folder:
        EXCEL_FILES.append(filename)
else:
    print("Folder '{}' does not exist or is not a directory.".format(FOLDER_NAME))

print(f"Files to read: {EXCEL_FILES}")

# My static excel df start column, also sheet name... one may change as they wish
SHEET_NAME = "Files"
HEADER_ROW = 9


def read_excel_file(file):
    """Read single excel data, generate df"""
    try:
        df = pd.read_excel(
            f"{FOLDER_PATH}/{file}",
            sheet_name=SHEET_NAME,
            header=HEADER_ROW - 1,
            index_col=1,
            engine="openpyxl",
        )
    except FileNotFoundError:
        print(f"Error: File '{file}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred while reading the Excel file '{file}': {e}")
        return None
    return df


def read_concat_EXCEL_FILES(files):
    """Concat df's"""
    dfs = []
    for file in files:
        df = read_excel_file(file)
        if df is not None:
            dfs.append(df)

    concatenated_df = pd.concat(dfs)
    return concatenated_df


# Check if cached file exists
cached_file = f"cached_df/cached_df.pkl"
if os.path.exists(cached_file):
    print("Loading DataFrame from cache...")
    with open(cached_file, "rb") as f:
        concatenated_df = pickle.load(f)
else:
    print("Cached DataFrame not found. Generating and caching...")
    concatenated_df = read_concat_EXCEL_FILES(EXCEL_FILES)
    with open(cached_file, "wb") as f:
        pickle.dump(concatenated_df, f)


# Get the number of rows in the concatenated DataFrame
def get_num_rows(df):
    """ 
    Get total number of rows for a dataframe
    """
    num_rows = df.shape[0]
    return num_rows


def get_frequencies(df, decimal_places=0, sort_by='index'):
    """
    Get frequency info for a dataframe.
    """
    try:
        # Specify the column for which you want to calculate frequencies
        column_name = "Size (MB)"

        # Round the 'Size (MB)' column to the desired decimal places
        df["Size (MB)"] = df["Size (MB)"].round(decimal_places)

        # Get frequencies for the specified column
        frequency = df[column_name].value_counts()

        # Sort the frequencies
        if sort_by == 'index':
            frequency = frequency.sort_index()
        elif sort_by == 'values':
            frequency = frequency.sort_values()
        else:
            print("Invalid 'sort_by' parameter. Sorting by index.")
            frequency = frequency.sort_index()

        # Convert the Series to a dictionary
        frequencies_dict = frequency.to_dict()

        return frequencies_dict, frequency
    except Exception as e:
        print(f"An error occurred while getting frequencies: {e}")
        return None
    
def get_size_portion(frequency, percent=0.80):
    """
    Get the interval that sums up to a certain percentage of total frequencies.
    """

    num_rows = frequency.sum()
    print(f"num rows \n {num_rows}")

    # Sort the frequency in ascending order of 'Size (MB)'
    sorted_frequency = frequency.sort_index(ascending=True)

    # Calculate the cumulative sum of frequencies
    cumulative_sum = sorted_frequency.cumsum()

    print(f"cuml sum: \n {cumulative_sum}")

    # Find the index where cumulative sum reaches the specified percentage
    index = cumulative_sum[cumulative_sum <= (percent * num_rows)].index.max()

    # Get the interval bounds
    lower_bound = cumulative_sum.index.min()
    upper_bound = index

    return lower_bound, upper_bound


def get_extension_count(df):
    """
    Get extension frequency
    """
    try:
        # Specify the column for which you want to get the file extension
        column_name = "Filename"

        # Extract file extensions from the "Filename" column using pathlib
        df["File Extension"] = df[column_name].apply(lambda x: Path(x).suffix.lower())

        # Get frequencies for the file extensions
        extension_frequency = df["File Extension"].value_counts()

        return extension_frequency
    except Exception as e:
        print(f"An error occurred while getting extension frequencies: {e}")
        return None

# Enable to display all rows
# pd.set_option("display.max_rows", None)

# Get the file extension frequencies
extension_frequency = get_extension_count(concatenated_df)
# print("File Extension Frequencies:")
# print(extension_frequency)

show_freq, freq = get_frequencies(concatenated_df, decimal_places=1)
# print(freq)

# Get the Size (MB) interval for the first 80% of frequencies
lower_bound, upper_bound = get_size_portion(freq)
# print("Interval for the first 80% of frequencies:")
# print(f"Lower Bound: {lower_bound}")
# print(f"Upper Bound: {upper_bound}")


# Reset pandas display options to default
#pd.reset_option("display.max_rows")
