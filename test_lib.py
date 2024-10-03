"""
Test goes here

"""

import pytest
from mylib.lib import *



def test_load_and_preprocess():
    # TODO: Add tests for load_and_preprocess
    csv = "https://projects.fivethirtyeight.com/nba-model/2023/latest_RAPTOR_by_player.csv"
    load_and_preprocess(csv)
    df = load_and_preprocess(csv)
    assert isinstance(df, pd.DataFrame), "Expected a DataFrame to be returned"
    assert not df.empty, "Expected DataFrame not to be empty"

def test_process_mean():
    # TODO: Add tests for process_mean
    csv = "https://projects.fivethirtyeight.com/nba-model/2023/latest_RAPTOR_by_player.csv"
    general_df = pd.read_csv(csv)
    result = process_mean(general_df, "mp")
    # print(result)
    assert result == 1174.4158964879853


def test_process_median():
    # TODO: Add tests for process_median
    csv = "https://projects.fivethirtyeight.com/nba-model/2023/latest_RAPTOR_by_player.csv"
    general_df = pd.read_csv(csv)
    result = process_median(general_df, "mp")
    # print(result)
    assert result == 996.0

def test_process_std():
    # TODO: Add tests for process_std
    csv = "https://projects.fivethirtyeight.com/nba-model/2023/latest_RAPTOR_by_player.csv"
    general_df = pd.read_csv(csv)
    result = process_std(general_df, "mp")
    # print(result)
    assert result == 913.0096399467657





test_load_and_preprocess()
test_process_mean()
test_process_median()
test_process_std()