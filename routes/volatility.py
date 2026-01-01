from fastapi import APIRouter
from services.cumsum import computeCumsum

router = APIRouter()

@router.get("/cusum")
def cusum_volatility(ticker):
    df = computeCumsum(ticker)
    return {
        "date":df.index.tolist(),
        "rolling_std":df["rolling_std"].tolist(),
        "cusum":df["cusum_vol"].tolist(),
        "events":df["cusum_event"].astype(int).tolist()
    }


