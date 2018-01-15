#!/usr/bin/python
	
def getMin(list):
	result = []
	for i in range(len(list)):
		if list[i] != 0:
			for j in range(list[i]):
				result.append(str(i))
				list[i] -= 0
	return ''.join(result)
	
a = raw_input()
b = raw_input()


result = []

a_digit_counts = [0,0,0,0,0,0,0,0,0,0]
for i in range(len(a)):
	a_digit_counts[int(a[i])] += 1
	
# from left to right 
for i in range(len(b)):
	for j in range(9, -1, -1):
		if a_digit_counts[j] != 0:
			a_digit_counts[j] -= 1
			if int(''.join(result) + str(j) + getMin(a_digit_counts)) <= int(b):
				result.append(str(j))
				break
			else:
				a_digit_counts[j] += 1
print int(''.join(result))