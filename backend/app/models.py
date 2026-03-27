from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base


class Member(Base):
    __tablename__ = "members"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(50), unique=True, index=True)
    name = Column(String(100), index=True)
    phone = Column(String(20))
    level = Column(String(50), default="普通会员")
    points = Column(Integer, default=0)
    remark = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    consumptions = relationship("Consumption", back_populates="member")


class Consumption(Base):
    __tablename__ = "consumptions"

    id = Column(Integer, primary_key=True, index=True)
    member_id = Column(Integer, ForeignKey("members.id"))
    amount = Column(Float, default=0)
    product_name = Column(String(200))
    quantity = Column(Integer, default=1)
    consume_time = Column(DateTime(timezone=True), server_default=func.now())
    remark = Column(Text, nullable=True)

    member = relationship("Member", back_populates="consumptions")


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(50), unique=True, index=True)
    name = Column(String(100))
    description = Column(Text, nullable=True)

    products = relationship("Product", back_populates="category")


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(50), unique=True, index=True)
    name = Column(String(200), index=True)
    category_id = Column(Integer, ForeignKey("categories.id"))
    price = Column(Float, default=0)
    stock = Column(Integer, default=0)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    category = relationship("Category", back_populates="products")


class Material(Base):
    __tablename__ = "materials"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(50), unique=True, index=True)
    name = Column(String(200), index=True)
    spec = Column(String(100))
    unit = Column(String(20))
    current_stock = Column(Integer, default=0)
    remark = Column(Text, nullable=True)

    records = relationship("MaterialRecord", back_populates="material")


class MaterialRecord(Base):
    __tablename__ = "material_records"

    id = Column(Integer, primary_key=True, index=True)
    material_id = Column(Integer, ForeignKey("materials.id"))
    operation_type = Column(String(20))
    quantity = Column(Integer, default=0)
    operator = Column(String(100))
    record_time = Column(DateTime(timezone=True), server_default=func.now())
    remark = Column(Text, nullable=True)

    material = relationship("Material", back_populates="records")
