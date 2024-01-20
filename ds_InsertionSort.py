


def swap(arr, startIndex, endIndex):
	temp            = arr[startIndex]
	arr[startIndex] = arr[endIndex]
	arr[endIndex]   = temp


def sorting(arr):
	print("Steps for sorting")
	#Pick the starting element of the unsorted array
	#Assume first element is always sorted
	#put selected element at its right place in sorted array. 
	#repeat the above two steps till array got sorted
	#[1, 100, 64, 65, 25]
	#[1] [100, 64, 65, 25] --> Is this correct ?? or not ??
	#[1, 100] [64, 65, 25]
	#[1, 64, 100] [65, 25]
	#[1, 64, 65, 100] [25]
	#[1, 25, 64, 65, 100]

	#itr 0
	key = arr[0]  #--> single element is always sorted
	print("Itr 0 of sorting : ", arr)

	#itr 1
	#[200, 100, 64, 65, 25]
	key = arr[1]
	if arr[1] < arr[0]: # 100 < 200 --> true
		swap(arr, 0, 1)
		print("swap done !!! ", arr[1], arr[0])
		
	print("Itr 1 of sorting : ", arr)
	
	#itr 2
	#[100, 200] [64, 65, 25]
	#[100, 64] [200, 65, 25]
	#[64, 100, 200] [65, 25]

	key = arr[2]     # point to 64  with 200
	if arr[2] < arr[1]:
		swap(arr, 2, 1)
	print("Itr 2 of sorting : ", arr)

	key = arr[2]     # point to 64  with 100
	if arr[1] < arr[0]:
		swap(arr, 1, 0)
	print("Itr 2 of sorting : ", arr)

	#Itr 3
	#[64, 100, 200] [65, 25]
	
	
	#[64, 65, 100] [200, 25]

	key = arr[3]     # point to 65 
	if arr[3] < arr[2]:
		swap(arr, 3, 2)
	print("Itr 3 of sorting : ", arr) #--> [64, 100, 65] [200, 25]

	key = arr[3]     # point to 65 
	if arr[2] < arr[1]:
		swap(arr, 2, 1)
	print("Itr 3 of sorting : ", arr) #--> [64, 65, 100] [200, 25]
	
	key = arr[3]     # point to 65 
	if arr[1] < arr[0]:
		swap(arr, 1, 0)
	print("Itr 3 of sorting : ", arr) #--> #[64, 65, 100, 200] [25]


	#Itr
	key = arr[4]     # point to 25
	if arr[4] < arr[3]:
		swap(arr, 4, 3)
	print("Itr 4 of sorting : ", arr) #--> #[64, 65, 100, 25] [200]

	key = arr[4]     # point to 25 
	if arr[3] < arr[2]:
		swap(arr, 3, 2)
	print("Itr 4 of sorting : ", arr) #--> #[64, 65, 25, 100] [200]
	
	key = arr[4]     # point to 25 
	if arr[2] < arr[1]:
		swap(arr, 2, 1)
	print("Itr 4 of sorting : ", arr) #--> #[64, 25, 65, 100, 200]

	key = arr[4]     # point to 25 
	if arr[1] < arr[0]:
		swap(arr, 1, 0)
	print("Itr 4 of sorting : ", arr) #--> #[25, 64, 65, 100, 200]

		
def sortingUsingSingleLoop(arr):
	print("Steps for sorting")
	#Pick the starting element of the unsorted array
	#Assume first element is always sorted
	#put selected element at its right place in sorted array. 
	#repeat the above two steps till array got sorted
	#[1, 100, 64, 65, 25]
	#[1] [100, 64, 65, 25] --> Is this correct ?? or not ??
	#[1, 100] [64, 65, 25]
	#[1, 64, 100] [65, 25]
	#[1, 64, 65, 100] [25]
	#[1, 25, 64, 65, 100]

	
	#itr 0
	key = arr[0]  #--> single element is always sorted
	
	print("Itr 0 of sorting : ", arr)
	
	#itr 1
	keyIndex = 1
	j = keyIndex
	while(j>0): 
		key = arr[j]
		if arr[j] < arr[j-1]: 
			swap(arr, j, j-1)
		j = j-1
		print("Itr 1 of sorting : ", arr)
	
	#itr 2
	key = arr[2]
	keyIndex = 2
	j = keyIndex
	while(j>0): 
		key = arr[j]
		if arr[j] < arr[j-1]: 
			swap(arr, j, j-1)
		j = j-1
		print("Itr 2 of sorting : ", arr)

	#Itr 3
	keyIndex = 3
	j = keyIndex
	while(j>0): 
		key = arr[j]
		if arr[j] < arr[j-1]: 
			swap(arr, j, j-1)
		j = j-1
		print("Itr 3 of sorting : ", arr)

	#Itr
	keyIndex = 4
	j = keyIndex
	while(j>0): 
		key = arr[j]
		if arr[j] < arr[j-1]: 
			swap(arr, j, j-1)
		j = j-1
		print("Itr 4 of sorting : ", arr)
		

def sortingUsingDoubleLoop(arr):
	for i in range(0, len(arr)):
		keyIndex = i
		j = keyIndex
		while(j>0):			
			if i == 0:
				break
			key = arr[j]
			if arr[j] < arr[j-1]: 
				swap(arr, j, j-1)
			j = j-1
	


#Entry Point Function
if __name__ == "__main__":
	arr = [200, 100, 64, 65, 25, 30, 393, 1, 2, 4, 91]	
	#sorting(arr)
	#sortingUsingSingleLoop(arr)
	sortingUsingDoubleLoop(arr)
	print("Sorted array : ", arr)


















