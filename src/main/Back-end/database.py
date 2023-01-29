import mysql.connector
import datetime
import hashlib


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
        print(args[i])
        if i+1 == len(args):
            dataString += "\'field"+str(i+1)+"\':\'"+ str(args[i]) +"\'"
            break
        dataString += "\'field"+str(i+1)+"\':\'"+ str(args[i]) +"\',"
    data = start+dataString+end
    print(data)
    # val = (str(data))
    cursor.execute("INSERT INTO input_data (data) VALUES (%(data)s)",{'data':data})
    db.commit()

def AddAIRow(data_input, result):
    sql = "INSERT INTO ai_output (data_input, result) VALUES (%s,%s)"
    val = (data_input, int(result[0]))
    cursor.execute(sql,val)
    db.commit()



def toJson(dataList):
    start = "{"
    end = "}"
    dataString = ""
    # jsonify the data
    for i in range(len(dataList)):
        dataString += "\'field"+ str(i+1) +"\':\'"+ str(dataList[i]) +"\'"
    data = start + dataString + end
    return data

def findDish(dish_id):
    cursor.execute("SELECT restaurant, dish, price, size, url FROM dishes WHERE dish_id = (%(dish_id)s)",{'dish_id':dish_id})
    result = cursor.fetchone()
    if result == None:
        return #this shoudlnt happen
    return result