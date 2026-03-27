from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class MemberBase(BaseModel):
    code: str
    name: str
    phone: Optional[str] = None
    level: str = "普通会员"
    points: int = 0
    remark: Optional[str] = None


class MemberCreate(MemberBase):
    pass


class MemberUpdate(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None
    level: Optional[str] = None
    points: Optional[int] = None
    remark: Optional[str] = None


class MemberResponse(MemberBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class ConsumptionBase(BaseModel):
    member_id: int
    amount: float = 0
    product_name: str
    quantity: int = 1
    remark: Optional[str] = None


class ConsumptionCreate(ConsumptionBase):
    pass


class ConsumptionResponse(ConsumptionBase):
    id: int
    consume_time: datetime
    member: Optional[MemberResponse] = None

    class Config:
        from_attributes = True


class CategoryBase(BaseModel):
    code: str
    name: str
    description: Optional[str] = None


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None


class CategoryResponse(CategoryBase):
    id: int

    class Config:
        from_attributes = True


class ProductBase(BaseModel):
    code: str
    name: str
    category_id: int
    price: float = 0
    stock: int = 0
    description: Optional[str] = None


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    name: Optional[str] = None
    category_id: Optional[int] = None
    price: Optional[float] = None
    stock: Optional[int] = None
    description: Optional[str] = None


class ProductResponse(ProductBase):
    id: int
    created_at: datetime
    category: Optional[CategoryResponse] = None

    class Config:
        from_attributes = True


class MaterialBase(BaseModel):
    code: str
    name: str
    spec: Optional[str] = None
    unit: Optional[str] = None
    current_stock: int = 0
    remark: Optional[str] = None


class MaterialCreate(MaterialBase):
    pass


class MaterialUpdate(BaseModel):
    name: Optional[str] = None
    spec: Optional[str] = None
    unit: Optional[str] = None
    current_stock: Optional[int] = None
    remark: Optional[str] = None


class MaterialResponse(MaterialBase):
    id: int

    class Config:
        from_attributes = True


class MaterialRecordBase(BaseModel):
    material_id: int
    operation_type: str
    quantity: int
    operator: str
    remark: Optional[str] = None


class MaterialRecordCreate(MaterialRecordBase):
    pass


class MaterialRecordResponse(MaterialRecordBase):
    id: int
    record_time: datetime
    material: Optional[MaterialResponse] = None

    class Config:
        from_attributes = True
