sq=[val*val  for val in range(1,11)]
print(sq)

#even numbers from 1 to even
even=[num for num in range(1,11) if num%2==0]
print(even)

#lis=[1,2,-4,7,8-1,-3] when there is -ve no , override with 0
lis=[-1,2,-4,7,8,-1,-3]
lis=[val if val>0 else 0 for val in lis]
print(lis)