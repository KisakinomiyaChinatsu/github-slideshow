from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..models import Member
from ..schemas import MemberCreate, MemberUpdate, MemberResponse

router = APIRouter(prefix="/api/members", tags=["members"])


@router.get("", response_model=List[MemberResponse])
def get_members(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    members = db.query(Member).offset(skip).limit(limit).all()
    return members


@router.post("", response_model=MemberResponse)
def create_member(member: MemberCreate, db: Session = Depends(get_db)):
    db_member = db.query(Member).filter(Member.code == member.code).first()
    if db_member:
        raise HTTPException(status_code=400, detail="会员编号已存在")
    db_member = Member(**member.model_dump())
    db.add(db_member)
    db.commit()
    db.refresh(db_member)
    return db_member


@router.put("/{member_id}", response_model=MemberResponse)
def update_member(member_id: int, member: MemberUpdate, db: Session = Depends(get_db)):
    db_member = db.query(Member).filter(Member.id == member_id).first()
    if not db_member:
        raise HTTPException(status_code=404, detail="会员不存在")
    for key, value in member.model_dump(exclude_unset=True).items():
        setattr(db_member, key, value)
    db.commit()
    db.refresh(db_member)
    return db_member


@router.delete("/{member_id}")
def delete_member(member_id: int, db: Session = Depends(get_db)):
    db_member = db.query(Member).filter(Member.id == member_id).first()
    if not db_member:
        raise HTTPException(status_code=404, detail="会员不存在")
    db.delete(db_member)
    db.commit()
    return {"message": "删除成功"}
