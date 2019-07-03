a=input()
s=0
v=0
for i in a:
  if(i=='('):
    s=s+1
  if(i==')'):
    v=v+1
if(s==v):
  print("yes")
else:
  print("no")
