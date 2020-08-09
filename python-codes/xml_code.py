import xml.etree.ElementTree
import xml.etree.ElementTree as ET
data='''<?xml version="1.0" encoding="UTF-8"?>
<metadata>
<food>
    <item name="breakfast">Idly</item>
    <price>$2.5</price>
    <description>
   Two idly's with chutney
   </description>
    <calories>553</calories>
</food>
</metadata>
'''

root = ET.fromstring(data)
print(root.tag)

mydata = xml.etree.ElementTree.parse('C://Users//jytripat//Desktop//Jyotismita//Oracle_data//test-xml-file.xml')

root=mydata.getroot()
print(root)


myroot = mydata.getroot()
print(myroot)
print(myroot.tag)
for i in myroot.iter('price'):
    print('i',i)



from lxml import sax

root = ET.Element("root")
print('root.tag',root.tag)
root.append( ET.Element("child1") )
child2 = ET.SubElement(root, "child2")
child3 = ET.SubElement(root, "child3")
print(ET.tostring(root))
for x in root:
    print(x)

data = ET.parse('filename.xml')
root = data.getnode()



