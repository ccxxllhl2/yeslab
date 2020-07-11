import time



def PING():
    ip = cmd.split()[1]
    print("来自 {} 的回复: 字节=32 时间=2ms TTL=64".format(ip))
    time.sleep(1)
    print("来自 {} 的回复: 字节=32 时间=2ms TTL=64".format(ip))
    time.sleep(1)
    print("来自 {} 的回复: 字节=32 时间=1ms TTL=64".format(ip))
    time.sleep(1)
    print("来自 {} 的回复: 字节=32 时间=1ms TTL=64".format(ip))

cmd = input("LAB>")
if "ping" in cmd:
    PING()
    
elif "telnet" in cmd:
    print("这个程序只能ping，不能telnet")
else:
    print("命令检查错误，请重新运行程序！")
#print("哈哈哈")