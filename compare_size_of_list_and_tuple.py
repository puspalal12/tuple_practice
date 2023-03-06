from sys import getsizeof
l=list(range(1,11))
print("List:",l)
t=tuple(range(1,11))
print("Tuple:",t)
print("List size:",getsizeof(l))
print("Tuple size:",getsizeof(t))
