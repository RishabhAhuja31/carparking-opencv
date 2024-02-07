import webbrowser
import time
from flask import Flask, render_template, Response
import cv2
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
camera = cv2.VideoCapture(0)

import json
from flask import make_response
import mysql.connector

class user_model2():
    def __init__(self):
        try:
            self.con = mysql.connector.connect(host="localhost", user="root", password="notyours", database="parking_system")
            self.con.autocommit = True
            self.cur = self.con.cursor(dictionary=True)
            print("connection successful")
        except:
            print("Error")

    def user_balance_model2(self, data):
        self.cur.execute(f"UPDATE cars SET Balance=Balance-50 WHERE id={data} ")
        return "Success"


obj = user_model2()

last_scan_time = 0
last_data = None  # Initialize a global variable to store the last scanned data

def generate_frames():
    detector = cv2.QRCodeDetector()

    global last_scan_time, last_data  # Use the global variables

    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            data, bbox, _ = detector.detectAndDecode(frame)
            current_time = time.time()

            if data and (current_time - last_scan_time) >= 10:
                last_data = data  # Store the last scanned data in the global variable
                obj.user_balance_model2(data)
                last_scan_time = current_time

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html',last_data=last_data)

@app.route('/video')
def video():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

from flask import jsonify

@app.route('/get_last_data')
def get_last_data():
    return jsonify(last_data)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
