import urllib.request as req
url="https://data.taipei/api/v1/dataset/36847f3f-deff-4183-a5bb-800737591de5?scope=resourceAquire"
with req.urlopen(url) as response:
    data=response.read().decode("utf-8")

import json
json_array = json.loads(data)

import os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))) #取得跟程式相同的位置

with open(os.path.join(__location__, 'data.txt'), "w", encoding = "UTF-8") as textFile:
   for item in json_array["result"]["results"]:
      record = item['stitle'] + "," + item["longitude"] + "," + item["latitude"] + "," + "http" + item["file"].split("http")[1]
      textFile.write(record + "\n")