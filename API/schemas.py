from typing import Any, Optional, Dict
from pydantic import BaseModel
from pydantic.utils import GetterDict
import peewee

class PeeweeGetterDict(GetterDict):
    def get(self, key: Any, default: Any = None):
        res = getattr(self._obj, key, default)
        if isinstance(res, peewee.ModelSelect):
            return list(res)
        return res

class ArticleBase(BaseModel):
    article_id: int
    name: str
    price: int
    quantity: int

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict

class BillBase(BaseModel):
    bill_id: int
    client_name: str
    rnc: str
    description: str
    article_id: int
    quantity: int

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict

class getAllBills(BillBase):
    sub_total: int
    itbis: int
    total: int

class deleteBill(BaseModel):
    bill_id: int = Any

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict