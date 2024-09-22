import pandas as pd
import matplotlib.pyplot as plt
# player_name	player_id	season	poss	mp

# Data Loading and Preprocessing:
def load_and_preprocess(csv):
    """loads the data"""
    general_df = pd.read_csv(csv)
    return general_df


# Data Operations
def process_mean(general_df, col):
    """returns the mean of a specific col in dataframe"""
    general_mean = general_df[col].mean()
    return general_mean


def process_median(general_df, col):
    """returns the median of a specific col in dataframe"""
    general_median = general_df[col].median()
    return general_median


def process_std(general_df, col):
    """returns the std of a specific col in dataframe"""
    general_std = general_df[col].std()
    return general_std


def process_quantile(general_df, col, quantile_num):
    """returns the quantile specified of a specific col in dataframe"""
    general_quantile = general_df[col].quantile(quantile_num)
    return general_quantile


# Data Vizualization
def NBA_histogram_poss(general_df, jupyter_render):
    """generate a histogram of poss of distbution of congress members"""
    plt.figure(figsize=(10, 6))
    plt.hist(general_df["poss"], bins=20, edgecolor="black")
    plt.title("Poss Distribution of NBA Members")
    plt.xlabel("Poss")
    plt.ylabel("Frequency")
    if not jupyter_render:
        plt.savefig("NBA_poss.png")
    else:
        plt.show()



def NBA_bar_mp(general_df, jupyter_render):
    """generate a bar graph of state distrubution of congress members"""
    gender_counts = general_df["mp"].value_counts()
    plt.figure(figsize=(15, 6))
    gender_counts.plot(kind="bar", color="salmon")
    plt.title("MP Distribution of Congress Members")
    plt.xlabel("mp")
    plt.ylabel("Count")
    plt.xticks(rotation=0)
    if not jupyter_render:
        plt.savefig("NBA_mp.png")
    else:
        plt.show()