import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    x1 = df['Year']
    y1 = df['CSIRO Adjusted Sea Level']
    slope1, intercept1, _, _, _ = linregress(x1, y1)

    x1_pred = pd.Series(range(1880, 2051))
    y1_pred = intercept1 + slope1 * x1_pred

    plt.plot(x1_pred, y1_pred, 'r', label='Line of Best Fit')

    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]

    x2 = df_recent['Year']
    y2 = df_recent['CSIRO Adjusted Sea Level']
    slope2, intercept2, _, _, _ = linregress(x2, y2)

    x2_pred = pd.Series(range(2000, 2051))
    y2_pred = intercept2 + slope2 * x2_pred

    plt.plot(x2_pred, y2_pred, 'g', label='Line of Best Fit (2000+)')


    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()