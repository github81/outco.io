



def quicksort(nums):

	def subsort(left,right):
	
		#base case
		if left >= right:
			return
			
		pivot = right
		wall = left
		
		for i in range(left,right):
		
			if nums[i] < nums[pivot]:
				nums[i], nums[wall] = nums[wall], nums[i]
				wall+=1
				#increment i - automatic for loop
			
			# if nums[i] > nums[pivot]:
			#	increment i - automatic for loop
							
		#swap wall with pivot
		nums[wall], nums[pivot] = nums[pivot], nums[wall]
		
		#
		subsort(left,wall-1)
		subsort(wall+1,right)
		
		
	subsort(0,len(nums)-1)
	return nums
	
	
if __name__ == "__main__":

	#nums = [3,9,1,4,7]
	nums = [1,2,3,4,5,6,1]
	nums = quicksort(nums)
	
	for item in nums:
		print(item)