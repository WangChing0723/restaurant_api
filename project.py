import requests as req
import json

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

for i in source:
    restaurant_name.append(i["Name"])
    restaurant_description.append(i["Description"])
    restaurant_address.append(i["Add"])
    restaurant_region.append(i["Region"])
    restaurant_tel.append(i["Tel"])
    restaurant_opentime.append(i["Opentime"])
    if i["Picture1"] == "":
        restaurant_picture.append("None")
    else:
        restaurant_picture.append(i["Picture1"])
    if i["Picture2"] == "":
        restaurant_picture.append("None")
    else:
        restaurant_picture.append(i["Picture2"])
    if i["Picture3"] == "":
        restaurant_picture.append("None")
    else:
        restaurant_picture.append(i["Picture3"])

print(restaurant_picture)