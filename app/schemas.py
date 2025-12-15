from pydantic import BaseModel
from datetime import date
from typing import List, Optional


class Transaction(BaseModel):
    category: str
    amount: float
    date: date
    description: Optional[str] = ""


class FarmData(BaseModel):
    farmer_name: str
    crop_name: str
    season: str
    total_acres: float
    sowing_date: date
    harvest_date: date
    location: str
    expenses: List[Transaction]
    incomes: List[Transaction]
