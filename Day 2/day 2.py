'''
for(i=0;i<n;i++){
    for(j=0j<n;j++){
        statements;   n*n----n square
        }
    };
    
Time complexity=O(n square)
'''

#Implement a 2D Array and rotate the matrix 90deg
'''
r=int(input("rows:"))
c=int(input("columns:"))
m1=[]
for i in range(r):
    a=[]
    for j in range(c):
        a.append(int(input()))
    m1.append(a)
    
print(m1)
'''

'''
for(i=1;i<n;i*2){
statements;
}
ANALYSIS
i=1		1 time
i=2		2 times (1*2)
i=3		4 		(1*2)*2=2 power 2
i=4		8 		(1*2)*2)*2=2 power 3
so when stops i>=n
                i=2 power k
                2 power k>=n
                k=log n base 2
so time complexity O(log n base 2)
'''

#create an array 1D it should contain between 10 to 30 extract and 1) print even numbers 2)2 power values


'''l=[]

def pows(n,b):
    if(n<=0 or b<=0):
        return 0
    while n%b==0:
        n=n/b
    return n==1
size=int(input("size: "))
print("Enter numbers: ")
for i in range(size):
    c=int(input())
    l.append(c)
print("Even numbers: ")
for i in range(size):
    if l[i]%2==0:
        print(l[i])

print("2 powers: ")
for i in range(size):
    b=2
    x=pows(l[i],b)
    if(x==1):
        print(l[i])'''

'''
Final Summary:
-------------

i++  i--  i+2      O(n)

i*2   i/2          log(n)    base 2

p=0
for p<n i++
p=p+i

O(sqrt(n))
'''

'''l=[]
def add(li,size):
    sum1=0
    for i in range(size):
        li.append(int(input()))
        sum1=sum1+li[i]
    return sum1
print("Sum=",add(l,size=int(input("size: "))))'''


'''def LSearch(l,key):
    c=0
    for i in range(len(l)):
        if(l[i]==key):
            print("Element found")
            break
    else:
        print("Element not found")
        
        
size=int(input("Size: "))
l=[]
for i in range(size):
    l.append(int(input()))
key=int(input("Enter key: "))
LSearch(l,key)'''

'''
It is parallel to time complexity concept

array of size n will take O(n) space

2d array will take O(n2) space
'''

'''
O(1)
constant space complexity:
Same amount of space regardless of the input size 'n' it is called constant complexity
Ex-1:
-->Sum of array elements and linear search
O(1) because space is not depending on values
'''

#quick sort O(log n)

'''polynomial complexity: O(n2)
space complexity grows proportionally to the square of the input size

ex:
def generate_lists_of_lists(n):
    table_list=[]
    for num in range(n):
        row=[]
        for i in range(n):
            row.append(i)
        table_list.append(row)
    return table_list
print(generate_lists_of_lists(10))'''

#sum of n numbers
#fibonacci series
#factorial

'''def sum1(n):
    if n<=0:
        return 0
    else:
        return n+sum1(n-1)
n=int(input())
print(sum1(n))'''

'''def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
        
    
    
n=int(input())
print(fact(n))'''

def fib(n):
    
    if n<0:
        print("Input is incorrect")
    elif n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

n=int(input())
for i in range(n):
    print(fib(i),end=" ")


    
