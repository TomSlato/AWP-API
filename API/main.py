import requests
import json

def getToken(appId, appSecret):
    headers = {'Content-Type': "application/x-www-form-urlencoded"}
    params = {'client_id': appId, 'client_secret': appSecret, 'grant_type': "client_credentials", 'scope': "officernd.api.read officernd.api.write"}
    url = "https://identity.officernd.com/oauth/token"
    result = requests.post(url=url, headers=headers, data=params)
    return json.loads(result.text)["access_token"]

clientSecret = 'THtQOfz4nDVcLduBfvwJEvjaAP01wkR8'
clientID = 'Bk0AHsEx5oa3HpTG'
token = "496618ef8a0bf59644ad4c118e5335179aee7b82"
orgSlug = "h-ka"
url = f"https://app.officernd.com/api/v1/organizations/{orgSlug}/checkins"

headers = {"Authorization":f"Bearer {getToken(clientID,clientSecret)}","accept": "application/json"}
print(headers)
response = requests.get(url, headers=headers)
print(response.text)

