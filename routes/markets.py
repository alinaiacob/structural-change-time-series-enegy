from fastapi import APIRouter, HTTPException
from services.data_loader import loadData

router = APIRouter()

@router.get("/overview")
def marketOverview(ticker):
    try:
        df = loadData(ticker)

        if df.empty:
            raise ValueError("Empty dataframe")

        return {
            "symbol": ticker,
            "date": df.index.astype(str).tolist(),
            "close": df["Close"].astype(float).tolist(),
            "volume": df["Volume"].astype(float).tolist()
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

# res = marketOverview("NXT")
# print("res",res)    