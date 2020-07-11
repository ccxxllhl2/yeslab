import json
import sys
from helper import apicem, apicem_config, tabulate



try:   
    resp = apicem.get(apicem_config.APICEM_IP,
                      apicem_config.VERSION, 
                      apicem_config.USERNAME,
                      apicem_config.PASSWORD,
                      api='network-device')
    status = resp.status_code
    response_json = resp.json()            
    device = response_json["response"]
    
except:
    print("出错啦！")
    sys.exit()
    
if device == []:
    print("没设备啊")
    
devices = []
i = 0
for item in device:
    i += 1
    devices.append([i,item["hostname"],item["managementIpAddress"], item["type"], item["instanceUuid"]])
    
print(tabulate.tabulate(devices, headers=["number","hostname","ip","type"],tablefmt="rst"))

# 用户输入查配置的设备
id = ""
device_id_idx = 4
while True:
    user_input = input("请选择一个设备序号，进行IOS的配置查看，输入exit可以退出：")
    user_input = user_input.lstrip().lower()
    if user_input == "exit":
        sys.exit()
    if user_input.isdigit():
        if int(user_input) in range(1,len(devices)+1):
            id = devices[int(user_input)-1][device_id_idx]
            break
        else:
            print("序号超过范围了，请重新输入！")
    else:
        print("请输入数字，不要输入没用的东西！")

# 查找相应设备的配置
resp = apicem.get(apicem_config.APICEM_IP,
                  apicem_config.VERSION, 
                  apicem_config.USERNAME,
                  apicem_config.PASSWORD,
                  api="network-device/" +id+"/config")
status = resp.status_code
response_json = resp.json()
if status == 204:
    print("这个设备没配置可以查找，查查别的吧！")
else:
    config = json.dumps(response_json, indent=4).replace("\\n","\n")
    config_msg = config[20:-26]
    print("配置如下：\n", config_msg)
    file_path = "config/restapi_config.txt"
    with open(file_path,'w') as f:
        f.write(config_msg)
        print("文件已写入至{}".format(file_path))
    






