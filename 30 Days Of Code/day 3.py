N = int(input())
if N<=100 and N>=1:

 if N%2!=0  or N in (6,8,10,12,14,16,18,20):
  print("Weird")
 elif N%2==0 or N in (2,4):
  print("Not Weird")
 
