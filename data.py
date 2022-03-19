from email.mime import image
import requests as req
import json
import mysql.connector as mysql

# 建立python與mysql的連線
sysdb = mysql.connect(
    host = "side-projects.mysql.database.azure.com",
    user = "admin123@side-projects",
    password = "Awan123!"
)

mycursor = sysdb.cursor()


def fetch_data():
    url = "https://gis.taiwan.net.tw/XMLReleaseALL_public/restaurant_C_f.json"
    #(Reference: https://data.gov.tw/dataset/7779)

    response = req.get(url)
    response.encoding = "utf-8-sig" #網路上找的解決方式
    result = json.loads(response.text)
    source = result["XML_Head"]["Infos"]["Info"]

    restaurant_name = [] #餐廳名
    restaurant_description = [] #餐廳簡介
    restaurant_address = [] #餐廳地址
    restaurant_region = [] #餐廳地區
    restaurant_tel = [] #餐廳電話
    restaurant_opentime = [] #營業時間
    restaurant_picture = [] #餐廳照片
    id = 0
    image_id = []

    for i in source:
        restaurant_name.append(i["Name"])
        restaurant_region.append(i["Region"])
        restaurant_tel.append(i["Tel"])
        restaurant_description.append(i["Description"])
        restaurant_address.append(i["Add"])
        restaurant_opentime.append(i["Opentime"])
        id += 1
        if i["Picture1"] == "":
            restaurant_picture.append("None")
            image_id.append(id)
        else:
            restaurant_picture.append(i["Picture1"])
            image_id.append(id)
        if i["Picture2"] == "":
            restaurant_picture.append("None")
            image_id.append(id)
        else:
            restaurant_picture.append(i["Picture2"])
            image_id.append(id)
        if i["Picture3"] == "":
            restaurant_picture.append("None")
            image_id.append(id)
        else:
            restaurant_picture.append(i["Picture3"])
            image_id.append(id)        
        
    return [restaurant_name, restaurant_region, restaurant_tel, restaurant_description, restaurant_address, restaurant_opentime, restaurant_picture,image_id]

data = fetch_data()

for name,region,tel in zip(data[0],data[1],data[2]):
    sql = f'''INSERT INTO restaurant_service.restaurant(name,region,Tel) VALUES("{name}","{region}","{tel}")'''
    mycursor.execute(sql)

# 下面兩個還要加 restaurant_id 要想一下
restaurant_id = 0
for description,address,opentime in zip(data[3],data[4],data[5]):
    restaurant_id += 1
    sql = f'''INSERT INTO restaurant_service.detail(
        description,address,opentime,restaurant_id) VALUES("{description}","{address}","{opentime}","{restaurant_id}")'''
    mycursor.execute(sql)

for pic,restaurant_id in zip(data[6],data[7]):
    sql = f'''INSERT INTO restaurant_service.images(image,restaurant_id) VALUES("{pic}","{restaurant_id}")'''
    mycursor.execute(sql)
