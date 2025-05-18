# Utility functions for data processing and visualization
import pandas as pd
import numpy as np
import os

def load_country_data(country: str, data_dir: str = "data") -> pd.DataFrame:
    """
    Load cleaned data for a given country from the data directory.
    """
    file_map = {
        "Benin": "benin_clean.csv",
        "Sierra Leone": "sierraleone_clean.csv",
        "Togo": "togo_clean.csv"
    }
    file_name = file_map.get(country)
    if not file_name:
        raise ValueError(f"No data file mapped for country: {country}")
    file_path = os.path.join(data_dir, file_name)
    return pd.read_csv(file_path)

def get_countries() -> list:
    """
    Return the list of available countries.
    """
    return ["Benin", "Sierra Leone", "Togo"]

def get_ghi_column(df: pd.DataFrame) -> str:
    """
    Return the name of the GHI column if present.
    """
    for col in df.columns:
        if "ghi" in col.lower():
            return col
    raise ValueError("No GHI column found in dataframe.")

def get_top_regions(df: pd.DataFrame, region_col: str, ghi_col: str, n: int = 5) -> pd.DataFrame:
    """
    Return the top n regions by average GHI.
    """
    return df.groupby(region_col)[ghi_col].mean().sort_values(ascending=False).head(n).reset_index()
