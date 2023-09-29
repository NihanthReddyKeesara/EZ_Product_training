#BITWISE OPERATORS
'''
10*4/6+3-1%2
40/6+3-1%2
6.66+3-1
9.66-1
8.66'''

'''def DecimalToBinary(num):
    
    if num>=1:
        DecimalToBinary(num//2)
    print(num%2, end=' ')

if __name__=='__main__':
    num=int(input())
    DecimalToBinary(num)'''



'''n=int(input())
l=[]
if(n<0):
    m=-(n)
    while(m>0):
        rem=m%2
        l.append(rem)
        m=m//2
    nums=list(reversed(l))
    for i in range(len(nums)):
        if nums[i]==0:
            nums[i]=1
        elif nums[i]==1:
            nums[i]=0
    print(*nums)
else:
    while(n>0):
        rem=n%2
        l.append(rem)
        n=n//2
    num=list(reversed(l))
    print(*num)'''   #prints list as the number'''

#print(10|3&4)
#print(~12)
#print(7>>1)

#Even or odd
'''def isEvenOrOdd(num):
    if num & 1==0:
        return "even"
    else:
        return "odd"

print(isEvenOrOdd(num=int(input("Enter num: "))))'''

#binary to decimal
'''num=input()
l=len(num)'''

#print(9>>4)

'''import math as m

n=int(input())
p=m.pow(2,int(input()))
print(n*p)'''

'''
After  creating an array find out the smallest missing positive integer

I/p: [3,7,-5,-6,0,4]

O/p: 1
'''




'''size=list(map(int,input().split(" ")))


n=[]

for i in range(len(size)):
    if size[i]>=0:
        n.append(size[i])

n.sort()    
print(n)

m=[]
for i in range(0,max(n)):
    if i not in n:
        m.append(i)

print(min(m))'''


#In the given array every number occurs twice only one number occurs once find out the number

'''def findSingle(ar,n):
    res=ar[0]
    for i in range(1,n):
        res=res^ar[i]
    return res
ar=[2,3,5,4,5,3,4,2,88]
print(findSingle(ar,len(ar)))'''

#swap 2 numbers using XOR
'''a=100
b=200
print("a:",a,"b:",b)

a=a^b
b=a^b
a=a^b

print("a:",a,"b:",b)'''


#for the given number n check the kth bit is set or not    (set-->1)


'''l=list(map(int,input().split(" ")))
count=0
for i in range(len(l)):
    count=l.count(l[i])
    if count==1:
        print(l[i])
        break'''

'''n=7
xor=0
if n%4==0:
    print(n)
elif n%4==1:
    print(1)
elif n%4==2:
    print(n+1)
elif n%4==3:
    print(0)'''

#Given a range left-right print xor
'''lets say
4 to 9
xor(1 to 9)^xor(1 to 3)
(1^2^3^4^5^6^7^8^9)^(1^2^3)
in above 1 2 3 xors will get cancelled
generalise xor(r)^xor(l-1)'''

'''n=int(input("enter the term: "))
n1=0
n2=0
if(n<0):
    print("not possible")
else:
    for i in range(0,n-1):
        n3=n1+n2
        n1=n2
        n2=n3
    print(n2)'''


def TowerOfHanoi(n , source, destination, auxiliary):
    if n==1:
        print ("Move disk 1 from source",source,"to destination",destination)
        return
    TowerOfHanoi(n-1, source, auxiliary, destination)
    print ("Move disk",n,"from source",source,"to destination",destination)
    TowerOfHanoi(n-1, auxiliary, destination, source)
    

n = 4
TowerOfHanoi(n,'A','B','C')


    
    
    
    
    
        



