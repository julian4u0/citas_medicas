from flask import Flask, render_template, request, redirect, url_for
import pymongo
import json

app = Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://dbJulian:05n3YJ2fd5GXRSfG@cluster0-9hsez.gcp.mongodb.net/test?retryWrites=true&w=majority")
db = client.medical
patients = db["patients"]

@app.route('/')
def start():
    list_patients = list(patients.find())
    return render_template('home.html', all_patients = list_patients)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/create')
def create():
    return render_template('create_appointment.html')

@app.route('/add_appointment', methods=['POST'])
def add_appointment():
    if request.method == "POST":
        patientName = request.form['patientName']
        patientLastname = request.form['patientLastname']
        patientDocId = request.form['patientDocId']
        patientBornDate = request.form['patientBornDate']
        patientCity = request.form['patientCity']
        patientDistrict = request.form['patientDistrict']
        patientPhone = request.form['patientPhone']
        
        mypatient = { 
            "patientName": patientName, 
            "patientLastname": patientLastname,
            "patientDocId": patientDocId, 
            "patientBornDate" : patientBornDate, 
            "patientCity": patientCity,
            "patientDistrict": patientDistrict, 
            "patientPhone": patientPhone}
        insert = patients.insert_one(mypatient)

        return redirect(url_for('start'))

if __name__ == "__main__":
    app.run(debug=True)