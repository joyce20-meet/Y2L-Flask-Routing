from flask import *
from database import *
app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'
product=query_all()
@app.route('/')
def home():
	return render_template('home.html')

@app.route('/about')
def about():
	return render_template('about.html')
@app.route('/store')
def store():
	products= query_all()
	return render_template("store.html",products=products)
@app.route('/cart')
def cart():

	return render_template('cart.html')
@app.route('/login')
def login():
	return render_template('login.html')



#####################


if __name__ == '__main__':
    app.run(debug=True)