import pytest
from main import *



def test_general_describe():
    # TODO: Add tests for general_describe
    csv = "https://projects.fivethirtyeight.com/nba-model/2023/latest_RAPTOR_by_player.csv"
    general_describe(csv)
    pass


def test_custom_describe():
    # TODO: Add tests for custom_describe
    csv = "https://projects.fivethirtyeight.com/nba-model/2023/latest_RAPTOR_by_player.csv"    
    custom_describe(csv, "mp")
    pass


def test_general_viz_combined():
    # TODO: Add tests for general_viz_combined
    csv = "https://projects.fivethirtyeight.com/nba-model/2023/latest_RAPTOR_by_player.csv"   
    general_viz_combined(general_df, True)
    pass

    
    

def test_save_to_markdown():
    # TODO: Add tests for save_to_markdown
    csv = "https://projects.fivethirtyeight.com/nba-model/2023/latest_RAPTOR_by_player.csv"   
    save_to_markdown(csv)
    pass
