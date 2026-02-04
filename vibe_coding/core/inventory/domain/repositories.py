from abc import ABC, abstractmethod
from typing import List, Optional, Generic, TypeVar
import uuid

from .models import Product, ProductCategory, Warehouse

T = TypeVar('T')


class IGenericRepository(ABC, Generic[T]):
    @abstractmethod
    def get_by_id(self, id: uuid.UUID) -> Optional[T]:
        ...

    @abstractmethod
    def list_all(self) -> List[T]:
        ...

    @abstractmethod
    def add(self, entity: T) -> T:
        ...

    @abstractmethod
    def update(self, entity: T) -> T:
        ...

    @abstractmethod
    def delete(self, id: uuid.UUID) -> None:
        ...


class IProductRepository(IGenericRepository[Product]):
    @abstractmethod
    def find_by_sku(self, sku: str) -> Optional[Product]:
        ...


class IProductCategoryRepository(IGenericRepository[ProductCategory]):
    @abstractmethod
    def find_by_name(self, name: str) -> List[ProductCategory]:
        ...


class IWarehouseRepository(IGenericRepository[Warehouse]):
    @abstractmethod
    def find_by_code(self, code: str) -> Optional[Warehouse]:
        ...
