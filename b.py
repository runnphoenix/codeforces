#!/usr/bin/python

n = int(raw_input())
A = [int(_) for _ in raw_input().split()]

su = 0
su_neg1 = 0
su_pos1 = 0
su_zer = 0

for i in range(n):
	if A[i] < -1:
		su += -1 - A[i]
		su_neg1 += 1
	elif A[i] == 0:
		su_zer += 1
	elif A[i] > 1:
		su += A[i] - 1
		su_pos1 += 1
	elif A[i] == -1:
		su_neg1 += 1
	else:
		su_pos1 += 1
		
su_neg1 %= 2
if su_neg1 ==1:
	if su_zer > 0:
		su += 1
		su += su_zer - 1
	else:
		su += 2
else:
	su += su_zer
	
print su
	
