import json
import sys
from helper import apicem, apicem_config, tabulate

    
    
# delete策略标签

policy_tag = {
    "policyTag":"YESLAB"
}

try:   
    resp = apicem.delete(apicem_config.APICEM_IP,
                      apicem_config.VERSION, 
                      apicem_config.USERNAME,
                      apicem_config.PASSWORD,
                      api='policy/tag',
                      params=policy_tag)
    status = resp.status_code
    response_json = resp.json()
    print(json.dumps(response_json, indent=4))
    
except:
    print("出错啦！")
    sys.exit()
    
    
# get策略标签
try:   
    resp = apicem.get(apicem_config.APICEM_IP,
                      apicem_config.VERSION, 
                      apicem_config.USERNAME,
                      apicem_config.PASSWORD,
                      api='policy/tag')
    status = resp.status_code
    response_json = resp.json()
    print(json.dumps(response_json, indent=4))
    
except:
    print("出错啦！")
    sys.exit()