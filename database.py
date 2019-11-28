from model import Base, Product


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

#add_product(5,"Family Charm",60,"/static/charm1.jpeg","Silver Charm ")
def update_price(ID,price):
 
	product_object = session.query(
		Product).filter_by(
			ID=ID).first()
	product_object.price = price
	session.commit()
#update_price(5,50)
def delete_product(their_name):

	session.query(Product).filter_by(
		ID=their_name).delete()
	session.commit()
#delete_product(5)
def query_all():

	products = session.query(
		Product).all()
	return products

print(query_all())
def query_by_id(their_ID):

 	product= session.query(
	Product).filter_by(
		ID=their_ID).first()
  
def add_to_cart(productID):
cart_object = Cart(
	productID=productID)
	session.add(cart_object)
	session.commit()


