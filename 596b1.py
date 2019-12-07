#!/usr/bin/python

t = int(raw_input())

for _ in range(t):
	[n,k,d] = [int(_) for _ in raw_input().split()]
	an = [int(_)for _ in raw_input().split()]
	
	m = 10000
	for i in range(n-d+1):
		mi = len(set(an[i:i+d]))
		if mi < m:
			m = mi
	print m