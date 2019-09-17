import matplotlib.pyplot as plt
def main():
	# Start your code below this commend
	


	while 1:
		
		low = float(input("Enter Lower X Value: "))

		high = float(input("Enter Higher X Value: "))
		print()

		if(low>=high):
			print("Lower is higher than Higher")
			quit()
		
		resolution = float(input("Enter the resolution of X: "))	

		if(resolution<=0):
			print("Resolution is 0 or negative")
			quit()

		x_vals= [0]*int((high-low)/resolution)
		y_vals= [0]*int((high-low)/resolution)

		for i in range (len(x_vals)):
			x_vals[i]= low+ resolution*i


		coef=[]
		power=[]

		# print("Enter the coef and power and to end just enter q in any")
		# print()

		# y=''
		# z=''

		# while(y!= 'q')and(z!='q'):
		# 	y = input("Enter the Coeficient of the x term: ")
		# 	z = input("Enter the Power of x term: ")
		# 	print()

			
		# 	if (y!= 'q')and(z!='q'):
		# 		coef.append(float(y))
		# 		power.append(float(z))

		print("Also add coefficints in each term like 1x^2 and split terms by spaces")
		my_str = input("Enter a valid Expression with x as the variable and eqault to y: ")

		whiteSpaceRegex = "\\s"
		terms=[]
		terms = my_str.split(" ")

		sign =1;

		for term in terms:
			if(term.isdigit()):
				coef.append(float(term)*sign)
				power.append(0)
			elif(term =="+"):
				sign=1;
			elif(term=="-"):
				sign =-1;
			elif(term=="x"):
				coef.append(1*sign)
				power.append(1)		
			elif("x^" in term):
				numbers=[]
				numbers = term.split("x^")
				coef.append(float(numbers[0])*sign)
				power.append(float(numbers[1]))
			elif("x" in term):
				numbers=[]
				numbers = term.split("x")
				coef.append(float(numbers[0])*sign)
				power.append(1)	
			


							



		for j in range(len(coef)):
			for i in range (len(y_vals)):
				y_vals[i]=y_vals[i]+  	coef[j]*(x_vals[i]**power[j])

		plt.plot(x_vals, y_vals)
		plt.xlabel('x - axis')
		plt.ylabel('y - axis')
		plt.title('My first graphing calculator!')
		plt.show()
		print()





		

	# End your code above this line

if __name__ == '__main__':
	main()