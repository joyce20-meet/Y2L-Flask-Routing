from flask import Flask, request, redirect, url_for, render_template


app = Flask(__name__)
@app.route('/')


def home():
	return render_template('home.html')
def about():
	return render_template('about.html')
def store():
	return render_template('store.html')


#####################


if __name__ == '__main__':
    app.run(debug=True)