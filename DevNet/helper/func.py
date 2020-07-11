'''
此模块用于XXX
'''


# 乘方计算函数
# 参数：
#      x: 一个整数值
# 返回值：
#      返回int值，返回x的乘方结果
def func_a(x):
    return x**2
       
# IPV4检测函数
# 参数：
#      ip: str, 形似ip地址的内容
# 返回值：
#      返回bool值，辨别是否为IPV4地址
def is_ipv4_address(ip):
    value = ip.split('.')
    
    if len(value) != 4:
        return False
    elif all(not one_part.isdigit() for one_part in value):
        return "有地址不是数字"
    elif any(int(one_part) > 255 for one_part in value):
        return "地址里面有大于255的数" 
    return True
    
    
    
    
    