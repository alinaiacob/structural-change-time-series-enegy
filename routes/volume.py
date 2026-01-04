from fastapi import APIRouter
from services.features import addFeatures

router = APIRouter()

@router.get("/zscore")
def volume_zscore(ticker):
    df =  addFeatures(ticker)

    return{
        "symbol":"ticker",
        "date":df.index.astype(str).tolist(),
        "zscore":df["vol_zscore_20"].astype(float).tolist()
    }

# res = volume_zscore("NXT")
# print(res)