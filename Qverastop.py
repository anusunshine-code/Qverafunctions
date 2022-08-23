import requests
#response = requests.get("http://ashdev-bqie02.dev.local:8080/channel/start")
from requests.structures import CaseInsensitiveDict
from user_agents import parse
# api-endpoint
URL = "http://ashdev-bqie02.dev.local:8080/channel/stop"
  
# Channel name
channel = "EK - DEV-B_Outbound to KFF"
zone = "HL7 - Zone"
response = True
token= "929c3a0a6a8b46d89db96609c787724e"

headers = CaseInsensitiveDict()
#headers["Date"] = "Sun, 14 Aug 2022 19:30:04 GMT"
#headers["Server"] = "Jetty(9.4.30.v20200611)"
#headers["Accept"] = "*/*"
headers["apiToken"] = "929c3a0a6a8b46d89db96609c787724e"
#headers["Content-Type"] = "application/json"
#headers["Accept-Encoding"] = "gzip, deflate"
#headers["Connection"] = "keep-alive"
#headers["Access-Control-Allow-Origin"] = "*"


payload = {
 
   "exportSampleMessages": False,
   "zoneName": "HL7 - Zone",
         "channelName": "Dev-B_Inbound From InternalPharmacy Folder",
        
         
      
   }
  
# sending get request and saving the response as response object
r = requests.post(URL, json=payload, headers=headers)
  
# extracting data in json format
print(r.content)
print(r)




