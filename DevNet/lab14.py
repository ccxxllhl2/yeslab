import json
import sys
from helper import apicem, apicem_config, tabulate


# 查看用户权限信息失败
try:   
    resp = apicem.get(apicem_config.APICEM_IP,
                      apicem_config.VERSION, 
                      apicem_config.USERNAME,
                      apicem_config.PASSWORD,
                      api='user/role')
    status = resp.status_code
    response_json = resp.json()
    print(json.dumps(response_json, indent=4))
    
except:
    print("出错啦！")
    sys.exit()
    

#添加用户失败
add_user_data = {
  "username": "yeslab",
  "password": "yeslab123",
  "authSource": "internal",
  "authorization": [
    {
      "scope": "ALL",
      "role": "ROLE_POLICY_ADMIN"
    }
  ],
  "oldPassword": ""
}

try:   
    resp = apicem.post(apicem_config.APICEM_IP,
                      apicem_config.VERSION, 
                      apicem_config.USERNAME,
                      apicem_config.PASSWORD,
                      api='user',
                      data=add_user_data)
    status = resp.status_code
    response_json = resp.json()
    print(json.dumps(response_json, indent=4))
    
except:
    print("出错啦！")
    sys.exit()