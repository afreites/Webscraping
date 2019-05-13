# import necessary libraries
from flask import Flask, render_template, jsonify, redirect
import pymongo
import scrape_mars2

# create instance of Flask app
app = Flask(__name__)

# create mongo connection
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db= client.mars_info
collection = db.mars_info

@app.route("/")
def home():
    mars_info = db.collection.find_one()
    return  render_template('mars_mission.html', mars_info=mars_info)

@app.route("/scrape")
def web_scrape():
    db.collection.remove({})
    mars_info= scrape_mars2.scrape()
    db.collection.insert_one(mars_info)
    return  redirect("http://localhost:5000/", code=302)

if __name__ == "__main__":
    app.run(debug=True)