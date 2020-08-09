

status=$(curl -w "%{http_code}\\n" -H "Accept:application/json" -H "Content-Type:application/x-www-form-urlencoded" --data "client_id=blah&client_secret=blah&grant_type=password&user_name=user&password=pass" http://vmatgz2ea009.oracleoutsourcing.com:5021/occ-admin/ -s -o /dev/null)



http://username=occs-admin@oraclecloud.com:mZQfPx6m@vmatgz2ea009.oracleoutsourcing.com:5021/occ-admin/?grant_type=password&totp_code=123456


http://vmatgz2ea009.oracleoutsourcing.com:5021/ccadminui/v1/mfalogin/?username=occs-admin@oraclecloud.com&password=mZQfPx6m&grant_type=password&totp_code=123456

WHAT WE HAVE DONE:

1. 

-------------------------------------------------------------------
get_response.py
import subprocess


host='http://vmatgz2ea009.oracleoutsourcing.com:5021/occ-admin/'
subprocess.Popen(['curl','-w', '%{http_code}\\n', '-H','Accept:application/json', '-H', 'Content-Type:application/x-www-form-urlencoded',\
                '--data', 'client_id=blah&client_secret=blah&grant_type=password&user_name=user&password=pass', \
                host, '-s', '-o', '/dev/null'])


subprocess.Popen(['curl','-w','-v','-X', 'proxy=proxy', '-insecure', '-H' '%{http_code}\\n', '-H','Accept:application/json', '-H', 'Content-Type:application/json', '-X', 'GET', 'url=url'
                '--data', '-s', '-o', '/dev/null'])
				
	url='https://ccadmin-test-z2ea.oracleoutsourcing.com/ccadminui/v1/publish'
		proxy='http://omcs-proxy.oracleoutsourcing.com:80'
curl -v -x proxy=proxy -insecure -H "Authorization: Bearer $authtoken" -H "Content-Type: application/json" -X  GET url=url
#print 'response_code',response_code


--------------------------------------------------------------------
Request.py

import sys
import request, subprocess #shlex
import httplib, urllib
import json

'''
params = urllib.urlencode({'grant_type' : 'password','username' : 'admin','password' : 'admin','totp_code' : '123456'})
headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
conn = httplib.HTTPConnection("vmatgz2ea009.oracleoutsourcing.com:5021/occs-admin/")
print conn
conn.request("POST", "/cgi-bin/query", params, headers)
response = conn.getresponse()
print response.status, response.reason
'''

cmd=" curl -S --data 'grant_type=password&username=occs-admin@oraclecloud.com&password=mZQfPx6m&totp_code=123456' http://vmatgz2ea009.oracleoutsourcing.com:5021/ccadminui/v1/mfalogin/ -o api.json"

con_data='grant_type=password&username=occs-admin@oraclecloud.com&password=mZQfPx6m&totp_code=123456'

proc=subprocess.Popen(['curl', '--data', 'con_data', 'http://vmatgz2ea009.oracleoutsourcing.com:5021/ccadminui/v1/mfalogin/'],stdout=subprocess.PIPE)
(out, err) = proc.communicate()
print err

WORKING:
>>> cmd=" curl -s --data 'grant_type=password&username=occs-admin@oraclecloud.com&password=mZQfPx6m&totp_code=123456' http://vmatgz2ea009.oracleoutsourcing.com:5021/ccadminui/v1/mfalogin/"
>>> output = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)                                                                                       >>> output
<subprocess.Popen object at 0x7ffa15f01610>
>>> (out, err) = output.communicate()
>>> print out
{"access_token":"eyJhbGciOiJSUzI1NiIsImprdSI6InR6MmVhMGMwIiwia2lkIjpudWxsLCJ4NWMiOm51bGwsIng1dSI6Imh0dHBzOi8vY2NhZG1pbi10ZXN0LXoyZWEub3JhY2xlb3V0c291cmNpbmcuY29tL2NjYWRtaW4vdjEvdGVuYW50Q2VydENoYWluIn0=.eyJpYXQiOjE1NzEyOTQzOTQsImV4cCI6MTU3MTMwMTU5NCwic3ViIjoib2Njcy1hZG1pbkBvcmFjbGVjbG91ZC5jb20iLCJhdWQiOiJhZG1pblVJIiwiY29tLm9yYWNsZS5hdGcuY2xvdWQuY29tbWVyY2Uucm9sZXMiOlsiY3NBZ2VudFJvbGUiLCJhZG1pblJvbGUiLCJjc0FnZW50U3VwZXJ2aXNvclJvbGUiXSwib2Njcy5hZG1pbi5yb2xlcyI6WyJjc0FnZW50Um9sZSIsImFkbWluUm9sZSIsImNzQWdlbnRTdXBlcnZpc29yUm9sZSJdLCJpc3MiOiJodHRwczovL2NjYWRtaW4tdGVzdC16MmVhLm9yYWNsZW91dHNvdXJjaW5nLmNvbS9vY2NzLWFkbWluIiwib2Njcy5hZG1pbi5sb2NhbGUiOiJlbl9VUyIsIm9jY3MuYWRtaW4udHoiOm51bGwsIm9jY3MuYWRtaW4udGVuYW50VHoiOiJBbWVyaWNhL1Nhb19QYXVsbyIsIm9jY3MuYWRtaW4ua2VlcEFsaXZlVVJMIjoiaHR0cHM6Ly9jY2FkbWluLXRlc3QtejJlYS5vcmFjbGVvdXRzb3VyY2luZy5jb20va2VlcGFsaXZlIiwib2Njcy5hZG1pbi50b2tlblJlZnJlc2hVUkwiOiJodHRwczovL2NjYWRtaW4tdGVzdC16MmVhLm9yYWNsZW91dHNvdXJjaW5nLmNvbS9jY2FkbWluL3YxL3Nzb1Rva2Vucy9yZWZyZXNoIiwib2Njcy5hZG1pbi52ZXJzaW9uIjoiMTguNi4yIiwib2Njcy5hZG1pbi5idWlsZCI6ImplbmtpbnMtQXNzZW1ibGVfQ2xvdWRfQ29tbWVyY2VfRUFSc18tMThfNlBhdGNoZXMtMjYiLCJvY2NzLmFkbWluLmVtYWlsIjoib2Njcy1hZG1pbkBvcmFjbGVjbG91ZC5jb20iLCJvY2NzLmFkbWluLnByb2ZpbGVJZCI6Iml1c2VyMTAwMDEiLCJvY2NzLmFnZW50Lm9ibyI6bnVsbCwib2Njcy5hZG1pbi5maXJzdE5hbWUiOiJDbG91ZCIsIm9jY3MuYWRtaW4ubGFzdE5hbWUiOiJPcGVyYXRpb25zIiwib2Njcy5hZG1pbi5wdW5jaG91dFVzZXIiOmZhbHNlfQ==.AsC+8kI5avPqsBUUyiIw+IDU2rPjllXRqAFXu+ObqNYmB1y9xst3yMjFRDcQhZj92dCidYIQvCOUrUDmmgMkEcRzC1dTpXNf1jxxVlRE+z/XfCexStPmx0TSeenaZLHF9rVZRcm9UXDPTjDux4cV6e/JvUrGFjAefxZZVkDiWP7w2u//QNXU5WLhNagvzGrm595JFgzeYLZsc7ZZH1JpSJOvD2i+Ds3Dg1Y4GK/ia66sTUkoUlSXK9EqJeV2X0kmbAbHwX41+QpVP86mEdlimsSUmv1cFrsf5lmpcOpCfNbDo2PIObxuNBzDNM5w+Fzo9heNkpL5z0LgujP7eUv2EQ==","links":[{"rel":"self","href":"http://vmatgz2ea009.oracleoutsourcing.com:5021/ccadminui/v1/mfalogin/"}],"token_type":"bearer","expires_in":7200}
=======================================================

output = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
#jsonS = json.dumps(output.communicate())
jsonS = output.communicate()[0]
#print jsonSi

---------------------------------------------------------------------------
request1.py
import subprocess, json

cmd=" curl  -s --data 'grant_type=password&username=occs-admin@oraclecloud.com&password=mZQfPx6m&totp_code=123456' " \
            "http://vmatgz2ea009.oracleoutsourcing.com:5021/ccadminui/v1/mfalogin/ -o api.txt"
output = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
#jsonS = json.dumps(output.communicate())
#jsonS = output.communicate()[0]
#print jsonSi


def json_parse(filename):
        with open(filename, "r") as json_file:
                data = json.load(json_file)
                print data
                access_token_found=''
                if len(data['access_token']):
                        print('access token is present')

                print access_token_found




#check if file is present:
import os.path
from os import path
try:
        if os.path.isfile("api.txt"):
                #os.system("rm choices.txt")
                print 'yes'
                filename="api.txt"
                json_parse(filename)
except IOError:
        print 'not found'
		
		
---------------------------------------------------------------------------------------------------------------------------
#GET THE RESPONSE_CODE
#ADMIN URL
def get_response_code():
        '''
        user='occs-admin@oraclecloud.com'
        #pass='mZQfPx6m'
        #status_cmd= "curl -w '%{http_code}\\n' -H 'Accept:application/json' -H 'Content-Type:application/x-www-form-urlencoded' --data 'client_id=blah&client_secret=blah&grant_type=password&user_name=user&password=mZQfPx6m' http://vmatgz2ea009.oracleoutsourcing.com:5021/occ-admin/ -s -o /dev/null"

        status_cmd=subprocess.Popen(
        ["./test.sh"], stdout=subprocess.PIPE,
        stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        res_code = subprocess.Popen(status_cmd)
        res_out = res_code.communicate()
        print res_out
        '''
        #subprocess.call(['test.sh'])
        #shellscript = subprocess.Popen(['/tz2ea0c0/fmw/jyoti_workspace/test.sh' ] , stdin=subprocess.PIPE)
#get_response_code()

#admin_url='http://vmatgz2ea009.oracleoutsourcing.com:5021/occ-admin/'

arglist = 'ADMIN_USER ADMIN_PASSWORD'
bashCommand = "/bin/bash test.sh " + arglist
os.system(bashCommand)
