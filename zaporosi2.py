import sqlite3

conn=sqlite3.connect('webshop.db')
cursor = conn.cursor()

cursor.execute('''
SELECT
id_order as "номер покупки",
(SELECT name FROM product WHERE zakaz.id_product=product.id_product) as "название товара",
"kol-vo" as " сколько куплено"
FROM zakaz;
''')

cursor.execute('''
SELECT
(SELECT login from buyer where buyer.id_buyer=pokupka.id_buyer) as "кто закал",
status as "доставлено ли"
FROM pokupka;
''')

cursor.execute('''
SELECT
name as "название товара",
(SELECT name from category where category.id_category=product.id_category) as "название категории товара"
FROM product;
''')

conn.commit()

conn.close()