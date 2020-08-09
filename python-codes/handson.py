import requests
url='https://database.uk-london-1.oraclecloud.com/20160918/dbSystems/ocid1.dbsystem.oc1.uk-london-1.abwgiljra4vhckksobn3lys6gvn6ehb3dj2rgcchdwysnphmmjakdwmmrmja'
oci="http://169.254.169.254/opc/v1/instance/"
jeninks_url = 'http://localhost:8080'
git_url = 'https://github.com/TripathyJyotismita/Automation'
headers = {'Content-Type': 'application/json'}
auth=('jyotismita.tripathy@oracle.com', 'M@y585739951m@y')

try:
    r =  requests.get(jeninks_url)
    r.status_code
    r.raise_for_status()
    print('statauscode:',r.status_code)
    print('r.raise_for_status()', r.raise_for_status())
    print('r.cookies', r.cookies)
except requests.exceptions.HTTPError as httperr:
    raise httperr
except requests.exceptions.Timeout as e:
    print('received err1')
    #raise e
except requests.exceptions.ConnectionError as connerr:
    print('received err2')
    #raise connerr
except requests.exceptions.RequestException as err:
    print('received err3')



#req =  requests.get(url, headers=headers, params=auth)
request = requests.get(jeninks_url)
#print(request.status_code)
#print(request.content)
#print(request.json)

git_res = requests.get(git_url)
#print(git_res.content)

import urllib3
res = urllib3.get_host(git_url)
#print('res',res)
x=urllib3.connection_from_url(git_url)
#print('x=',x)


#Write a program to reverse a number in Python?
n = 613
rev=0
while (n>0):
    dig=n%10
    print(dig)
    rev=rev*10+dig
    n=n//10
    print("The reverse of the number:", rev)

#Write a program to find the sum of the digits of a number in Python?
sum_dig =0
n=1263
while n>0:
    dig = n%10
    sum_dig =sum_dig+dig
    n=n//10
print(sum_dig)

#Write a Python Program to Check if a Number is a Palindrome or not?
n=212
tmp=n
rev=0
while n>0:
    dig=n%10
    rev=rev*10+dig
    n=n//10

if (tmp == rev):
    print('pallindrome')
else:
    print('not pallindrome')

#pallindrome string
str='aba1'
if str == str[::-1]:
    print('pallindrome')
else:
    print('not pallindrome')

#Write a Python Program to Count the Number of Digits in a Number?
n=123456
count=0
while n>0:
    dig = n%10
    n=n//10
    count +=1

print(count)

#Write a Python Program to Print Table of a Given Number?
n=2
print([n*x for x in range(1,11)])
res = lambda x: n*x , range(1,11)
print(res)

# Write a Python Program to Check if a Number is a Prime Number?
n=7
k=0
for i in range(2, n//2+1):
    if n%2 == 0:
        k=k+1
        if k<=0:
            print('prime')
        else:
            print('not prime')

#Write a Python Program to Find the Second Largest Number in a List?
x=7
lst = []
for n in range(1,x+1):
    lst.append(n)
print(lst)
print(sorted(lst)[-2])

#Write a Python Program to Swap the First and Last Value of a List?
x=7
lst = []
for n in range(1,x+1):
    lst.append(n)

tmp=lst[0]
lst[0]=lst[n-1]
lst[n-1]=tmp
print(lst)

#Write a Python Program to Count the Number of Vowels in a String?
str='aeiouaeiouuuaeeee'
dct={}

for i in str:
    if i in ('aeiou'):
        if i in dct:
            dct[i]+=1
        else:
            dct[i]=1
print(dct)

#######UNIT TESTIING
def fact(n):
    if n == 0:
        return 1
    return n * fact(n -1)
import unittest
'''
class Test_fact():
    def test_fact(self):
        res= fact(5)
        self.assertEqual(res, 120)

if __name__ == '__main__':
    unittest.main()
'''

#reverse the string
string = 'This is my string!'


rev = ''
for i,j in enumerate(string):
    rev=string[i]+rev
print(rev)


