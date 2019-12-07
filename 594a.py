#!/usr/bin/python

import itertools

t = int(raw_input())
for t_o in range(t):
	n = int(raw_input())
	ns = [int(_) for _ in raw_input().split()]
	m = int(raw_input())
	ms = [int(_) for _ in raw_input().split()]

#	count = 0
#	for i in range(n):
#		for j in range(m):
#			inter_x = (ns[i]+ms[j]) / 2.0
#			if inter_x - round(inter_x) == 0:
#				count += 1
#	print count
	
#	inter_xs = [(a+b)*0.5 for a in ns for b in ms]
#	inter_xs_int = [x for x in inter_xs if x-round(x) == 0]
#	print len(inter_xs_int)
	
#	inter_xs = [(_[0]+_[1])*0.5 for _ in itertools.product(ns,ms)]
#	inter_xs_int = [x for x in inter_xs if x-round(x) == 0]
#	print len(inter_xs_int)
	
	ns_odd = [_ for _ in ns if _ % 2 != 0]
	len_ns_odd = len(ns_odd)
	len_ns_even = len(ns) - len_ns_odd
	
	ms_odd = [_ for _ in ms if _ % 2 != 0]
	len_ms_odd = len(ms_odd)
	len_ms_even = len(ms) - len_ms_odd
	
	print len_ns_odd * len_ms_odd + len_ns_even * len_ms_even