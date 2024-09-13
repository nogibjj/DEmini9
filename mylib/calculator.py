import pandas as pd
import matplotlib.pyplot as plt

# dataset = "https://projects.fivethirtyeight.com/nba-model/2023/latest_RAPTOR_by_player.csv"

def load_dataset(dataset):
    df = pd.read_csv(dataset)
    return df


def grab_mean(df, col):
    return df[col].mean()



def create_histogram(df, col):
    if col not in df.columns:
        raise ValueError(f"Column '{col}' not found in DataFrame")

    # Plot the histogram
    plt.figure(figsize=(8, 6))
    plt.hist(df[col], bins=30, color='blue', edgecolor='black')
    
    # Add title and labels
    plt.title(f'Histogram of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')

    # Show the plot
    plt.show()

def grab_median(df, col):
    return df[col].median()

def grab_STD(df,col):
    return df[col].std()

def grab_max(df,col):
    return df[col].max()
