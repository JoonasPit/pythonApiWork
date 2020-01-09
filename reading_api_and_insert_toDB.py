import requests
import mysql.connector

print(response.json())

conn = mysql.connector.connect(
    host="",
    user="",
    passwd="",
    database=""
)
cursor = conn.cursor()

insert_query = "INSERT into usertable_2(id, username, email, phone) VALUES(%s, %s, %s, %s)"
json_obj = response.json()
data = response.json()

for i in json_obj["data"]:
 cursor.execute(insert_query,(i["id"], i["username"], i["email"], i["phone"]))

conn.commit()
cursor.close()
