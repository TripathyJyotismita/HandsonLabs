import cx_Oracle
def fun():
    CONN_INFO = {
        'host': 'localhost',
        'port': 1521,
        'user': 'system',
        'psw': '0racleDB',
        'service': 'orcl.oradev.oraclecorp.com'
    }
    con = cx_Oracle.connect('system/0racleDB@127.0.0.1:1521/orcl.oradev.oraclecorp.com')
    query = '''select * from dcsp_order where CNAME='ZCP' AND STATE='SUBMITTED';'''
	#con = cx_Oracle.connect('system/0racleDB@127.0.0.1:1521/orcl.oradev.oraclecorp.com')
	#conn = cx_Oracle.connect(con)
	cur = con.cursor()
	print(con.version)
	cur.execute('select count(*) from SYSTEM.dcsp_order')
	#cur.execute('select count(table_name) from ALL_TABLES')
	result=(cur.fetchall())
	cur.close()
	con.close()
	return result
	
print(fun())

#INSERT INTO SYSTEM.dcsp_order(ORDER_ID,STATE,CREATION_DATE,SUBMITTED_DATE) VALUES("o10075","INCOMPLETE", "19-DEC-18", "19-DEC-18")


def dbConnection():
    print("Calling DBCONNECTION")
    CONN_INFO = {
        'host': 'localhost',
        'port': 1521,
        'user': 'system',
        'psw': '0racleDB',
        'service': 'orcl.oradev.oraclecorp.com'
    }
    CONN_STR = '{user}/{psw}@{host}:{port}/{service}'.format(**CONN_INFO)
    #con = cx_Oracle.connect('system/0racleDB@localhost:1521/orcl.oradev.oraclecorp.com')
    c_name='ZCP'
    query = '''select * from %s.dcsp_order where CNAME='%s' AND STATE='SUBMITTED' ''' % ((CONN_INFO['user']), c_name)

    query1 = '''INSERT INTO dcsp_order(ORDER_ID, STATE,CREATION_DATE,SUBMITTED_DATE) 
    VALUES ('o10035', 'INCOMPLETE','04-04-19', '04-04-19' );'''
		

    try:
        conn = cx_Oracle.connect(CONN_STR)
        cur = conn.cursor()
        #cursor.execute('INSERT INTO dcsp_order (ORDER_ID,STATE,CREATION_DATE,SUBMITTED_DATE) VALUES (\''+str(o10075)+'\',\''+str(INCOMPLETE)+'\',\''+str(19-DEC-18)+'\',\''+str(null)+'\')')
        #cursor.execute('INSERT INTO dcsp_order (ORDER_ID,STATE,CREATION_DATE,SUBMITTED_DATE) VALUES ('+str(o10075)+','+str(INCOMPLETE)+','+str(19-DEC-18)+','+str(null)+')')
        ord=str('o10075')
        state=str('INCOMPLETE')
        cd=str('19-DEC-18')
        sd=str('19-DEC-18')
        import pdb
        #pdb.set_trace()
        #cur.execute('INSERT INTO SYSTEM.dcsp_order(ORDER_ID,STATE,CREATION_DATE,SUBMITTED_DATE) VALUES("o10075","INCOMPLETE", "19-DEC-18", "19-DEC-18")')
        #cur.execute("select count(*) from SYSTEM.dcsp_order")
        #cur.prepare('select count(*) from dcsp_order')
        cur.execute()
        result= cur.fetchall()

        print(result)
        print('DONEDONEDONE')
        cur.close()
    finally:
        conn.close()
#dbConnection()

import os,subprocess
query = '''
WHENEVER SQLERROR EXIT FAILURE
SET FEEDBACK OFF
SET HEAD OFF
SET EMB ON PAGES 0 NEWP
SET LINE 10000
SELECT * from dual;
EXIT;
'''
db_home=/orahome/Database/db12c
dbsession = subprocess.Popen(["/usr/bin/sudo","su","-","oracle","-c",""""""""+db_home+"""/bin/sqlplus -S / as sysdba"""""], stdin=subprocess.PIPE,stdout=subprocess.PIPE, stderr=subprocess.PIPE,env={"ORACLE_SID": "EMREP", "ORACLE_HOME": "+db_home+"})
dbsession.stdin.write(query)
query_result = dbsession.communicate()
print(query_result, dbsession.returncode)
