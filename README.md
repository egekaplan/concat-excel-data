# Concat Excel Data and Plot Size Distribution

This project demonstrates how to read multiple Excel files from a specific directory, concatenate the data into a single DataFrame, and then plot the distribution of file sizes.

## Project Structure

```
├── README.md
├── files_here
│   ├── 
├── get_data.py
├── plot_graph.py
└── requirements.txt
```

### Files Description

- `get_data.py`: Python script to read Excel files from the `files_here` directory, concatenate them into a single DataFrame, and cache the result.

- `plot_graph.py`: Python script to plot the distribution of file sizes from the concatenated DataFrame and save the plot as a PNG file.

- `cached_df.pkl`: Pickle file storing the cached DataFrame after concatenation.

- `files_here/`: Directory containing sample Excel files for demonstration.

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

1. Ensure your Excel files are placed in the `files_here` directory.

2. Run `get_data.py` to read and concatenate the Excel files:
   ```bash
   python get_data.py
   ```

   This will generate a cached DataFrame `cached_df.pkl`.

3. Run `plot_graph.py` to plot the size distribution of the files:
   ```bash
   python plot_graph.py
   ```

   The resulting bar chart will be saved as `file_size_bar_chart.png`.

## Notes

- Ensure that you have Python installed on your system.

- Additional libraries such as `pandas`, `matplotlib`, and `seaborn` are required. These dependencies are listed in `requirements.txt`.

- Modify the `sheet_name` and `header_row` variables in `get_data.py` according to your Excel file structure.
