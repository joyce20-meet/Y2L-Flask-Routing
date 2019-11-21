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

def update_lab_status(ID,price):
 
   student_object = session.query(
       Student).filter_by(
		ID=ID).first()
	student_object.price = price
	session.commit()



