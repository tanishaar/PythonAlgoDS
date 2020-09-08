# Returns index of x in arr if present, else -1
from typing import List

def binary_search (arr: List[int], left: int, right: int, x: int) -> int:
	if right >= left:
		mid = left + (right - left) // 2
 
		if arr[mid] == x: 
			return mid
		elif arr[mid] > x: 
			return binary_search(arr, left, mid-1, x)  
		else: 
			return binary_search(arr, mid + 1, right, x) 
	else:
		return -1

def main():
    arr = list()
    size = int(input("Enter the size of the input array : "))
    print("Enter the array elements :")

    for i in range(0, size):
        arr.append(int(input()))

    x = int(input("Enter the element to search : "))
    result = binary_search(arr, 0, len(arr)-1, x)

    if(result == -1):
        print("Element is not present in array")
    else:
        print("Element is present at index", result)

if __name__=="__main__":
    main()

""" Example :
Enter the size of the input array : 4
Enter the array elements :
21
12
45
55
Enter the element to search : 45
Element is present at index 2
"""