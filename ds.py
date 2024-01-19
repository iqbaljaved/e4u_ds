


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
	#step 1
	#[0, 6, 3, 1, 2, 4]
	#[0, 6, 3, 1, 2, 4]
	#[0, 3, 6, 1, 2, 4]
	#[0, 3, 1, 2, 6, 4]
	#[0, 3, 1, 2, 4, 6]

	#step 2
	#[0, 3, 1, 2, 4, 6]
	#[0, 1, 3, 2, 4, 6]
	#[0, 1, 2, 3, 4, 6]
	#[0, 1, 2, 3, 4, 6]

	"""	
	if (arr[0] > arr[0+1]):
		temp     = arr[0] 
		arr[0]  = arr[0+1]
		arr[0+1] = temp
		#output -->[0, 6, 3, 1, 2, 4]

	if (arr[1] > arr[2]):
		temp     = arr[1] 
		arr[1]  = arr[2]
		arr[2] = temp
		#output -->[0, 3, 6, 1, 2, 4]

	if (arr[2] > arr[3]):
		temp   = arr[2] 
		arr[2] = arr[3]
		arr[3] = temp
		#output -->[0, 3, 1, 6, 2, 4]
	"""

	for i in range(0, len(arr)):
		#i = 3
		for j in range(0, len(arr)-1-i):
			#for j = 0, 0, 1  0, 1, 2, 3, 4, 5
			#for j = 1, 1, 2
			#for j = 2, 2, 3
			#for j = 3, 3, 4
			#for j = 4, 4, 5

			if (arr[j] > arr[j+1]):	
				temp     = arr[j] 
				arr[j]   = arr[j+1]
				arr[j+1] = temp
				#output -->[0, 6, 3, 1, 2, 4]
	return arr



#Entry Point Function
if __name__ == "__main__":
	
	#print("prime ", isPrime(100))
	print("C = ", convertTemp(100))

	#input array or list
	unSorted  = [0, 6, 3, 1, 2, 4]

	#expect output array or list
	#sortedArr = [0, 1, 2, 3, 4, 6]

	sortedArr = sortFunc(unSorted)

	print("sortedArr ", sortedArr)
	print("sortedArr ", unSorted)
	

	"""
	print ("len : ", len(unSorted))
	for i in range(0, len(unSorted)):
		print("for i : ", i)
		for j in range(0, len(unSorted)-1-i):
			print("    j : ", j, unSorted[j], unSorted[j+1])

	"""

'''
max=0
[12,23,4,78,34]
arr[max]>arr[1]
max=1
arr[max]>arr[2]
max=1
arr[1]>arr[3]
max=3
arr[max]>arr[4]
max=3

'''

def searchmax (arr):
    max=0
    for x in range (0, len (arr)-1):
        if arr[x+1] > arr[max]:
            max=x+1
    return max
#arr = list(input ("Enter your list"))
arr=[12,23,4,78,34]
result = searchmax(arr)
print (result )













