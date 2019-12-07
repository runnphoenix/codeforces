#!/usr/bin/python

[n,p] = [int(_) for _ in raw_input().split()]

candidates = []
i = 0
while 2**i + p <= n:
	candidates.append(2**i + p)
	i += 1
	
candidates = sorted(candidates, reverse = True)
print candidates

remains = n
count = 0
while remains > 0:
	if candidates[-1] > remains:
		break
	for candi in candidates:
		if candi <= remains:
			remains -= candi
			count += 1
			print candi, remains
print remains
print count