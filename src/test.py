a = [1, 5, 6, 7, 10]
b = [-10, -4, -2, -4, -2, 0]
c = [1, 5, 5, 8, 7]

def centered_avg(ints):
	# Sort the ints
	ints.sort()
	# Slice off the first and last value
	ints = ints[1:-1]
	# Ang out the remaining ints.
	avg = sum(ints) // len(ints)
	return avg

# print(centered_avg(a))

def centered_avg_optimised(ints):
	# find the maximum and minimum values
	small = min(ints)
	large = max(ints)
	# Remove the max and min
	ints.remove(small)
	ints.remove(large)
	# Find sum of new array // length of new array
	return sum(ints) // len(ints)

def centered_avg_optimised_2(ints):
	# largest = float("-inf")
	# smallest = float("inf")
	largest = ints[0]
	smallest = ints[0]
	total = 0
	# For integer in ints
	for i in ints:
		# If the integer is smaller than the min, set min to the int
		if i < smallest:
			smallest = i
		# If the integer is larger than max, set max to the int
		if i > largest:
			largest = i
		# Keep a running total of the sum
	total += i
	# Return the sum divided by the length - 2
	return (total - largest - smallest) // (len(ints) - 2)


# print(centered_avg_optimised_2(b))

a = 5

def mult_2(n):
	n *= 2
	return n

print(mult_2(a))
print(a)