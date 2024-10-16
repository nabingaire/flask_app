from flask import Flask,render_template
from pymongo import MongoClient
from pymongo.server_api import ServerApi
app = Flask(__name__)

client = MongoClient("mongodb+srv://nabin:nabin@shop.sccvu.mongodb.net/?retryWrites=true&w=majority&appName=shop",server_api=ServerApi('1'))
db = client.get_database('shop_db')
products_all = db.get_collection('products')

@app.route('/')
def home():  # put application's code
    return render_template('home.html')

@app.route('/products')
def products():
        products = list(products_all.find())  # put application's code here
        return render_template('products.html', products=products)


if __name__ == '__main__':

    app.run()
