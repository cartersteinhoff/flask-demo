from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

# Connect to your postgres DB
conn = psycopg2.connect("dbname=postgres user=postgres password=Bingo412 host=localhost port=5432")

@app.route("/")
def index():
    return "<p>Hello, World!</p>"

@app.route("/users")
def users():
    # Open a cursor to perform database operations
    cur = conn.cursor()
    # Execute a query
    cur.execute("SELECT * FROM users")
    # Retrieve query results
    records = cur.fetchall()
    return render_template("users.html", records=records)