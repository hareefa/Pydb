#!/usr/bin/env python
# coding: utf-8

# In[1]:





# In[6]:


#given number is prime number or not
def isprime(n):
    flag=True
    for i in range(2,n//2+1):
        if n%i==0:
            flag=False
            return flag
    return flag
isprime(11)


# In[14]:


#function to find prime numbers from 1 to 10
def primecount(n):
    cnt=0
    for a in range (2,n+1):
        k=0
        for i in range (2,a//2+1):
            if a%i==0:
                k=k+1
        if(k<=0):
            cnt=cnt+1
    return cnt   
primecount(10)


# In[19]:


#individual factorial digit sum as original number
def factorial(n):
    fact=1
    for i in range(2,n+1):
        fact *=i
    return fact
def digitfactsum(n):
    sum=0
    buffer =n
    while n!=0:
        r=n%10
        sum +=factorial(r)
        n=n//10
    if sum==buffer:
        return "Yes"
    else:
        return "No"
    return
print(digitfactsum(145))
print(digitfactsum(123))
                    


# In[27]:


#function to return the count of palindrome number two limits
def ispalindrome(n):                                                                                     
    rev=0
    buffer= n
    while  n!=0:
        r=n%10
        rev=rev*10+r
        n=n//10
    if rev==buffer:
        return True
    else:
        return False
    return
def countpalindrome(lb,ub):
    cnt=0
    while lb!=ub:
        if ispalindrome(lb)==True:
            cnt=cnt+1
        lb=lb+1
    return cnt
print(countpalindrome(1,10))
print(countpalindrome(11, 100))
    
    


# In[2]:


#function to generate the perfect number of a given range
def factoriallist(n):
    sum=0
    for i in range(1,n//2+1):
        if n%i==0:
            sum=sum+i
    return sum
def isperfect(n):
    if factoriallist(n) ==n:
        return True
    return False
def generateperfect(lb,ub):
    for x in range(lb,ub+1):
        if isperfect(x):
            print(x,end =" ")
    print( )
    return
generateperfect(1,10)
generateperfect(1,10000)




# In[4]:


s1="python"
print(s1[0])
print(s1[1])
print(s1[2])
print(s1[5])
print(s1[len(s1)-1])


# In[38]:


s1="python"
print(s1[-1])
print(s1[-2])
print(s1[:2])
print(s1[-2:])
print(s1[-3:])
print(s1[2:])
print(s1[:-2])
print(s1[1:-1])
print(s1[len(s1)//2])
print(s1[-1:-3:-1])
print(s1[-1::-1])
print(s1[::2])
print(s1[::3])
print(s1[::-3])


# In[13]:


def reversestring(str):
    return str[-1::-1]
reversestring("programming")


# In[15]:


def isPalindrome(str):
    if str==str[::-
                1]:
        return True
    else:
        return False
    return
print(isPalindrome("python"))
print(isPalindrome("ganag"))


# In[16]:


#function to print a upper case characters
def printUpper(x):
    for i in range(len(x)):
        if ord(x[i])>=65 and ord(x[i])<=90:
            print(x[i],end=" ")
    return
printUpper("PyThon")
            


# In[20]:


#function to print "python" if the count of 
#upper and lower case is same
def findcount(str):
    cntUpper=0
    cntLower=0
    for x in range(len(str)):
        if ord(str[x])>=65 and ord(str[x])<=90:
            cntUpper=cntUpper+1
        elif ord(str[x])>=97 and ord(str[x])<=122:
            cntLower=cntLower+1
    if cntUpper==cntLower:
        return "samecount"
    else:
        return "programming"
    return
print(findcount("PyThon"))
print(findcount("PYThon"))


# In[22]:


#extract digits from given string
def extractdigits(str):
    for x in range(len(str)):
        if ord(str[x])>=48 and ord(str[x])<=57:
            print(str[x],end=" ")
    return
extractdigits("Appli1cat8ion89")


# In[25]:


#function to return the sum of digits in a string
def sumofdigits(str):
    sum=0
    for x in range(len(str)):
        if ord(str[x])>=48 and ord(str[x])<=57:
            sum=sum+(ord(str[x])-48)
    return sum
sumofdigits("Appli1cat8ion89")


# In[27]:


def sumofevendigits(str):
    sum=0
    for x in range(len(str)):
        if ord(str[x])>=48 and ord(str[x])<=57: 
            if(ord(str[x])-48) %2 ==0:
                 sum=sum+(ord(str[x])-48)
    return sum
sumofevendigits("Appli1cat8ion89")


# In[37]:


#function to print the specific word in upper case
def wordUpperCase(str):
    spaceCnt=0
    for x in range(len(str)):
        if ord(str[x]) ==32:
            spaceCnt+=1
        if spaceCnt==1:
            if ord(str[x])>=65 and ord(str[x])<=90:
                 print(str[x],end=" ")
            elif ord(str[x])>=97 and ord(str[x])<=122:
                print(chr(ord(str[x])-32),end=" ")
        if spaceCnt==2:
            break
    return
wordUpperCase("Python Made Easy")


# In[44]:


def wordUpperCase(s):
    l=s.split()
    print(l[1].upper())
wordUpperCase("Python Made Easy")


# In[ ]:





# In[ ]:




