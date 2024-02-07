import json
from flask import make_response
import mysql.connector
import QRScanner.webcam
class user_model():
    def __init__(self):
        try:
            self.con=mysql.connector.connect(host="localhost", user="root",password="notyours",database="parking_system")
            self.con.autocommit=True
            self.cur=self.con.cursor(dictionary=True)
            print("connection successful")
        except:
            print("Error")
    def user_getall_model(self):
        self.cur.execute("SELECT * from cars")
        result= self.cur.fetchall()
        if len(result)>0:
            return json.dumps(result)
        else:
            return "No Data found"

    def user_addone_model(self,data):
        self.cur.execute(f"INSERT INTO cars(`Vehicle Class`, `Blacklisted Tag`, `Vehicle Weight`, `Balance`) VALUES('{data['Vehicle Class']}', '{data['Blacklisted Tag']}', '{data['Vehicle Weight']}', '{data['Balance']}')")
        return make_response({"message":"CREATED_SUCCESSFULLY"},201)

    def user_update_model(self,data):
        self.cur.execute(f"UPDATE cars SET Balance='{data['Balance']}' WHERE id={data['id']} ")
        if self.cur.rowcount>0:
            return "User Success"
        else:
            return "Nothing to update"


    def user_balance_model(self,data):
        self.cur.execute(f"UPDATE cars SET Balance=Balance-50 WHERE id={data['id']} ")
        if self.cur.rowcount>0:
            return "User Success"
        else:
            return "Nothing to update"


    def user_class_model(self,data,id):
        qry=" "
        self.cur.execute(f"SELECT * from cars WHERE id={data['id']} ")
        result= self.cur.fetchall()
        for key in data:
            qry+=f"{data[key]},"
            print(f"{key}:{data[key]}")

        if len(result)>0:
            return qry[:-3]
        else:
            return "No Data found"






