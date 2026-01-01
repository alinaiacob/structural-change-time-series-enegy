from fastapi import APIRouter
from services.features import addFeatures

router = APIRouter()

@router.get("/zscore")
def volume_zscore(ticker, years):
    df =  addFeatures(ticker)

    return{
        "date":df.index.tolist(),
        "zscore":df["vol_zscore_20"].tolist()
    }