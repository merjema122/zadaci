def sum_num(n):
 sum=0
 x=0
 while x<n:
   cub=x*x*x
   x=x+1
   sum+=cub
 return sum

print(sum_num(14))