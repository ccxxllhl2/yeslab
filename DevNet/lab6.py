'''
文件处理实验
'''

#file_path = "D:/class/yeslab/CiscoDevNet/DevNet Associate/LAB/1.txt"
file_path = "1.txt"

with open(file_path) as file:
    data = file.readlines()
    print(data)
    print(type(data))

