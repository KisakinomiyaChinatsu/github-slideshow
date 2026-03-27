from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..models import MaterialRecord, Material
from ..schemas import MaterialRecordCreate, MaterialRecordResponse

router = APIRouter(prefix="/api/material-records", tags=["material-records"])


@router.get("", response_model=List[MaterialRecordResponse])
def get_material_records(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    records = db.query(MaterialRecord).offset(skip).limit(limit).all()
    return records


@router.post("", response_model=MaterialRecordResponse)
def create_material_record(record: MaterialRecordCreate, db: Session = Depends(get_db)):
    db_material = db.query(Material).filter(Material.id == record.material_id).first()
    if not db_material:
        raise HTTPException(status_code=404, detail="物品不存在")
    
    if record.operation_type == "in":
        db_material.current_stock += record.quantity
    elif record.operation_type == "out":
        if db_material.current_stock < record.quantity:
            raise HTTPException(status_code=400, detail="库存不足")
        db_material.current_stock -= record.quantity
    else:
        raise HTTPException(status_code=400, detail="操作类型无效")
    
    db_record = MaterialRecord(**record.model_dump())
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record
