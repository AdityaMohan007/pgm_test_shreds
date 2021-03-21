'''
Let's say the HR team of a company has goodies set of size N each with a different price tag for each goodie. Now the HR team has to distribute the goodies among the M employees in the company such that one employee receives one goodie. Find out the goodies the HR team can distribute so that the difference between the low price goodie and the high price goodie selected is minimum.
'''


d={}    #goods and their prices are stored in dictionary 'd'
d1={}
sum1=0

n=int(input('Enter number of goodies:'))

for i in range(n):
    k,v=input().split(':')
    d[k]=int(v)
    d1[int(v)]=k
    
lst=list(d.values())    #price of goods are stored in lst
lst.sort()       #price of goods are sorted in ascending order so it becomes easier to find price difference btw goods
                        
lst1=[]     

#finding the price difference of first 2 goods in lst and so on in iterative manner and stored in lst1
for i in range(n-1):
    lst1.append(lst[i+1]-lst[i])
    
m=int(input('Enter number of employees:'))

lst2=[]

#finding the sum of first 3 prices of goods in lst1 and so on in iterative manner and stored in lst2
for i in range(n-m+1):
    lst2.append(sum(lst1[i:i+(m-1)]))
    
small=lst2.index(min(lst2))

lst3=lst[small:small+m]     #prices of goods distributed to the employees

for i in range(m):
    print(d1[lst3[i]],':',lst3[i])

print('And the difference between the chosen goodie with highest price and the lowest price is' , lst3[-1]-lst3[0])
