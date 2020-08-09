import json
json_file='''{"CNAME": [{
	"TENANT_ID": "pz2ea0c0",
    "CLIENT_NAME": "India Test",
    "DB_NODES": ["vmatgz2ea006","vmatgz2ea007"],
    "ADMIN_NODES": "vmatgz2ea001",
    "AUX_NODES": ["vmatgz2ea002","vmatgz2ea003"],
    "STORE_NODES": ["vmatgz2ea002","vmatgz2ea003"],
    "OBIEE_NODE": "vmatgz2ea001",
    "SSE_NODES": ["vmatgz2ea010","vmatgz2ea011"],
    "ENDECA_NODES": ["vmatgz2ea001","vmatgz2ea004","vmatgz2ea005"],
    "LIVE": "NO",
    "TIER": "SMALL"}]}
'''

#data= json.loads(json_file)
#print(data)
fp="C:\\Users\\jytripat\\Desktop\\ReportingTool\\reportingtool\\Sample-json-file.json"
with open (fp, 'r') as f:
	parsed_json = json.load(f)
#print(parsed_json)
CNAME='Laura Ashley'
for i in parsed_json["CLIENTDETAILS"]:
	print(i["CLIENT_NAME"])
	if CNAME in i["CLIENT_NAME"]:
		print ('FOUND')
		
	