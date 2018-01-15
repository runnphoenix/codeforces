#!/usr/bin/python

a = raw_input()
b = raw_input()

if len(a) < len(b):
	x = ''.join(sorted(list(a), reverse=True))
	print int(x)
else:
	result = []
	
	a_digit_counts = [0,0,0,0,0,0,0,0,0,0]
	for i in range(len(a)):
		a_digit_counts[int(a[i])] += 1
		
	for i in range(len(b)):
		if a_digit_counts[int(b[i])] > 0:
			result.append(b[i])
			a_digit_counts[int(b[i])] -= 1
		else:
			# judge if lefted digits of a can be smaller than b's left digits
			remin = False
			for j in range(int(b[i])-1, -1, -1):
				if a_digit_counts[j] != 0:
					remin = True
					break
			# True
			if remin == True:
				# put a biggest under
				for j in range(int(b[i])-1, -1, -1):
					if a_digit_counts[j] != 0:
						result.append(str(j))
						a_digit_counts[j] -= 1
						break
				break
			# False, replace top with smaller one
			else:
				x = result.pop()
				a_digit_counts[int(x)] += 1
				for j in range(int(x)-1, -1, -1):
					if a_digit_counts[j] != 0:
						result.append(str(j))
						a_digit_counts[j] -= 1
						break
				break
	# put from max to min
	for j in range(9, -1, -1):
		if a_digit_counts[j] != 0:
			for jj in range(a_digit_counts[j]):
				result.append(str(j))
				a_digit_counts[j] -= 1
	
	result = ''.join(result)
	print int(result)