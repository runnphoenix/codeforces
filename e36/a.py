#!/usr/bin/python

n,k = raw_input().split()
n = int(n)
k = int(k)
a = list(raw_input().split())

max_a = 0
for i in range(n):
	if k % int(a[i]) == 0:
		if int(a[i]) > max_a:
			max_a = int(a[i])
print k / max_a