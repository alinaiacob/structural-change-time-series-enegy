from fastapi import APIRouter
from services.garch import computeGarch

router = APIRouter()

@router.get("/volatility")
def garchVolatility(ticker):
    df = computeGarch(ticker)
    return{
        "symbol":ticker,
        "metric":"garch_volatility",
        "data":[
            {
                "date":idx.strftime("%Y-%m-%d"),
                "value":float(v)
            }
            for idx, v in df["garch_vol"].dropna().items()
        ]
    }