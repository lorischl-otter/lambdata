"""
Utility functions for working with DataFrames
"""

import pandas as pd
import numpy as np

TEST_DF = pd.DataFrame([1, 2, 3], [4, np.NaN, 2])


# create utility functions for assignment

def nulls(df):
    """Take a DataFrame and outputs a new df of NaN sums by column."""
    return pd.DataFrame(df.isna().sum())


def display_settings(rows, columns):
    """Change the df display settings in a notebook."""
    pd.set_option('display.max_rows', rows)
    pd.set_option('display.max_columns', columns)
    print('Display options change complete.')
