from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testdb.db'
db = SQLAlchemy(app)

class Buyer(db.Model):
    id_buyer = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(80),nullable=True)
    password = db.Column(db.String(80),nullable=True)
    address=db.Column(db.String(80),nullable=True)
    mail=db.Column(db.String(80), unique=True, nullable=True)
    
    def __repr__(self):
        return f'{self.id_buyer}'    
    
class Category(db.Model):
    id_category=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80),nullable=True)
    
    def __repr__(self):
        return f'{self.id_category}'    
    
class Pokupka(db.Model):
        id_order = db.Column(db.Integer, primary_key=True)
        id_buyer = db.Column(db.Integer, db.ForeignKey('buyer.id_buyer'),nullable=True)
        date = db.Column(db.String(80),nullable=True)
        total_cost = db.Column(db.Integer,nullable=True)
        status = db.Column(db.String(80),nullable=True)
        buyer = db.relationship('Buyer',backref=db.backref('Pokupka', lazy=False))        
        
        def __repr__(self):
            return f'{self.id_order} {self.id_buyer}'

class Product(db.Model):
        id_product=db.Column(db.Integer,primary_key=True)
        id_category=db.Column(db.Integer,db.ForeignKey('category.id_category'))
        name=db.Column(db.String(80),nullable=True)
        price= db.Column(db.Integer,nullable=True)
        category = db.relationship('Category',backref=db.backref('Product', lazy=False))      
        
        def __repr__(self):
            return f'{self.id_product}'
        
class Zakaz(db.Model):
    id_str=db.Column(db.Integer,primary_key=True)
    id_order= db.Column(db.Integer,db.ForeignKey('pokupka.id_order'),nullable=True)
    id_product= db.Column(db.Integer,db.ForeignKey('product.id_product'),nullable=True)
    kol= db.Column(db.Integer,nullable=True)
    order = db.relationship('Pokupka',backref=db.backref('zakaz', lazy=False))   
    product = db.relationship('Product',backref=db.backref('zakaz', lazy=False))  
    
    def __repr__(self):
        return f'{self.id_str}'    
    
db.create_all()


buyer=Buyer(login='Oleg',password='12345',address='karavan',mail='oleg_mail')
db.session.add(buyer)
buyer2=Buyer(login='Artem',password='12344',address='almati',mail='artem_mail')
db.session.add(buyer2)
buyer3=Buyer(login='Alina',password='12343',address='sirius',mail='alina_mail')
db.session.add(buyer3)


category=Category(name='mystic')
db.session.add(category)
category2=Category(name='clother')
db.session.add(category2)


order=Pokupka(buyer=buyer, date='2021.08.20',total_cost=3000,status='+')
db.session.add(order)
order2=Pokupka(buyer=buyer3, date='2021.08.20',total_cost=3000,status='+')
db.session.add(order2)
order3=Pokupka(buyer=buyer2, date='2021.08.24',total_cost=3000,status='+')
db.session.add(order3)


product=Product(category = category,name='surprisebox',price=2000)
db.session.add(product)
product2=Product(category = category2,name='towel-pants',price=1000)
db.session.add(product2)


z=Zakaz(order=order,product=product2,kol=3)
db.session.add(z)
z2=Zakaz(order=order2,product=product2,kol=3)
db.session.add(z2)
z3=Zakaz(order=order3,product=product,kol=1)
db.session.add(z3)
z4=Zakaz(order=order3,product=product2,kol=1)
db.session.add(z4)


db.session.commit()