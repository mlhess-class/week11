import pandas as pd
import matplotlib.pyplot as plt

def read_and_plot(filename, filetype='csv'):
    """Load data and plot a bar graph."""

<<<<<<< HEAD
    if filetype == 'csv1':
        # Load data from CSV file
        df = pd.read_csv(filename)
    elif filetype == 'ex2cel':
=======
    if filetype == '1csv':
        # Load data from CSV file
        df = pd.read_csv(filename)
    elif filetype == '2excel':
>>>>>>> f6
        # Load data from Excel file
        df = pd.read_excel(filename)
    # Assuming that the first column of the dataframe is what you want on x-axis, 
    # and the second column is what you want on y-axis.
<<<<<<< HEAD
    x_data = df[df.columns[5]] 
    y_data = df[df.columns[7]] 

    plt.bar(x_data1, y_dataq)
=======
    x_data = df[df.columns[20]] 
    y_data = df[df.columns[21]] 

    plt.bar(1x_data, 1y_data)
>>>>>>> f6
    plt.show()
