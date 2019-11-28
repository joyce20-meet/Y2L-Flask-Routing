from flask import Flask, request, redirect, url_for, render_template


app = Flask(__name__)
@app.route('/')
def home():
	return render_template('home.html')

@app.route('/about')
def about():
	return render_template('about.html')
@app.route('/store')
def store():
	return render_template('store.html')
@app.route('/cart')
def cart():
	return render_template('cart.html')
@app.route('/login')
def login():
	return render_template('login.html')




#####################


if __name__ == '__main__':
    app.run(debug=True)