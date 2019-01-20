class CodingProblem2:
	def __init__(self,list):
		self.list = list;
	def computeUsingOptimalSolution(self):
		suffix_products = [] # Generate list of products suffix of element i
		for num in reversed(self.list):
			if suffix_products:
				suffix_products.append(suffix_products[-1] * num) # Multiply each element by last index of array
			else:
				suffix_products.append(num) # Add first element in list
		suffix_products = list(reversed(suffix_products))
		
		# Same methodology as above, just reverse the list and reverse back the final computed list
		prefix_products = [] # Generate list of products prefix of element i
		for num in self.list:
			if prefix_products:
				prefix_products.append(prefix_products[-1] * num); # Multiply each element by last index of array
			else:
				prefix_products.append(num);
		
		result = [];
		for i in range(len(self.list)):
			if i == 0:
				result.append(suffix_products[i + 1]) # First element gets added
			elif i == len(self.list) - 1:
				result.append(prefix_products[i - 1]) # Last element gets added
			else:
				result.append(prefix_products[i - 1] * suffix_products[i + 1]) # Multiply at index of element i for products i+1 and i-1
		return result
	def computeEasySolution(self):
		multiply_forward = []
		product = 0
		for num in self.list:
			if multiply_forward:
				product = num * product # Multiply products forward
			else:
				product = num # First element
			multiply_forward.append(product) 
		#print(*multiply_forward)

		#Same methodology as above. Just reverse the list and reverse it back at the end
		product = 0
		multiply_backward = []
		for num in reversed(self.list):
			if multiply_backward:
				product = num * product # Multiply products backward
			else:
				product = num; # First element
			multiply_backward.append(product)
		multiply_backward = list(reversed(multiply_backward))
		#print(*multiply_backward)
		result = []
		for index in range(len(self.list)):
			result.append(int((multiply_forward[index] * multiply_backward[index])//(self.list[index] * self.list[index]))) # Multiply backward and forward elements at same index and divide by square of original element
		return result;


