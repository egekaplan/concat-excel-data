# Concat Excel Data and Plot Size Distribution

This project demonstrates how to read multiple Excel files from a specific directory, concatenate the data into a single DataFrame, and then plot the distribution of file sizes.

## Project Structure

```
├── README.md│   
├── requirements.txt
├── src
│   │   
│   ├── cached_df
│   │   └── .gitkeep
│   ├── data_visualization
│   │   └── .gitkeep
│   │   
│   ├── files_here
│   │   └── .gitkeep
│   ├── get_data.py
│   └── plot_graph.py
└── .gitignore
```

### Files Description

- `get_data.py`: Python script to read Excel files from the `src/files_here` directory, concatenate them into a single DataFrame, and cache the result.

- `plot_graph.py`: Python script to plot the distribution of file sizes from the concatenated DataFrame and save the plot as a PNG file.

- `src/files_here/`: Directory containing Excel files to read

- `cached_df.pkl`: Pickle file storing the cached DataFrame after concatenation.

- `src/cached_df/`: Directory containing pickled DataFrame after concatenation.

- `src/data_visualization/`: Directory for generated graphs

## Setup and Execution

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/egekaplan/concat-excel-data.git
   ```

2. Navigate to the project directory:
   ```bash
   cd concat-excel-data
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. Ensure your Excel files are placed in the `src/files_here` directory.

2. Run `src/get_data.py` to read and concatenate the Excel files:
   ```bash
   python3 get_data.py
   ```

   This will generate a cached DataFrame `cached_df.pkl` in `src/cached_df/cached_df.pkl`.

3. Run `src/plot_graph.py` to plot the size distribution of the files:
   ```bash
   python3 plot_graph.py
   ```

   The resulting histogram chart will be saved as `file_size_histogram.png` and `extension_frequency_histogram`.

## Notes

- Ensure that you have Python installed on your system.

- Additional libraries such as `pandas`, `matplotlib`, and `seaborn` are required. These dependencies are listed in `requirements.txt`.

- Modify the `sheet_name` and `header_row` variables in `get_data.py` according to your Excel file structure.
