#!/usr/bin/python

n = int(raw_input())
states = list(int(_)for _ in raw_input())
ab = []
for _ in range(n):
	ab.append([int(_) for _ in raw_input().split()])
	
results = 0
	
it = 1
for i in range(n):
	it *= ab[i][0]
	
for i in range(10000):
	for j in range(n):
		if i >= ab[j][1] and (i - ab[j][1]) % ab[j][0] == 0:
			if states[j] == 0:
				states[j] = 1
			else:
				states[j] = 0
	
	counts = 0
	for k in range(n):
		if states[k] == 1:
			counts += 1
			
	if counts > results:
		results = counts
		
print results