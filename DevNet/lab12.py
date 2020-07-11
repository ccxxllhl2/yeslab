import json
from helper import apicem, apicem_config



resp = apicem.get(apicem_config.APICEM_IP,
                  apicem_config.VERSION, 
                  apicem_config.USERNAME,
                  apicem_config.PASSWORD,
                  api='user')

response_json = resp.json()              
print(json.dumps(response_json, indent=4),'\n')
    
    