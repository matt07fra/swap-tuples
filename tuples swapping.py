a=(1,2,3)
b=(4,5,6)
print("before swapping:",a,b)
a=list(a)
b=list(b)
a,b=b,a
a=tuple(a)
b=tuple(b)
print("after swapping:",a,b)