import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label="Data", color="blue")

    # Create first line of best fit
    slope_all, intercept_all, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_all = range(1880, 2051)
    y_all = [slope_all * year + intercept_all for year in x_all]
    plt.plot(x_all, y_all, label="Best Fit Line (All Data)", color="red")

    # Create second line of best fit
    df_2000 = df[df['Year'] >= 2000]
    slope_2000, intercept_2000, _, _, _ = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    x_2000 = range(2000, 2051)
    y_2000 = [slope_2000 * year + intercept_2000 for year in x_2000]
    plt.plot(x_2000, y_2000, label="Best Fit Line (2000 Onwards)", color="green")

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()
    plt.grid()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
