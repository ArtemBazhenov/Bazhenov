import sqlite3
    
class DB:
    def __init__(self):
        self.connection =  sqlite3.connect('webshop.db')
    
    def newCursor(self):
        self.cursor = self.connection.cursor()
    
    def closeCursor(self):
        self.cursor.close()
        
    def dbClose(self):
        self.connection.close()
        
    def get1(self):
        z1 = ('''
            SELECT
            id_order as "номер покупки",
            (SELECT name FROM product WHERE zakaz.id_product=product.id_product) as "название товара",
            "kol-vo" as " сколько куплено"
            FROM zakaz;
        ''')
        self.cursor.execute(z1)
        return self.cursor.fetchall()
    
    def get2(self):
        z2 = ('''
        SELECT
        (SELECT login from buyer where buyer.id_buyer=pokupka.id_buyer) as "кто закал",
        status as "доставлено ли"
        FROM pokupka;
        ''')
        self.cursor.execute(z2)
        return self.cursor.fetchall()
    
    def get3(self):
        z3 = ('''
        SELECT
        name as "название товара",
        (SELECT name from category where category.id_category=product.id_category) as "название категории товара"
        FROM product;
        ''')
        self.cursor.execute(z3)
        return self.cursor.fetchall()
    
