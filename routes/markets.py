from fastapi import APIRouter
from services.data_loader import loadData

router = APIRouter()

@router.get("/overview")
def marketOverview(ticker):
    df = loadData(ticker)
    return{
        "date": df.index.tolist(),
        "close": df["Close"].tolist(),
        "volume":df["Volume"].tolist()
    }