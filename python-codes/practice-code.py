
N=3
a= '1 6 5'
print(a)
x= [int(i) for i in a.split()]
sorted_x=(sorted(x))
#print(sorted_x)

nm=[[[j, x.index(j)] for i,j in enumerate(x) if j !=sorted_x[i] ] ]
#print (nm)
old_v=nm[0][0]
print(old_v)
new_v=nm[0][1]
print(new_v)
ir=new_v[1] #6
vr=old_v[0] #2
print(vr)
print(ir)

aa=a.split(' ')
aa[ir]=vr
print(aa)

if len(nm)>0:


or:
N=5
A= ' '.join([str(i) for i in range(1,N+1)])
#print(A)

sum=0
A_n=[]
index_v=''
for x in A:
    try:
        sum=sum+int(x)
        #print(int(x))
        A_n.append(int(x) * N)

    except ValueError:
        pass

for y in A_n:
    if sum < y:
        index_v = A_n.index(y)
        break
#print(sum)
#print(A_n)
#print(index_v)
print(A.split(' ')[index_v])


'''
n=int(input("Enter number:"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")
	



# Give size of list
a=int(input('enter a nu:'))

aa = list(range(int(a)))
print (aa)
print("Palindrome numbers are:")
# check through the list to check 
# number is palindrome or not

binary=[]
p_li=[i for i in aa if ("".join(reversed(str(i)))==str(i)) ]
print (p_li)
for num in p_li:
	#decToBinary(num);
	binary_li=''.join(str([int(x) for x in bin(num)[2:]]))
	print(binary_li)
	binary.append(binary_li)

print(binary)
'''	
	
a = ' '.join([str(x) for x in a])
    print ('a af:',a)
    #a= [1,2,3,4,5]
    noofleftr= 2
    out = []
    n= len(a)
    for i,e in enumerate(a):
        #print(i)
        a[len(a)-1], a[0] = a[0], a[len(a)-1]
        #print (a)
        for j, ele in enumerate(a[1:-2]):
            print (j,ele)
            print (a)
            a[j], a[j+1]= a[j], a[j+1]
            print ('a in for', a)

	
	

		