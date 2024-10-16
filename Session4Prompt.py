class Cat():
	def __init__(self, armLength, legLength, numEyes, hasTail, isFurry):
		self.armLength = armLength
		self.legLength = legLength
		self.numEyes = numEyes
		self.hasTail = hasTail
		self.isFurry = isFurry

	def describe(self):
		print("Cat attributes:")
		print("Arm length: " + str(self.armLength) + " cm")
		print("Leg length: " + str(self.legLength) + " cm")
		print("Number of eyes: " + str(self.numEyes))

		if(self.hasTail):
			print("Has tail: Yes")
		else:
			print("Has tail: No")

		if(self.isFurry):
			print("Is furry: Yes")
		else:
			print("Is furry: No")


def main():
	my_Cat = Cat(25.0, 30.0, 2, True, True)
	my_Cat.describe()

if __name__ == '__main__':
	main()