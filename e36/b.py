#!/usr/bin/python

n,pos,l,r = raw_input().split()
n,pos,l,r = int(n),int(pos),int(l),int(r)

if l == 1 and r == n:
	print 0
elif l == 1 and r != n:
	if pos >= r:
		print pos-r + 1
	else:
		print r-pos + 1
elif l != 1 and r == n:
	if pos <= l:
		print l-pos + 1
	else:
		print pos-l + 1
	
else:
	if pos <= l:
		print l-pos + 1 + r-l + 1
	elif pos >= r:
		print pos-r + 1 + r-l + 1
	else:
		if pos-l <= r-pos:
			print pos-l + 1 + r-l + 1
		else:
			print r-pos + 1 + r-l + 1