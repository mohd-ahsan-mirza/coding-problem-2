from module import *
import datetime
import random
size = 1000
while size !=10000:
	data = random.sample(range(1, size*3), size) #Generate array of len 10000 between 1 and 30000 for sample
	print("----------------------")
	print("Sample size of " + str(size))
	print("----------------------")
	#print("Original List")
	#print("----------------------")
	#print(data)
	#print("----------------------")

	codingProblem = CodingProblem2(data)

	print("----------------------")
	start_time = datetime.datetime.now()
	result = codingProblem.computeUsingOptimalSolution()
	#print(*result)
	#print("----------------------")
	delta_optimal = datetime.datetime.now() - start_time
	print ("Optimal solution took "+ str( int(delta_optimal.total_seconds() * 1000) ) + "ms to run")
	print("----------------------")

	start_time = datetime.datetime.now()
	result = codingProblem.computeEasySolution()
	#print(*result)
	#print("----------------------")
	delta_easy = datetime.datetime.now() - start_time
	print ("Easy solution took "+ str( int(delta_easy.total_seconds() * 1000) ) + "ms to run")
	print("----------------------")
	if(delta_optimal > delta_easy):
		print("Optimal Solution took " + str(int((delta_optimal - delta_easy).total_seconds() * 1000)) + "ms more than the easy solution")
	else:
		print("Easy Solution took " + str(int((delta_easy - delta_optimal).total_seconds() * 1000)) + "ms more than the optimal solution")
	size = size + 1000


