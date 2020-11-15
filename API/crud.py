import models, schemas, datetime

def get_articles(skip: int = 0, limit: int = 100):
    return list(models.Article.select().offset(skip).limit(limit))

def register_article(article: schemas.ArticleBase):
    new_article = models.Article.create(
        article_id = article.article_id,
        name = article.name,
        price = article.price,
        quantity = article.quantity
    )
    return new_article

def get_bills(skip: int = 0, limit: int = 100):
    return list(models.Bill.select().offset(skip).limit(limit))

def register_bill(bill: schemas.BillBase):
    new_bill = models.Bill.create(
        bill_id = bill.bill_id,
        client_name = bill.client_name,
        rnc = bill.rnc,
        description = bill.description,
        date = datetime.datetime.now(),
        article = bill.article_id,
        quantity = bill.quantity,
        sub_total = models.Article.select(models.Article.price).where(
            models.Article.article_id == bill.article_id
        ),
        itbis = models.Article.select(models.Article.price * 18 / 100).where(
            models.Article.article_id == bill.article_id
        ),
        total = models.Article.select(models.Article.price + 18 / 100 + bill.quantity).where(
            models.Article.article_id == bill.article_id
        )
    )

    new_quantity = models.Article.update(
        quantity = models.Article.quantity - bill.quantity
    ).where(models.Article.article_id == bill.article_id)

    new_quantity.execute()

    return new_bill

def updated_bill(bill: schemas.BillBase):
    updated_bill = models.Bill.update(
        client_name = bill.client_name,
        rnc = bill.rnc,
        description = bill.description,
        date = datetime.datetime.now(),
        article = bill.article_id,
        quantity = bill.quantity,
        sub_total = models.Article.select(models.Article.price).where(
            models.Article.article_id == bill.article_id
        ),
        itbis = models.Article.select(models.Article.price * 18 / 100).where(
            models.Article.article_id == bill.article_id
        ),
        total = models.Article.select(models.Article.price + 18 / 100 + bill.quantity).where(
            models.Article.article_id == bill.article_id
        )
    ).where(models.Bill.bill_id == bill.bill_id)

    updated_bill.execute()
    return updated_bill


