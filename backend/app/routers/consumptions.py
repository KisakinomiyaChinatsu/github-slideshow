from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..models import Consumption
from ..schemas import ConsumptionCreate, ConsumptionResponse

router = APIRouter(prefix="/api/consumptions", tags=["consumptions"])


@router.get("", response_model=List[ConsumptionResponse])
def get_consumptions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    consumptions = db.query(Consumption).offset(skip).limit(limit).all()
    return consumptions


@router.post("", response_model=ConsumptionResponse)
def create_consumption(consumption: ConsumptionCreate, db: Session = Depends(get_db)):
    db_consumption = Consumption(**consumption.model_dump())
    db.add(db_consumption)
    db.commit()
    db.refresh(db_consumption)
    return db_consumption


@router.get("/{consumption_id}", response_model=ConsumptionResponse)
def get_consumption(consumption_id: int, db: Session = Depends(get_db)):
    db_consumption = db.query(Consumption).filter(Consumption.id == consumption_id).first()
    if not db_consumption:
        raise HTTPException(status_code=404, detail="消费记录不存在")
    return db_consumption
