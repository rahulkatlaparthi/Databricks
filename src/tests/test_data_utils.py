import pandas as pd
from src.utils.data_utils import clean_data

def test_clean_data():
    df = pd.DataFrame({"A": [1, None, 3]})
    result = clean_data(df)
    assert len(result) == 2
    assert result["A"].isnull().sum() == 0
