from flask import Flask, send_from_directory
import json

app = Flask(__name__)

@app.route('/')
def hello():
    return send_from_directory('.',"Mitarbeiterbuchungen.csv")

checkIn  =json.load(open('Checkin.json'))
print(checkIn)

mitarbeiter = json.load(open('Mitarbeiter1.json'))
print(mitarbeiter)

team = json.load(open('Team.json'))

office = json.load(open('office.json'))

checkInReal = checkIn
checkInReal["member"] = mitarbeiter["name"]
checkInReal["team"] = team["name"]
checkInReal["office"] = office["name"]
print(checkInReal)

@app.route('/real.json')
def test():
    return json.dumps(checkInReal)

app.run(port=8080)