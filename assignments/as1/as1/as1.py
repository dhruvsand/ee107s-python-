def main():
    # Start your code below this commend
    


    while 1:
    	
    	x= input("Enter operation: ")
    	if(x!= 'q'):
    		y = input("Enter first number: ")
    		z = input("Enter second number: ")

			
    		if (y==''):
    			y='0'

    		if(z==''):
    			z='0'

			

    		if(x=='+'):
    			print(float(y)+float(z))
    		elif(x=='-'):	
    			print(float(y)-float(z))
    		elif(x=='/'):
    			print(float(y)/float(z))
    		elif(x=='*'):	
    			print(float(y)*float(z))
    		elif(x=='^'):	
    			print(float(y)**float(z))

    	
    	else:
    		break



    	

    # End your code above this line

if __name__ == '__main__':
    main()