#Linearly search x in array. If x is present then
#return its location, otherwise, return -1.

from typing import List

def search(arr: List[int], size: int, x: int) -> int:
    for i in range (0, size):
        if (arr[i] == x):
            return i;
    return -1;

def main():
    arr = list()
    size = int(input("Enter the size of the input array : "))
    print("Enter the array elements :")

    for i in range(0, size):
        arr.append(int(input()))

    x = int(input("Enter the element to search : "))
    result = search(arr, size, x)

    if(result == -1):
        print("Element is not present in array")
    else:
        print("Element is present at index", result)

if __name__=="__main__":
    main()

""" Example :
Enter the size of the input array : 4
Enter the array elements :
12
5
6
34
Enter the element to search : 6
Element is present at index 2
"""
