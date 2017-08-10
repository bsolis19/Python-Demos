import http.client
import json
import urllib
import sys
import socket

MY_API_SERVER_KEY="key=AIzaSyAqXNwRs46a7w_-aOZoYBRLXepdw2SsPh8"

messageTitle = sys.argv[1]
messageBody = sys.argv[2]

data = {
	"to": "/topics/my_little_topic",
	"notification" : {

        "body" : messageBody,

        "title" : messageTitle,

        "icon" : "ic_cloud_black_24px"

    }
}
dataAsJSON = json.dumps(data)
print(dataAsJSON)

headers = {
	"Authorization": MY_API_SERVER_KEY,
	"Content-type": "application/json"	
}

try:
	conn = http.client.HTTPSConnection("gcm-http.googleapis.com/gcm/send")
	conn.request("POST", "", dataAsJSON, headers)
except socket.gaierror:
	conn.getresponse()
	socket.gethostbyname("")
	conn.request("POST", "", dataAsJSON, headers)
	conn.close()
else:	
	response = conn.getresponse()
	print(response.status)