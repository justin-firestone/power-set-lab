# This function generates all subsets of a given set S using the binary
# counting method and returns them in an array.

import time

def generate_all_subsets(set_S):
	subsets = {}
	#  TODO
	return subsets

# This function returns the interest-optimized list of companies you have time (in minutes)
# to chat with at the career fair.

def career_fair_planner(companies, availableTime):
	subsets = generate_all_subsets(companies)
	optimalSubset = {}
	#  TODO
	return optimalSubset

# This function accepts an integer i and returns the binary representation of i
# in an array of n bits (e.g. getBitArray(1, 5) would return [0, 0, 0, 0, 1])

def get_bit_array(i, n):
	base2 = bin(i)
	base2 = [char for char in base2]
	base2 = base2[2:]
	for i in range(len(base2)):
		base2[i] = int(base2[i])
	# pad the zeros
	for i in range(n - len(base2)):
		base2.insert(0, 0)
	return base2

def display_results(companies):
	print("The companies you should visit are: ")

	for i in range(len(companies)):
		print(f"Company {companies[i][0]} with an interest of {companies[i][1]} "
			  f"and estimated chat time of {companies[i][2]}")


# [0]: name, [1]: interest, [2]: estimated chat time
# A-U is 21 companies
companies = [
	["A", 7, 12],
	["B", 8, 9],
	["C", 8, 3],
	["D", 3, 3],
	["E", 5, 15],
	["F", 10, 25],
	["G", 4, 13],
	["H", 6, 4],
	["I", 7, 7,],
	["J", 1, 14],
	["K", 6, 15],
	["L", 6, 11],
	["M", 7, 4],
	["N", 4, 7],
	["O", 8, 20],
	["P", 10, 18],
	["Q", 3, 1],
	["R", 5, 5],
	["S", 9, 12],
	["T", 4, 16],
	["U", 8, 18]
]

start_time = time.time()
optimalSubset = career_fair_planner(companies, 120)
total_time = round(time.time() - start_time, 7)
display_results(optimalSubset)
print(f"Power set took {total_time} seconds")
