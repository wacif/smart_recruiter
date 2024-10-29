# utils/table_utils.py

import pandas as pd

def generate_results_table(candidate_results):
    """Creates a DataFrame table for candidate results."""
    df = pd.DataFrame(candidate_results)
    return df
