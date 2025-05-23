import pytest
import pandas as pd
import numpy as np
import os
from app import utils

def test_get_countries():
    countries = utils.get_countries()
    assert isinstance(countries, list)
    assert set(["Benin", "Sierra Leone", "Togo"]).issubset(set(countries))

def test_load_country_data():
    for country in utils.get_countries():
        df = utils.load_country_data(country, data_dir="data")
        assert isinstance(df, pd.DataFrame)
        assert not df.empty
        assert utils.get_ghi_column(df) in df.columns

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
