import pandas as pd
from utils import addDatesCol, cleanData
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATASETS_DIR = BASE_DIR / "datasets"

my_dict = {
    "NXT": DATASETS_DIR / "nxt_us_d.csv",
    "NEE": DATASETS_DIR / "nee_us_d.csv",
    "LEU": DATASETS_DIR / "leu_us_d.csv",
    "UUUU": DATASETS_DIR / "uuuu_us_d.csv",
    "ENPH": DATASETS_DIR / "enph_us_d.csv",
    "SPX": DATASETS_DIR / "^spx_d.csv",
}


def loadData(symbol):
    if symbol not in my_dict:
        raise ValueError(f"Unknown symbol: {symbol}")

    path = my_dict[symbol]

    if not path.exists():
        raise FileNotFoundError(f"Dataset not found: {path}")

    df = pd.read_csv(path)
    df = addDatesCol(df)
    df = cleanData(df)

    return df
