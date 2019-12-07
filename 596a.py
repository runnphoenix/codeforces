#!/usr/bin/python

da, db = [int(_) for _ in raw_input().split()]

if da + 1 == db:
	print da*10+9, db*10
elif da == db:
	print da*100, da*100+1
elif da == 9 and db == 1:
	print da*10+9, db*100
else:
	print -1