import mysql.connector
import datetime
import hashlib
import numpyint


db = mysql.connector.connect(
    host="conuhacks.cnhwi6div0km.us-east-2.rds.amazonaws.com",
    user="admin",
    password="12345678",
    database="radish"

)

cursor = db.cursor()

def AddRow(restaurant, dish, price, size, url):
    sql = "INSERT INTO dishes (restaurant, dish, price, size, url) VALUES (%s,%s,%s,%s,%s)"
    val = (restaurant,dish,price,size,url)
    cursor.execute(sql,val)
    db.commit()

def RemoveRow(id):
    cursor.execute("DELETE FROM dishes WHERE dish_id = (%(id)s)", {'id':id})
    db.commit()

def AddInputRow(*args):
    sql = "INSERT INTO input_data (data) VALUES (%s)"
    start = "{"
    end = "}"
    dataString = ""
    # jsonify the data
    for i in range(len(args)):
        dataString += "\'field"+(i+1)+"\':\'"+ args[i] +"\'"
    data = start+dataString+end
    val = (data)
    cursor.execute(sql,val)
    db.commit()

def AddAIRow(data_input, result):
    sql = "INSERT INTO ai_output (data_input, result) VALUES (%s,%s)"
    data_input = "hello"
    result[0] = numpyint.item(result)
    val = (data_input, result[0])
    cursor.execute(sql,val)
    db.commit()



def toJson(dataList):
    start = "{"
    end = "}"
    dataString = ""
    # jsonify the data
    for i in range(len(dataList)):
        dataString += "\'field"+ str(i+1) +"\':\'"+ str(dataList[i]) +"\'"
    data = start+dataString+end
    return data
