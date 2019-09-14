import sqlite3
from alchemy_db import db

class ItemModel(db.Model):
    __tablename__ = 'ITEMS'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(60))
    price = db.Column(db.Float(precision=2))
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def json(self):
        return {'name':self.name, 'price':self.price}

    @classmethod
    def find_by_name(cls, name):
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        query = 'SELECT * FROM ITEMS WHERE name = ?'
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        conn.close()
        if row:
            return cls(*row)

    def insert(self):
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        insert_query = 'INSERT INTO ITEMS VALUES(?, ?)'
        cursor.execute(insert_query, (self.name, self.price))
        conn.commit()
        conn.close()

    def update(self):
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        update_query = 'UPDATE ITEMS SET price=? WHERE name=?'
        cursor.execute(update_query, (self.price, self.name))
        conn.commit()
        conn.close()