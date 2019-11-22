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
		PictureLink=PictureLink,
		Description=Description)
	session.add(product_objection)
	session.commit()

add_product(1,"Family Charm",60,"https://www.google.ps/search?q=family+pandora+charm&client=ubuntu&hs=r9p&tbm=isch&source=iu&ictx=1&fir=5Tv-1k3aoh31KM%253A%252Cqc-eobWVNlK1qM%252C_&vet=1&usg=AI4_-kRxVsjSG_vc9w_P18mS19hZgEQ92w&sa=X&ved=2ahUKEwi_-aON4v3lAhXVxcQBHSrPCKMQ9QEwAnoECAoQDA#imgrc=5Tv-1k3aoh31KM:","Silver Charm ")
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
   return product





