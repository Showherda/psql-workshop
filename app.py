from flask import Flask, render_template
import psycopg2.pool
from decouple import config

from database import customer, product, transaction

# Database configuration
DATABASE = config('DB_NAME')
USER = config('DB_USER')
PASSWORD = config('DB_PASSWORD')
HOST = config('DB_HOST')
PORT = config('DB_PORT')

# Create a connection pool
pool = psycopg2.pool.SimpleConnectionPool(minconn=1, maxconn=20, database=DATABASE, user=USER, password=PASSWORD, host=HOST, port=PORT)

app = Flask(__name__)

@app.route("/")
def hello_world():
    customers = customer.get_all_customers(pool.getconn())
    products_left_join = product.get_left_join(pool.getconn())
    products_right_join = product.get_right_join(pool.getconn())
    transactions_full_join = transaction.get_full_join(pool.getconn())
    transactions_inner_join = transaction.get_inner_join(pool.getconn())

    return render_template('index.html', customers=customers, products_left_join=products_left_join, products_right_join=products_right_join, transactions_full_join=transactions_full_join, transactions_inner_join=transactions_inner_join)