from pydantic import BaseModel, Field
from typing import Optional
import uuid


class BaseDomainModel(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)


class ProductCategory(BaseDomainModel):
    name: str
    description: Optional[str] = None
    parent_category_id: Optional[uuid.UUID] = None
    company_id: uuid.UUID


class Warehouse(BaseDomainModel):
    name: str
    code: str
    location: Optional[str] = None
    is_active: bool = True
    company_id: uuid.UUID


class Product(BaseDomainModel):
    sku: str
    name: str
    description: Optional[str] = None
    category_id: uuid.UUID
    base_unit: str  # e.g., "unit", "kg", "liter"
    is_active: bool = True
    company_id: uuid.UUID

    class Config:
        orm_mode = True
