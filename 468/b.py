#!/usr/bin/python
import math

n,a,b = raw_input().split()
n = int(n)
a = int(a)
b = int(b)

# sort a,b
if a > b:
	t = a
	a = b
	b = t
	
def spl(n1, n2, a, b):
	mid = (n1+n2) / 2
	
	if a <= mid and b > mid:
		return n2 - n1
	elif b <= mid:
		return spl(n1, mid, a, b)
	else:
		return spl(mid, n2, a, b)
		
ranges = spl(0,n,a,b)
if ranges == n:
	print 'Final!'
else:
	print int(math.log(ranges, 2))
