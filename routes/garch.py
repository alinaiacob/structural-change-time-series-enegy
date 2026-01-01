from fastapi import APIRouter
from services.garch import computeGarch

router = APIRouter()

@router.get("/volatility")
def garchVolatility(ticker):
    df = computeGarch(ticker)
    return{
        "date":df.index.tolist(),
        "garch_vol":df["garch_vol"].tolist()
    }