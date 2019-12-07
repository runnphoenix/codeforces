#!/usr/bin/python

n = int(raw_input())
ns = [int(_) for _ in raw_input().split()]

ns = sorted(ns,reverse=True)

if len(ns) == 1:
	print ns[0]*ns[0]
else:
	half = 0
	if len(ns)%2 == 0:
		half = len(ns)/2
	else:
		half = len(ns)/2 + 1

	ns_b = ns[:half]
	ns_s = ns[half:]

	b = reduce(lambda a,b:a+b, ns_b)
	s = reduce(lambda a,b:a+b, ns_s)

	print b*b+s*s