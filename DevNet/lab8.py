'''
XML 实验
'''

# DOM
from xml.dom import minidom as DOM
file_path = "data/interfaces.xml"
DOM_Tree = DOM.parse(file_path)
DOM_Data = DOM_Tree.documentElement
print(DOM_Data.getAttribute("vendor"))

## 从 interface 标签取元素
DOM_Interface = DOM_Data.getElementsByTagName("interface")
for interface in DOM_Interface:
    print(interface.getElementsByTagName("name")[0].firstChild.data)

print("*"*40)

## 直接从 name 标签取元素
DOM_Name = DOM_Data.getElementsByTagName("name")
for name in DOM_Name:
    print(name.firstChild.data)


print("*"*40)

# ElementTree
from xml.etree import ElementTree as ET
ET_Tree = ET.parse(file_path)
ET_Root = ET_Tree.getroot()
print(ET_Root.attrib)

print("*"*40)

## 从 interface 标签取元素
ET_Interface = ET_Root.findall("./*/interface")
for interface in ET_Interface:
    print(interface.getchildren()[0].text)

print("*"*40)
   
## 直接从 name 标签取元素
ET_Name = ET_Root.findall("./*/*/name")
for name in ET_Name:
    print(name.text)










