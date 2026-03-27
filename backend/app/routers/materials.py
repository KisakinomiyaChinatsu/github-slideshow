from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..models import Material
from ..schemas import MaterialCreate, MaterialUpdate, MaterialResponse

router = APIRouter(prefix="/api/materials", tags=["materials"])


@router.get("", response_model=List[MaterialResponse])
def get_materials(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    materials = db.query(Material).offset(skip).limit(limit).all()
    return materials


@router.post("", response_model=MaterialResponse)
def create_material(material: MaterialCreate, db: Session = Depends(get_db)):
    db_material = db.query(Material).filter(Material.code == material.code).first()
    if db_material:
        raise HTTPException(status_code=400, detail="物品编号已存在")
    db_material = Material(**material.model_dump())
    db.add(db_material)
    db.commit()
    db.refresh(db_material)
    return db_material


@router.put("/{material_id}", response_model=MaterialResponse)
def update_material(material_id: int, material: MaterialUpdate, db: Session = Depends(get_db)):
    db_material = db.query(Material).filter(Material.id == material_id).first()
    if not db_material:
        raise HTTPException(status_code=404, detail="物品不存在")
    for key, value in material.model_dump(exclude_unset=True).items():
        setattr(db_material, key, value)
    db.commit()
    db.refresh(db_material)
    return db_material


@router.delete("/{material_id}")
def delete_material(material_id: int, db: Session = Depends(get_db)):
    db_material = db.query(Material).filter(Material.id == material_id).first()
    if not db_material:
        raise HTTPException(status_code=404, detail="物品不存在")
    db.delete(db_material)
    db.commit()
    return {"message": "删除成功"}
