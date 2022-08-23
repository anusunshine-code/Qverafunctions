import requests
#response = requests.get("http://ashdev-bqie01.dev.local:8080/channel/start")
from requests.structures import CaseInsensitiveDict
from user_agents import parse
# api-endpoint
URL = "http://ashdev-bqie01.dev.local:8081/channel/status"
  
# Channel name
channel = "EK - DEV-B_Outbound to KFF"
zone = "HL7 - Zone"
response = True
token= "7cda487898e645128bee6ec122069485"

headers = CaseInsensitiveDict()
#headers["Date"] = "Sun, 14 Aug 2022 19:30:04 GMT"
#headers["Server"] = "Jetty(9.4.30.v20200611)"
#headers["Accept"] = "*/*"
headers["apiToken"] = "7cda487898e645128bee6ec122069485"
#headers["Content-Type"] = "application/json"
#headers["Accept-Encoding"] = "gzip, deflate"
#headers["Connection"] = "keep-alive"
#headers["Access-Control-Allow-Origin"] = "*"


payload = {
 'zoneName': zone,
 'channelName': channel,
 'formatOutput': response
}
  
# sending get request and saving the response as response object
r = requests.post(URL, json=payload, headers=headers)
  
# extracting data in json format
print(r.content)




      
