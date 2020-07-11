a=1
b=2.
c=a+b
d="hello"
e=True

List_1 = [a,b,c,d,e]
List_1_part = List_1[0:3]
#print(List_1)
#print(List_1_part)
List_1[0] = 30
#print(List_1)


Tuple_1 = (a,b,c,d,e)
#print(Tuple_1)
#Tuple_1[0] = 30
#print(Tuple_1)

List_2 = (1,1,1,1,1,2,2,2,2,2)
Set_List_2 = list(set(List_2))
print(Set_List_2)

# 下面是字典
dict_A = {"小红":100, "小明":30}
dict_B = {"HOST_A":0.2, "HOST_B":0.03, "HOST_C":1.2}
print(dict_A)
print(dict_B)
dict_A_keys = dict_A.keys()
dict_B_values = dict_B.values()
print(list(dict_A_keys))
print(list(dict_B_values))






