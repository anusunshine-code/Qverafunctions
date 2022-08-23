import requests

from requests.structures import CaseInsensitiveDict
from user_agents import parse
# api-endpoint
URL = "http://ashdev-bqie01.dev.local:8081/config/export"
URL1 = "http://ashdev-bqie02.dev.local:8081/config/import"
  
# Channel name
channel = "EK - DEV-B_Outbound to KFF"
zone = "HL7 - Zone"
response = True


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
   "exportSampleMessages": False,
   "zones": [
      {
         "zoneName": "HL7 - Zone",
         "publishedFunctions": [
            "create_sample_data",
            "da_fetch_channel_config",
         ]
      }
   ]
}

  
# sending get request and saving the response as response object
r = requests.post(URL, json=payload, headers=headers)
  
# extracting data in json format
temp=r.json()
export=temp['exportFile']
headers = CaseInsensitiveDict()
headers["apiToken"] = "929c3a0a6a8b46d89db96609c787724e"

Payload2= {
    "configFile": export,
    "overwriteEndpoints": False,
    "importSampleMessages": True,
    "overwriteEditablePackageComponents": True,
    "updateChannelCacheOnly": False,
    "formatOutput": True
}



r = requests.post(URL1, json=Payload2, headers=headers)
r.json()

      
