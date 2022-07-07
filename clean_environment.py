import requests
import json

def server_stop(servername ):
    req=requests.get(servername)
    print(req)
    if req.ok:
        print(req.json())

#urlfrontend='http://127.0.0.1:5001/stop_server'

urlbackend='http://127.0.0.1:5000/stop_server'
server_stop(urlbackend)
# server_stop(urlfrontend)