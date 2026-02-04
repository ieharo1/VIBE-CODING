import uuid
from sqlalchemy import Column, String, Boolean, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from vibe_coding.infrastructure.persistence.database import Base


class BaseModel(Base):
    __abstract__ = True
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    # company_id will be added to each concrete model that needs it


class ProductCategory(Base):
    __tablename__ = "product_categories"

    name = Column(String, nullable=False, index=True)
    description = Column(String)
    
    parent_category_id = Column(UUID(as_uuid=True), ForeignKey("product_categories.id"))
    parent = relationship("ProductCategory", remote_side=[BaseModel.id], back_populates="children")
    children = relationship("ProductCategory", back_populates="parent")

    company_id = Column(UUID(as_uuid=True), nullable=False, index=True) # Assuming a companies table exists
    products = relationship("Product", back_populates="category")


class Warehouse(Base):
    __tablename__ = "warehouses"

    name = Column(String, nullable=False)
    code = Column(String, nullable=False, unique=True, index=True)
    location = Column(String)
    is_active = Column(Boolean, default=True)
    
    company_id = Column(UUID(as_uuid=True), nullable=False, index=True)


class Product(Base):
    __tablename__ = "products"

    sku = Column(String, nullable=False, unique=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    base_unit = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)

    category_id = Column(UUID(as_uuid=True), ForeignKey("product_categories.id"), nullable=False)
    category = relationship("ProductCategory", back_populates="products")

    company_id = Column(UUID(as_uuid=True), nullable=False, index=True)
