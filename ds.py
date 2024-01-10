


#Count digits in a number e.i 1234
#number = number/10 
#counter++

def countDigits(number):
	counter = 0
	while number is not 0:
		number = int(number/10)  #123.4
		counter = counter+1
	return counter 

#Check number is a palindrome or not
#12321, PytyP, NitiN
#Lets take basic approach
#Steps 1. Reverse the digits of number 
#Steps 2. compare with Orig number
#

def checkPal(num):
	number = num
	revNumber = 0
	while number != 0:
		lastDigit = number%10
		revNumber = revNumber*10 + lastDigit  #43
		print("lastDigit : ", lastDigit, revNumber)
		number = int(number/10)  #123.4

	return revNumber == num

#Compute Factorial of a number
#5 --> 5*4*3*2*1 -->120
#n --> 1*2*3 .... *(n-1)*n
def fact(number):

	if number == 0:
		return 1
	res = 1
	for i in range(1, number+1):
		res = res*i
		print("fact : ", res)

	return res


def factRec(number):

	if number == 0:
		return 1
	
	print("fact call : ", number, number-1)
	return number*factRec(number-1)



#table of two 
def table(number=2, times=10):
	for itr in range(1, times+1):
		mul = number*itr
		print("table : ", number, itr, mul)








def isPrime(number):
	
	for i in range(2, number):
		if number%i == 0:	
			return False	
	return True



def convertTemp(F):
	c = (F - 32) * (5.0/9.0)
	return c




#sort an array
def sortFunc(arr):

	#Paper work and dry run
	#


#Entry Point Function
if __name__ == "__main__":

	#print("prime ", isPrime(100))
	print("C = ", convertTemp(100))

	#input array or list
	unSorted  = [0, 6, 3, 1, 2, 4]

	#expect output array or list
	sortedArr = [0, 1, 2, 3, 4, 6]

























