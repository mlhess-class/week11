import pandas as pd
import matplotlib.pyplot as plt

def read_and_plot(filename, filetype='csv'):
    """Load data and plot a bar graph."""

    if filetype == 'csv':
        # Load data from CSV file
        df = pd.read_csv(filename)
    elif filetype == 'excel':
        # Load data from Excel file
        df = pd.read_excel(filename)
    # Assuming that the first column of the dataframe is what you want on x-axis, 
    # and the second column is what you want on y-axis.
    x_data = df[df.columns[0]] 
    y_data = df[df.columns[1]] 

    plt.bar(x_data, y_data)
    plt.show()
