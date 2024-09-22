"""
Test goes here

"""

from mylib.lib import (
    load_and_preprocess,
    process_mean,
    process_quantile,
    process_median,
    process_std,
)

example_csv = "https://projects.fivethirtyeight.com/nba-model/2023/latest_RAPTOR_by_player.csv"

def test_load_and_preprocess():
    """test that loading the csv will work"""
    general_df = load_and_preprocess(example_csv)
    assert general_df is not None
    assert general_df.shape == (541, 21)


def test_stats():
    """test that checks the data operations is working"""
    general_df = load_and_preprocess(example_csv)
    mean_test = process_mean(general_df, "mp")
    quantile_test = process_quantile(general_df, "mp", 0.25)
    median_test = process_median(general_df, "mp")
    std_test = process_std(general_df, "mp")
    describe_test = general_df.describe()
    print(median_test)
    assert describe_test.loc["mean", "mp"] == mean_test
    assert describe_test.loc["std", "mp"] == std_test
    assert describe_test.loc["25%", "mp"] == quantile_test
    assert median_test == 996.0

if __name__ == "__main__":
    test_load_and_preprocess()
    test_stats()