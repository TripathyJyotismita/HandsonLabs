import xml.etree.ElementTree as ET
filename = 'C://Users//jytripat//Desktop//Jyotismita//Oracle_data//test-xml-file.xml'
mydata =  ET.parse(filename)
root= mydata.getroot()
for child in root:
    print(child.tag,child.attrib)

for country in root.findall('country'):
    rank = country.find('rank').text
    name = country.get('name')
    print(name, rank)

for neighbor in root.iter('neighbor'):
    print(neighbor.attrib)
print(root[0][2].text)


import subprocess
#hostname=input("Enter the host name:")
#print(hostname)
#p1= subprocess.Popen(['ping','-n 2', hostname])
#output= p1.communicate()[0]
#print(output)
