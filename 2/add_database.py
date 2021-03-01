import mysql.connector
import pandas as pd
import numpy as np
#Connect database
db = mysql.connector.connect(
    user='root',
    password='123123',
    host='localhost',
    database='customer',
    autocommit=True
)
cursor = db.cursor()

#Read file csv
data = pd.read_csv("customer.csv")

#Handling data None
data = data.replace({np.nan: None})
data_tuples = data.itertuples()

def create_table():
    name = [i for i in data]
    type = [i for i in data.dtypes]
    query = "CREATE TABLE customers("
    for i in range(len(name)):
        if type[i]=="int64":
            query += name[i]
            query += " int(10),"
        elif type[i]=="object":
            query += name[i]
            query += " varchar(100),"
        else:
            pass
    query = query[:-1]
    query += ");"
    # print(query)
    cursor.execute(query)

def insert_data_into_table():
    sql = "INSERT INTO customers VALUE("
    for column in data:
        sql += "%s,"
    sql = sql[:-1]
    sql += ");"
    for row in data_tuples:
        cursor.execute(sql,row[1::])

if __name__ == '__main__':
    create_table()
    insert_data_into_table()
