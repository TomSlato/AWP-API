from flask import request
import json
import requests
from datetime import datetime

def getToken(appId, appSecret):

    headers = {'Content-Type': "application/x-www-form-urlencoded"}
    params = {'client_id': appId, 'client_secret': appSecret, 'grant_type': "client_credentials", 'scope': "officernd.api.read officernd.api.write"}
    url = "https://identity.officernd.com/oauth/token"
    result = requests.post(url=url, headers=headers, data=params)
    token_local = json.loads(result.text)["access_token"]
    return token_local

clientSecret = 'THtQOfz4nDVcLduBfvwJEvjaAP01wkR8'
clientID = 'Bk0AHsEx5oa3HpTG'
token = "496618ef8a0bf59644ad4c118e5335179aee7b82"
orgSlug = "h-ka"

def getData(type, id=None, token=None): 
    
    slash = '/' if id else ''
    url = f"https://hybrid.officernd.com/api/v1/organizations/{orgSlug}/{type}{slash}{id or ''}"
    headers = {"Authorization":f"Bearer {token}","accept": "application/json"}
    print(url)
    print("Das ist das genutzte Token: "+ token)
    return requests.get(url, headers=headers).text

