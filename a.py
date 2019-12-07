#!/usr/bin/python

n = int(raw_input())
A = [int(_) for _ in raw_input().split()]
m = int(raw_input())
B = [int(_) for _ in raw_input().split()]

A,B = sorted(A),sorted(B)

def foo(A, B):
	for i in range(len(A)):
		for j in range(len(B)):
			su = A[i] + B[j]
			if su not in A[i:] and su not in B[j:]:
				return A[i], B[j]

print foo(A, B)[0], foo(A, B)[1]