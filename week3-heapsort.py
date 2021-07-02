

"""



example - 
https://www.youtube.com/watch?v=2DmK_H7IdTo&ab_channel=MichaelSambol


"""


def bubbleDown(arr,p,heapSize):
	
	
	#child index is valid && heap condition is unsatisfied
	
		#swap child value with parent value
		
		
		#shift parent index down to child index
		
		
		#calc new child in swap with


def heapsort(arr):

	#heapify
	for i in range(len(arr)-1,-1,-1):
		bubbleDown(arr,i,len(arr))
	
	#turn max heap into sorted array
	for headEnd in range(len(arr)-1,0,-1):
		#swap the peak with end of heap
		swap(arr,0,heapEnd)
		
		#shrink the head size by 1
		heapSize = heapEnd
		
		#bubble down new peak
		bubbleDown(arr,0,heapSize)



if __name__ == "__main__":
	pass