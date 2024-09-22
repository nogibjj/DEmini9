"""
Test goes here

"""

import pytest
from mylib.lib import *



def test_load_and_preprocess():
    # TODO: Add tests for load_and_preprocess
    csv = "https://projects.fivethirtyeight.com/nba-model/2023/latest_RAPTOR_by_player.csv"
    load_and_preprocess(csv)
    pass


def test_process_mean():
    # TODO: Add tests for process_mean
    csv = "https://projects.fivethirtyeight.com/nba-model/2023/latest_RAPTOR_by_player.csv"
    df = load_and_preprocess(csv)
    process_mean(df,'mp')
    pass


def test_process_median():
    # TODO: Add tests for process_median
    csv = "https://projects.fivethirtyeight.com/nba-model/2023/latest_RAPTOR_by_player.csv"
    df = load_and_preprocess(csv)
    process_mean(df,'mp')
    pass


def test_process_std():
    # TODO: Add tests for process_std
    csv = "https://projects.fivethirtyeight.com/nba-model/2023/latest_RAPTOR_by_player.csv"
    df = load_and_preprocess(csv)
    process_mean(df,'mp')
    pass


def test_process_quantile():
    # TODO: Add tests for process_quantile
    csv = "https://projects.fivethirtyeight.com/nba-model/2023/latest_RAPTOR_by_player.csv"
    df = load_and_preprocess(csv)
    process_mean(df,'mp',0.25)
    pass


def test_NBA_histogram_poss():
    # TODO: Add tests for NBA_histogram_poss
    csv = "https://projects.fivethirtyeight.com/nba-model/2023/latest_RAPTOR_by_player.csv"
    df = load_and_preprocess(csv)
    process_mean(df,'mp')
    NBA_histogram_poss(df, True)
    pass


def test_NBA_bar_mp():
    # TODO: Add tests for NBA_bar_mp
    csv = "https://projects.fivethirtyeight.com/nba-model/2023/latest_RAPTOR_by_player.csv"
    df = load_and_preprocess(csv)
    process_mean(df,'mp')
    NBA_bar_mp(df, True)
    pass
