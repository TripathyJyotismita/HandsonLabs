input types:
Sample Input
	5 4
	1 2 3 4 5


fun()
firstline = ' '.join(nd)

main()
nd = input().split()
n = int(nd[0])
d = int(nd[1])
a = list(map(int, input().rstrip().split()))
========================================================================================
Sample Input:
5 3
1 2 100
2 5 100
3 4 100

fun:
	startIndex = ''
    endIndex = ''
    k = ''
    for row in a:
        q = ' '.join([str(elem) for elem in row])
        startIndex = q.split(" ")[0]
        endIndex = q.split(" ")[1]
        k = q.split(" ")[-1]
	
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')


============================================================================
Else:

Sample Input 0

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

 firstinput= (input()).split(" ")
    ins= [((input()).split(" ")) for i in range(int(N))]
    print (ins)

    command= firstinput[0]
    print (firstinput)
    print (command) 
    index = firstinput[1]
    print (index)
    number = firstinput[2]
    print (number)
    input = ' '.join([command, index, number] )
    print (input)
    print (type(input))
    