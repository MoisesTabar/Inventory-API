from fastapi import FastAPI, Depends, HTTPException
from database import db_state_default
from typing import List
import schemas, crud, models, database

database.db.connect()
database.db.create_tables([models.Article, models.Bill])
database.db.close()

app = FastAPI()

sleep_time = 10

async def reset_db_state():
    database.db._state._state.set(db_state_default.copy())
    database.db._state.reset()

def get_db(db_state=Depends(reset_db_state)):
    try:
        database.db.connect()
        yield
    finally:
        if not database.db.is_closed():
            database.db.close()

@app.get('/articles/get', response_model = List[schemas.ArticleBase], dependencies = [Depends(get_db)])
def get_articles(skip: int = 0, limit: int = 100):
    articles = crud.get_articles(skip = skip, limit = limit)
    return articles

@app.post('/articles/save', response_model = schemas.ArticleBase, dependencies = [Depends(get_db)])
def register_article(article: schemas.ArticleBase):
    new_article = crud.register_article(article)
    return new_article

@app.get('/bills/get', response_model = List[schemas.getAllBills], dependencies = [Depends(get_db)])
def get_bills(skip: int = 0, limit: int = 100):
    bills = crud.get_bills(skip = skip, limit = limit)
    return bills

@app.post('/bills/save', response_model = schemas.BillBase, dependencies = [Depends(get_db)])
def register_bill(bill: schemas.BillBase):
    new_bill = crud.register_bill(bill) 
    return new_bill

@app.post('/bills/update', response_model = schemas.BillBase, dependencies = [Depends(get_db)])
def update_bill(bill: schemas.BillBase):
    updated_bill = crud.updated_bill(bill)
    return updated_bill