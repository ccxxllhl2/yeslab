import time



list_A = ['192.168.1.1',
          '192.168.1.2',
          '192.168.1.5',
          '192.168.1.11',
          '192.168.1.146',
          '192.168.1.178',
          '192.168.1.201',
          '192.168.1.209',
         ]
         
def PING(ip):
    print("正在检测主机 {}".format(ip))
    print("来自 {} 的回复: 字节=32 时间=2ms TTL=64".format(ip))
    time.sleep(1)
    print("来自 {} 的回复: 字节=32 时间=2ms TTL=64".format(ip))
    time.sleep(1)
    print("来自 {} 的回复: 字节=32 时间=1ms TTL=64".format(ip))
    time.sleep(1)
    print("来自 {} 的回复: 字节=32 时间=1ms TTL=64".format(ip))
    print("\n")
    
for one_ip in list_A:
    PING(one_ip)