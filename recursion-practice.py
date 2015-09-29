# # find length of a list without using len()
# def lenlst(lst):
# 	#base case (fail statement)
# 	# if lst is false (meaning 0)
# 	if not lst:
# 		return 0
# 	#Go through lst and return count of how many items
# 	# keeps running second return statement until the function hits the base case
# 	# when it hits the base case, it stops the function
# 	# the function keeps running because it is being called 
# 	return 1 + lenlst(lst[1:])

# def count(number):
# 	n = 1
# 	while n <= number:
# 		print n
# 		n = n + 1
# count(9)

# # takes number input, print up to number input
# # no for loops; no while loops
# def recurse(number):
# 	if 1 == number:
# 		print number
# 	else:
# 		recurse(number - 1)
# 		print number
# recurse(3)

# # sum of 0 to n 
# def sumnums(n):
# 	if n == 0:
# 		return 0
# 	else:
# 		# return n + sumnums(n-1)
# 		m = sumnums(n - 1)
# 		total = n + m
# 		return total
# print sumnums(4)

# # multiply numbers 0 to n
# def mulnums(n):
# 	if n == 1:
# 		return 1
# 	else:
# 		return n * mulnums(n - 1)
# print mulnums(5)

# # range(5) -> [0,1,2,3,4]
# def rangenums(n):
# 	if n == 0:
# 		return []
# 	else:
# 		x = rangenums(n-1)
# 		x.append(n-1)
# 		return x
# print rangenums(4)

# def count(num):
# 	if num == 0:
# 		print num
# 	else:
# 		count(num-1)
# 		print num
# count(5)

# def sumlst(lst):
# 	if not lst:
# 		return 0
# 	else:
# 		listslice = lst[1:]
# 		num = lst[0]
# 		total = sumlst(listslice)
# 		return total + num
# print sumlst([5,2,1])

# def multiplynums(lst):
# 	if not lst:
# 		return 1
# 	else:
# 		new_list = lst[1:]
# 		num = lst[0]
# 		total = multiplynums(new_list)
# 		return total * num
# print multiplynums([1,5,3,2])

# def maxnum(lst):
# 	print "."
# 	if len(lst) == 1:
# 		return lst[0]
# 	else:
# 		new_list = lst[1:]
# 		num = lst[0]
# 		t = maxnum(new_list)
# 		if t > num:
# 			return t
# 		else:
# 			return num
# print maxnum([9,4,2,7,7,1])

# def uniquenum(lst):
# 	if len(lst) == 1:
# 		return []
# 	else:
# 		new_list = lst[1:]
# 		num = lst[0]
# 		results = uniquenum(new_list)
# 		if num in new_list:
# 			results.append(num)
# 			return results
# 		return results
# print uniquenum([1,2,2,2,4,5,3,9])

# def unique(lst):
# 	if not lst:
# 		return []
# 	else:
# 		new_list = lst[1:]
# 		num = lst[0]
# 		results = unique(new_list)
# 		if num not in results:
# 			results.append(num)
# 			return results
# 		return results
# print unique([1,5,2,8,1,2])
## output: [1,5,2,8]

# def minnum(lst):
# 	if not lst:
# 		return None
# 	elif len(lst) == 1:
# 		return lst[0]
# 	else:
# 		nlst = lst[1:]
# 		num = lst[0]
# 		t = minnum(nlst)
# 		if t < num:
# 			return t
# 		else:
# 			return num
# print minnum([5,-4,1,0,10])
# print minnum([])
# print minnum([2])
# print minnum([5,4,1,0,10])

# def fib(num):
# 	print "$",
# 	if num < 0:
# 		return None
# 	elif num == 0:
# 		return 0
# 	elif num == 1:
# 		return 1
# 	else:
# 		num1 = fib(num-2)
# 		num2 = fib(num-1)
# 		t = num1 + num2
# 		return t
# print fib(8)
# print fib(-1)
# print fib(1)
# print fib(0)
# print fib(5)
# print fib(1)
# print fib(2)
# print fib(4)
# print fib(8)

def fib(num):
	if num < 0:
		return None
	elif num == 0:
		return 0
	elif num == 1:
		return 1
	else:
		num1,num2 = 1,1
		for i in range(num-1):
			print "$",
			num1,num2 = num2, num1+num2
		return num1
print fib(1)
print fib(2)
print fib(4)
print fib(8)

def fib_seq(num):
	fib_list = [0,1]
	while len(fib_list) <= num:
		fib_list.append(fib_list[-2] + fib_list[-1])
	return fib_list

def fib_num(num):
	fib_list = [0,1]
	while len(fib_list) <= 0:
		fib_list = [fib_list[-1], fib_list[-2], fib_list[-1]]
		# fib_list.append(fib_list[-2] + fib_list[-1])
		# fib_list.pop(0)
	return fib_list[-1]


