#using cx_Oracle
import cx_Oracle
import pdb, csv
import datetime
def db_fun():
    result=[]
    port='3008'
    user='SYSTEM'
    psw='Hbk25sam' #'OQEUK3TBLO'
    #c_name='LECHATEAU' # 'India_Test'
    c_name=input('enter cname: ')    
	#csv_file=csv.reader(open('connection.csv', 'rb+', delimiter=',')
    reader = csv.reader(open('connection.csv', 'r'))
    for row in reader:
        #print(len(row))
        if c_name in row:
            if row[-1] is '':
               #print((row))
               serviceName=row[0] #PZ2EA0C0
               #sh=(service_name[1:5]).lower()
               #host="scan-"+sh+"-01.oracleoutsourcing.com"
               host="scan-"+(serviceName[1:5]).lower()+"-01.oracleoutsourcing.com"
               #'user': 'pz2ea0c0_STORE',
               user1=serviceName+"_STORE"
            #else:
            #    serviceName=row[0]
            #    schemaName=row[-1]
            #    host="scan-"+(serviceName[1:5]).lower()+"-01.oracleoutsourcing.com"
			#    get_pwd=subprocess.Popen(["/home/oracle/passwdmgr.sh", "-get", cn], stdout=subprocess.PIPE,stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            #    out=get_pwd.communicate()
			#	psw=((str(out[0]))[2:-2]).split('\\')[0]
			#	print(schemaName)		
    print(host)
    #print(user)
    #print(serviceName)
    result.append(host)
    #result.append(schemaName)
    result.append(serviceName)
    fn = 'order_report'+datetime.datetime.now().strftime("%Y-%m-%d")+'.csv'
    with open(fn, 'w', newline='') as f:
        headers = ['ORDER-ID', 'STATE', 'CREATED-DATE', 'SUBMITTED-DATE', 'CUSTOMER-NAME']
        writer = csv.writer(f,delimiter=',')
        writer.writerow("THIS IS HEADER:")
        writer.writerow(host)
        writer.writerow(headers)
        for row in result:
            writer.writerow(row)
		
        
        
db_fun()




"""
    dsn = cx_Oracle.makedsn(host,port,service_name=serviceName)
    print(dsn)
    conn = cx_Oracle.connect(user,psw,dsn)
    cur = conn.cursor()
    print(conn)
    print(conn.version)
    query=select * from user1.dcspp_order where STATE='SUBMITTED'
    cur.execute(query)
    result = (cur.fetchall())
    print(result)

db_fun()
s='PZ2EA0C0'
st=s[:5]
st
'PZ2EA'
st=(s[:5]).lower()
st
'pz2ea'
st=(s[1:5]).lower()
st
'z2ea'
h="scan-"+st+"-01.oracleoutsourcing.com"
print(h)

#using subprocess
from subprocess import Popen, PIPE
username='pz2ea0c0_STORE'
password = 'OQEUK3TBLO'
clientName='IndiaTest'
v_user_string=username + "/" + password + "@" +clientName
session = Popen(['echo','sqlplus','-S',v_user_string],stdin=PIPE, stdout=PIPE, stderr=PIPE)
print(session.returncode)


		CONN_INFO = {
        'host': 'localhost',
        'port': 1521,
        'user': 'system',
        'psw': '0racleDB',
        'service': 'orcl.oradev.oraclecorp.com'
    }
        host='scan-z2ea-01.oracleoutsourcing.com'
        port='3008'
        serviceName='PZ2EA0C0'
        dsn = cx_Oracle.makedsn(host,port,service_name=serviceName)
        conn = cx_Oracle.connect('pz2ea0c0_STORE', 'OQEUK3TBLO', dsn)
        print(conn.version)
        cur = conn.cursor()
        #query=select count(*) from dcspp_order
        cur.execute(query)
        result = (cur.fetchall())
        print(result)


>>> psw=subprocess.Popen(["/home/oracle/passwdmgr.sh", "-get", cn], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
>>> psw
<subprocess.Popen object at 0x7f59d8e2a668>
>>> out=psw.communicate()
>>> out
(b'RETpLCvp\n', None)
>>> psw=subprocess.Popen(["/home/oracle/passwdmgr.sh", "-get", cn], stdout=subprocess.PIPE,stderr=subprocess.PIPE, stdin=subprocess.PIPE)
>>> psw
<subprocess.Popen object at 0x7f59d8e2a390>
>>> out=psw.communicate()
>>> out
(b'RETpLCvp\n', b'')
>>> str(out[0])
"b'RETpLCvp\\n'"
>>> str(out[0]).strip()
"b'RETpLCvp\\n'"
>>> str(out[0]).strip(\\n)
  File "<stdin>", line 1
    str(out[0]).strip(\\n)
                         ^
SyntaxError: unexpected character after line continuation character
>>> str(out[0]).strip('\\n')
"b'RETpLCvp\\n'"
>>> len(str(out)

psw=((str(out[0]))[2:-2]).split('\\')
psw
['RETpLCvp', '']
psw[0]
'RETpLCvp'
psw=((str(out[0]))[2:-2]).split('\\')[0]
psw
'RETpLCvp'
"""