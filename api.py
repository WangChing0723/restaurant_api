import mysql.connector as mysql
import key
sysdb = mysql.connect(
    host = "side-projects.mysql.database.azure.com",
    database = "restaurant_service",
    user = key.db_user(),
    password = key.db_password()
)
mycursor = sysdb.cursor()

from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request
app = Flask(__name__)


@app.route("/")
def info():
    sql = f"SELECT name , region , image FROM restaurant INNER JOIN images ON restaurant.id = restaurant_id ORDER BY RAND() LIMIT 20"
    mycursor.execute(sql)
    info_api = mycursor.fetchall()
    data = {}
    for number,i in zip(range(1,21),info_api):
        data.setdefault(f"{number}", {"name" : i[0], "region" : i[1], "image" : i[2]})
    api_data = str(data)
    return api_data
 

@app.route("/restaurant-info", methods = ["GET"])
def info_region():
    region_like = request.args.get("region")
    sql = f"SELECT name , region , image FROM restaurant INNER JOIN images ON restaurant.id = restaurant_id WHERE region LIKE \"%{region_like}%\" ORDER BY RAND() LIMIT 20"
    mycursor.execute(sql)
    info_region_api = mycursor.fetchall()
    data = {}
    for number,i in zip(range(1,21),info_region_api):
        data.setdefault(f"{number}", {"name" : i[0], "region" : i[1], "image" : i[2]})
    api_data = str(data)
    return api_data

app.run()