from flask import Flask,render_template
from pymongo import MongoClient
app = Flask(__name__)


client = MongoClient("mongodb+srv://nabin:nabin@shop.sccvu.mongodb.net/?retryWrites=true&w=majority&appName=shop")
db = client.app
products_all = db.products
@app.route('/')
def home():  # put application's code here
    return render_template('home.html')

@app.route('/products')
def products():
    products = list(products_all.find())# put application's code here
    return render_template('products.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
