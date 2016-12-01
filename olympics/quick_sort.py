# A typical recursive Python  implementation of QuickSort */
  
# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot
def partition(arr,low,high,index):
    i = ( low-1 )         # index of smaller element
    pivot = arr[high]     # pivot
  
    for j in range(low , high):
  
        # If current element is smaller than or
        # equal to pivot
        if   arr[j] >= pivot:
          
            # increment index of smaller element
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
            index[i],index[j]=index[j],index[i]
            
    arr[i+1],arr[high] = arr[high],arr[i+1]
    index[i+1],index[high]=index[high],index[i+1]
    return ( i+1 )
  
# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index
  
# Function to do Quick sort
def quickSort(arr,low,high,index):
    if low < high:
  
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr,low,high,index)
  
        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1,index)
        quickSort(arr, pi+1, high,index)


#arr=[3,1,2,2,13,9]
#index=[0,1,2,3,4,5]
#quickSort(arr,0,5,index)
#print(arr)
#print(index)
