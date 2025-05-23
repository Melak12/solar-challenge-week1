import pytest
import pandas as pd
import numpy as np
import os
from app import utils

MOCK_DATA_DIR = os.path.join(os.path.dirname(__file__), 'mock_data')

def test_get_countries():
    countries = utils.get_countries()
    assert isinstance(countries, list)
    assert set(["Benin", "Sierra Leone", "Togo"]).issubset(set(countries))

def test_load_country_data():
    for country in utils.get_countries():
        df = utils.load_country_data(country, data_dir=MOCK_DATA_DIR)
        assert isinstance(df, pd.DataFrame)
        assert not df.empty
        # Accept either 'ghi' or 'GHI' as the column name in mock data
        ghi_col = utils.get_ghi_column(df)
        assert ghi_col.lower() == 'ghi'

def test_get_ghi_column():
    df = pd.DataFrame({
        "ghi_value": [1, 2, 3],
        "other": [4, 5, 6]
    })
    col = utils.get_ghi_column(df)
    assert col == "ghi_value"
    with pytest.raises(ValueError):
        utils.get_ghi_column(pd.DataFrame({"foo": [1, 2]}))

def test_get_top_regions():
    df = pd.DataFrame({
        "region": ["A", "A", "B", "B", "C"],
        "ghi": [10, 20, 30, 40, 50]
    })
    top = utils.get_top_regions(df, "region", "ghi", n=2)
    assert len(top) == 2
    assert set(top["region"]).issubset({"B", "C"})
