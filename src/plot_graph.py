import os
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pickle

from get_data import get_num_rows, get_frequencies, get_extension_count


def plot_size_histogram(df, output_file, sizes, bins):
    """
    Plotting Size Histogram from the provided DataFrame and save as PNG
    """
    # Get total number of rows
    num_rows = get_num_rows(df)

    # Create the histogram
    plt.figure(figsize=(12, 8))  # Adjust the figure size as needed

    # Plot the histogram
    plt.hist(sizes, bins=bins, color='black', edgecolor='black', alpha=0.5)

    # Adding labels and title
    plt.xlabel('Size (MB)')
    plt.ylabel('Count')
    plt.title('Size Frequency')

    # Adding total number of rows as a legend
    plt.legend([f'Total Files: {num_rows}'], loc='upper right')

    # cutoff till outliers
    plt.xlim(0, 10)

    # Save the plot as a PNG file
    plt.tight_layout()
    plt.savefig(output_file)
    plt.close()


def plot_extension_histogram(df, output_file, extension_count):
    """
    Plotting Extension Histogram from the provided DataFrame and save as PNG
    """
    # Get extension names and counts
    extensions = extension_count.index
    counts = extension_count.values

    # Create the histogram
    plt.figure(figsize=(12, 8))  # Adjust the figure size as needed

    # Plot the histogram
    plt.bar(extensions, counts, color='black', alpha=0.5)

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=90)

    # Adding labels and title
    plt.xlabel('Extension')
    plt.ylabel('Count')
    plt.title('Extension Frequency')

    # Save the plot as a PNG file
    plt.tight_layout()
    plt.savefig(output_file)
    plt.close()

def main():
    """
    Main function
    """
    # Cache check
    cached_file = "cached_df/cached_df.pkl"
    if not os.path.exists(cached_file):
        print("Cached DataFrame file not found. Please generate the DataFrame first.")
        return

    # Load the DataFrame from the cached file
    with open(cached_file, "rb") as f:
        concatenated_df = pickle.load(f)

    # Get the sizes (MB) from the DataFrame
    sizes = concatenated_df['Size (MB)']

    # Specify the number of bins for the histograms
    bins_size = np.arange(0, sizes.max() + 1, 0.1)  # Adjust bin size as needed

    # Define the output PNG files
    output_png_size = "data_visualization/file_size_histogram.png"
    output_png_extension = "data_visualization/extension_frequency_histogram.png"

    # Call the plot function with the output files
    plot_size_histogram(concatenated_df, output_png_size, sizes, bins_size)

    # Get the extension frequencies
    extension_count = get_extension_count(concatenated_df)

    # Call the plot function for extension frequencies
    plot_extension_histogram(concatenated_df, output_png_extension, extension_count)

    print(f"Histogram for file size saved as {output_png_size}")
    print(f"Histogram for extension frequencies saved as {output_png_extension}")

if __name__ == "__main__":
    main()
