'''list1=[2,1,4,3]
list2=[3,4,5,6,3]
list1.append(5)
print(list1)
print(list1.index(2))
print(list1.pop(4))
list1.sort()
print(list1)
print(list2.count(3))
print(list1.copy())
list2.insert(1,10)
print(list2)
list1.reverse()
print(list1)
list2.remove(10)
print(list2)
list1.extend(list2)
print(list1)'''

t=("apple","Bananna","orange","apple")
print(t.count("apple"))
print(t.index("orange"))
'''s="Hello World!"
s1="hello"
print(s.upper())
print(s.lower())
print(s1.capitalize())
print(s1.title())
print(s.swapcase())
print(s.split(" "))
print(s.replace("Hello","!HEllo!"))
print(s.casefold())
print(s.isalnum())
print(s.isascii())
print(s.isdecimal())
print(s.endswith("w"))
print(s.startswith("O"))'''

'''marks=int(input())
if 100<marks>=90:
    print("A")
elif 89<marks>=70:
    print("b")
elif 69<marks>=60:
    print("c")
else:
    print("fail")'''

'''n=5
while n>0:
    n-=1
    if n==2:
        break
    print(n)
print("------------------------")
n=5
while n>0:
    n-=1
    if n==2:
        continue
    print(n)'''

'''s="hello world"
revstr=""
for i in s[::-1]:
    revstr+=i
print(revstr)'''

'''s=input()
reverse=""
for i in s[::-1]:
    reverse+=i
if s==reverse:
    print("It is Palindrome")
else:
    print("It is Not Palindrome")'''

'''n=int(input("enter the number"))
if n>1:
    for i in range(2,n):
        if(n%i)==0:
            print(n,"is not prime number")
            break
        else:
            print(n,"is prime number")
            break
'''

'''def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2
n1,n2=int(input()),int(input())
print("addition",add(n1,n2))
print("subtraction",sub(n1,n2))
print("Multiplication",mul(n1,n2))
print("division",div(n1,n2))'''

'''def person_info(name,age):
    return name,age
name=input()
age=int(input())
print(person_info(name,age))'''

'''n=int(input())
f0,f1=0,1
print(f0,f1,end=" ")
for i in range(2,n):
    f2=f0+f1
    f0=f1
    f1=f2
    print(f2,end=" ")'''

'''n=int(input())
if n%2!=0:
    print("Odd Number")
else:
    print("Even Number")'''

'''n=1
while n<=100:
    if n%2!=0:
        print(n, end=" ")
    else:
        print('#',end=" ")
    n+=1'''

'''n=[2,4,6,8,100,44,55]
for i in n:
    print(i*i)'''

'''dict={"age":23,"name":"Yashwanth","marks":30}
for i in dict.keys():
    print(i,":",dict.get(i))'''

'''def is_prime(n):
    if n<2:
        return "Not prime"
    for i in range(2,n):
        if n%i==0:
            return "Not Prime"
    return "Prime"
def check_prime(l,h):
    for i in range(l,h+1):
        if is_prime(i)=="Prime":
            print(i, end=" ")
check_prime(1,100)'''