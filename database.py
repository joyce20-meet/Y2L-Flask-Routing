from model import *


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_product(ID,name,price,Picturelink,Description):
	product_objection = Product(
		ID=ID,
		name=name,
		price=price,
		Picturelink=Picturelink,
		Description=Description)
	session.add(product_objection)
	session.commit()

#add_product(12,"Family Charm",60,"/static/charm1.jpeg","Silver Charm ")
def update_price(ID,price):
 
	product_object = session.query(
		Product).filter_by(
			ID=ID).first()
	product_object.price = price
	session.commit()
#update_price(12,50)
def delete_product(their_name):

	session.query(Product).filter_by(
		ID=their_name).delete()
	session.commit()
#delete_product(11)
def query_all():

	products = session.query(
		Product).all()
	return products
query_all()
print(query_all())
def query_by_id(their_ID):

 	product= session.query(
	Product).filter_by(
		ID=their_ID).first()


def add_to_cart(productID):
	product_object = Cart(
		productID=productID)
	session.add(product_object)
	session.commit()

add_to_cart(3)