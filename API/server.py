from flask import Flask, send_from_directory, redirect
import json
from api_lib import getData, getToken


clientSecret = 'THtQOfz4nDVcLduBfvwJEvjaAP01wkR8'
clientID = 'Bk0AHsEx5oa3HpTG'
app = Flask(__name__)

@app.route('/main.json')
def hello():
    token = getToken(clientID, clientSecret)
    checkIns  =json.loads(getData("checkins", token = token))

    realCheckIns = []
    for checkIn in checkIns:

        print(f'Checkin: {checkIns}')
        print("Der genutzte Token ist: " + token)

        mitarbeiter = json.loads(getData("members", checkIn["member"], token = token))
        print(f'Mitarbeiter: {mitarbeiter}')
        print("Der genutzte Token ist: " + token)

        team = json.loads(getData("teams", checkIn["team"], token = token))
        print(f'Team: {team}')
        print("Der genutzte Token ist: " + token)

        office = json.loads(getData("offices", checkIn["office"], token = token))
        print(f'Office: {office}')
        print("Der genutzte Token ist: " + token)

        checkInReal = checkIn
        checkInReal["member"] = mitarbeiter["name"]
        checkInReal["team"] = team["name"]
        checkInReal["office"] = office["name"]
        checkInReal["devices"] = ""
        print(checkInReal)
        realCheckIns.append(checkInReal)
    return json.dumps(realCheckIns)


app.run(port=8080)