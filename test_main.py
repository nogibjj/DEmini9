"""
Test goes here

"""

import matplotlib.pyplot as plt
from mylib.test_lib import *



#  Generate Markdown File
def generate_markdown():
    markdown_content = """
# Sample Plot Report

This is a sample report generated in Markdown format.

## Plot

Below is a plot generated from the data:

![Sample Plot](./plot.png)

## Conclusion

This is an auto-generated report from the Python script.
    """

    # Step 3: Write Markdown content to a file
    with open('report.md', 'w') as f:
        f.write(markdown_content)

if __name__ == "__main__":
    # create_plot()
    example_csv = "https://projects.fivethirtyeight.com/nba-model/2023/latest_RAPTOR_by_player.csv"

    test_load_and_preprocess()
    test_stats()
    generate_markdown()
