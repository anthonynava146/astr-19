#Adds two floats
def AddFloat(float1, float2):
	add = float1 + float2
	return add

#Subtract integers
def SubInts(int1, int2):
	diff = int1 - int2
	return diff
	#print("The difference between the two integers is: " + sum)

#Product function
def ProductOf(float, int):
	prod = float * int
	return prod
	#print("The product of the float and the integer is: " + prod)

def main():
	#Adding floats
	print("The sum of two floats 4.5 and 3.5 is: " + str(AddFloat(4.5, 3.5)) + " which is data type: " + str(type(AddFloat(4.5, 3.5))))

	#Subtracting ints
	print("The difference of integers 6 and 3 is: " + str(SubInts(6, 3)) + " which is data type: " + str(type(SubInts(6, 3))))

	#Product of float and int
	print("The product of the float 0.5 and the integer 10 is: " + str(ProductOf(0.5, 10)) + " which is data type: " + str(type(ProductOf(0.5, 10))))


if __name__ == '__main__':
	main()