import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pickle

def plot_size_bar_chart(df, output_file):
    """
    Plotting Size Bar Chart from the provided DataFrame and save as PNG
    """
    # Round the 'Size (MB)' column to 1 decimal place
    df['Size (MB)'] = df['Size (MB)'].round(0)

    # Group sizes greater than 10 MB into a single category
    df['Size (MB)'] = df['Size (MB)'].apply(lambda x: x if x <= 10 else 10)

    # Count the number of files for each unique size
    size_counts = df['Size (MB)'].value_counts().sort_index()

    # If there are files > 10 MB, add a '>10 MB' category
    if (df['Size (MB)'] > 10).any():
        size_counts.loc['>10 MB'] = (df['Size (MB)'] > 10).sum()

    # Create the bar chart
    plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
    size_counts.plot(kind='bar', color='skyblue')
    plt.xlabel('Size (MB)')
    plt.ylabel('File Count')
    plt.title('File Size Distribution')
    
    # Update x-axis labels to show '>10 MB' instead of '10'
    plt.xticks(range(len(size_counts)), [str(x) if x <= 10 else '>10 MB' for x in size_counts.index], rotation=45, ha='right')
    
    plt.tight_layout()

    # Save the plot as a PNG file
    plt.savefig(output_file)
    plt.close()

def main():
    # Check if cached file exists
    cached_file = "cached_df.pkl"
    if not os.path.exists(cached_file):
        print("Cached DataFrame file not found. Please generate the DataFrame first.")
        return

    # Load the DataFrame from the cached file
    with open(cached_file, "rb") as f:
        concatenated_df = pickle.load(f)

    # Print a sample of the DataFrame
    print("Sample of the DataFrame:")
    print(concatenated_df.head())

    # Define the output PNG file
    output_png = "file_size_bar_chart.png"

    # Call the plot function with the output file
    plot_size_bar_chart(concatenated_df, output_png)

    print(f"Bar chart saved as {output_png}")

if __name__ == "__main__":
    main()
