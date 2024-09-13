"""
Main cli or app entry point
"""

from mylib.calculator import *

import click

#var=1;var=2

@click.command("add")
@click.argument("a", type=int)
@click.argument("b", type=int)
def add_cli(a, b):
    click.echo(add(a, b))



def save_to_md():
    with open("test.md", "a") as file:
        file.write("TEST HERE")


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    # add_cli()
    dataset = "https://projects.fivethirtyeight.com/nba-model/2023/latest_RAPTOR_by_player.csv"
    df = load_dataset(dataset)
    # print(df)
    print(grab_mean(df, 'pace_impact'))
    create_histogram(df, 'mp')
