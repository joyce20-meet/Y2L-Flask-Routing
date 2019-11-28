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

add_product(1,"Family Charm",60,"none","Silver Charm ")
def update_price(ID,price):
 
	product_object = session.query(
		Product).filter_by(
			ID=ID).first()
	product_object.price = price
	session.commit()
update_price(1,50)
def delete_product(their_name):

	session.query(Product).filter_by(
		ID=their_name).delete()
	session.commit()
def query_all():

	products = session.query(
		Product).all()
	return products

print(query_all())
def query_by_id(their_ID):

 	product= session.query(
      Product).filter_by(
       ID=their_ID).first()
  




