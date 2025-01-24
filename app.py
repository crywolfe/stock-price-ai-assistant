from pydantic_a import Agent
from pydantic import BaseModel
import yfinance
from datetime import datetime

class StockPriceResult(BaseModel):
    """Model representing stock price data"""
    symbol: str
    current_price: float
    open_price: float
    high_price: float
    low_price: float
    volume: int
    last_updated: datetime
    
    class Config:
        json_encoders = {
            datetime: lambda dt: dt.isoformat()
        }
