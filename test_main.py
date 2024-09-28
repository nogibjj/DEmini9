import pytest
import os
from unittest.mock import patch
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
    general_df = load_and_preprocess(csv)
    # general_viz_combined(general_df, True)
    with patch('matplotlib.pyplot.show') as mock_show:
    # Call the visualization function
        general_viz_combined(general_df, True)

        # Assert that the plot function was called
        mock_show.assert_called_once()  # Ensure that plt.show() is called exactly once

        # Additional assertions can be added based on what the function does
        # For example, if the function saves a plot, check if the file was created
        output_plot_path = 'output_plot.png'  # Replace with the actual path used in your function, if applicable

    # Assert if the plot was saved as expected
    if os.path.exists(output_plot_path):
        assert os.path.exists(output_plot_path), "Expected plot file was not created."
        os.remove(output_plot_path) 
    pass

    
    

def test_save_to_markdown():
   # Test URL of the CSV file
    csv_url = "https://projects.fivethirtyeight.com/nba-model/2023/latest_RAPTOR_by_player.csv"
    
    # Define the output Markdown file path
    output_file = 'latest_RAPTOR_by_player.md'

    # Call the function
    save_to_markdown(csv_url, output_file)  # Ensure the function saves to this file

    # Assert: Check if the file was created
    assert os.path.exists(output_file), "Markdown file was not created."

    # Assert: Check the content of the file
    with open(output_file, 'r') as file:
        content = file.read()
        # Check if the content includes expected text (e.g., markdown headers)
        assert "# Latest RAPTOR by Player" in content, "Markdown file content is not as expected."
        assert "LeBron James" in content, "Expected player data is missing in the markdown file."

    # Cleanup: Optionally delete the generated markdown file after test
    os.remove(output_file)



    # test_general_viz_combined()
    # test_save_to_markdown()