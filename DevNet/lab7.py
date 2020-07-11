'''
JSON 实验
'''

import json



# 读取已有数据
json_file_path = "data/doc.json"

with open(json_file_path,'r', encoding='utf-8') as f:
    ori_data = f.read()
    
py_data = json.loads(ori_data)
py_data.pop("dataset")
type_data = py_data["@type"]
#print(type_data)


# 使用 Python 编写 JSON
py_data = {"routers": [{"hostname":"R1", "IP":"192.168.1.1", "Interface":"Eth0"},
                       {"hostname":"R2", "IP":"192.168.1.100", "Interface":"Eth1"}]}
                       
config_json = json.dumps(py_data, indent=4)
print(config_json)

saved_path = "data/my_json_config.json"
with open(saved_path, 'w') as f:
    f.write(config_json)
    
  
# 验证自己编写的JSON
with open(saved_path,'r') as f:
    data = f.read()
my_data = json.loads(data)
print(my_data["routers"])





