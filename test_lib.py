"""
Test goes here

"""

from mylib.lib import load_and_preprocess,process_mean,process_quantile,process_median,process_std
# Inside test_lib.py
# import mylib.lib
# print(f"lib.py imported from: {mylib.lib.__file__}")  # This will show the exact path being used


def test_load_and_preprocess():
    """test that loading the csv will work"""
    example_csv = "https://projects.fivethirtyeight.com/nba-model/2023/latest_RAPTOR_by_player.csv"   
    general_df = load_and_preprocess(example_csv)
    assert general_df is not None
    # assert general_df.shape == (541, 21)
    return general_df


def test_stats(general_df):
    """test that checks the data operations is working"""
    # general_df = load_and_preprocess(example_csv)
    # print(general_df)
    # print(general_df.shape)
    assert general_df is not None
    assert general_df.shape == (541, 21)
    #  print(f"The table we got is glimpsed like: {general_df.head()}")
    print(f"MP stands for Minutes Played, which represents the total number of minutes a player was on the court during the game or season. ")
    print(f"Poss stands for Possessions, which is an estimate of the number of possessions a player was directly involved in during a game or season.")
    mean_test = process_mean(general_df, "mp")
    quantile_test = process_quantile(general_df, "mp", 0.25)
    median_test = process_median(general_df, "mp")
    std_test = process_std(general_df, "mp")
    describe_test = general_df.describe()

    assert describe_test.loc["mean", "mp"] == mean_test
    assert describe_test.loc["std", "mp"] == std_test
    assert describe_test.loc["25%", "mp"] == quantile_test
    assert median_test == 996.0


if __name__ == "__main__":
    example_csv = "https://projects.fivethirtyeight.com/nba-model/2023/latest_RAPTOR_by_player.csv"

    general_df = test_load_and_preprocess()
    test_stats(general_df)