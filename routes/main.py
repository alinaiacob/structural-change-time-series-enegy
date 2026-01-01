from fastapi import APIRouter
from routes.garch import router as garch_router
from routes.volatility import router as volatility_router
from routes.volume import router as volume_router
from routes.markets import router as markets_router

router = APIRouter(
    prefix="/market",
    tags=["Market"]
)

router.include_router(markets_router)
router.include_router(volume_router)
router.include_router(volatility_router)
router.include_router(garch_router)
