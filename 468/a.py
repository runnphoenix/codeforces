#!/usr/bin/python

def tiredness(moves):
	return moves * (moves+1) / 2

a = int(raw_input())
b = int(raw_input())

diff = abs(a - b)
if diff % 2 == 0:
	ma = diff / 2
	mb = diff / 2
else:
	ma = diff / 2 + 1
	mb = diff / 2

print tiredness(ma) + tiredness(mb)