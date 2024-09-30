import pytest
import os
from unittest.mock import patch
import pandas as pd
from main import *



def test_general_describe():
    # TODO: Add tests for general_describe
    csv = "https://projects.fivethirtyeight.com/nba-model/2023/latest_RAPTOR_by_player.csv"
    df = general_describe(csv)
    assert isinstance(df, pd.DataFrame), "Expected a DataFrame to be returned"
    assert not df.empty, "Expected DataFrame not to be empty"
    # pass


def test_custom_describe():
    # TODO: Add tests for custom_describe
    csv = "https://projects.fivethirtyeight.com/nba-model/2023/latest_RAPTOR_by_player.csv"    
    # df = custom_describe(csv, "mp")
 
    result = custom_describe(csv, "mp")
    print(result)
    assert result["mean"] == 1174.4158964879853
    assert result["std"] == 913.0096399467657
    assert result["median"] == 996.0
    assert result["25 quantile"] == 323.0



# test_general_describe()
# test_custom_describe()
          