#Type checking means check which class does it belongs to.
a = 10
b = 15.5
c = "Ram"
d = [1,2,3,3,4,5,7,6,9]
e = (1,2,3,4,5,6,7)
f = {10,909,0,9,78,533}
g = {"name":"Kalyani"}
print(isinstance(a,int))



x = 'ram'
if isinstance(x,(int,float)):
    print("x is a number")
else:
    print("x is a string")