import json

import pandas as pd
import numpy as np

def read_csv(filename) -> pd.DataFrame:
    try:
        df = pd.read_csv(filename)
        return df
    except FileNotFoundError as e:
        print(f"The file {filename} was not found or could not be opened: {e}")
        raise

def read_json(filename) -> dict:
    try:
        return json.load(open(filename))
    except FileNotFoundError as e:
        print(f"The file {filename} was not found or could not be opened: {e}")
        raise
    except json.decoder.JSONDecodeError as e:
        print(f"The file {filename} could not be decoded: {e}")
        raise