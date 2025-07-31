#Linear Search
def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1

arr=[21,23,89,90,44]
target=int(input("Enter the number to be searched: "))
print(linear_search(arr,target))

#Binary Search (Recursion Code)
def binary_search(arr,target,start,end):
    while start<=end:
        mid=(start+end)//2
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            return binary_search(arr,target,start,mid-1)
        else:
            return binary_search(arr,target,mid+1,end)
    return -1
arr = [2, 3, 4, 10, 40]
target = 10
result = binary_search(sorted(arr), target, 0, len(arr) - 1)
if result != -1:
    print(f"Binary Search: Element found at index {result}")
else:
    print("Binary Search: Element not found")


#Binary Search (Iterative Code)
def b_search(arr,target):
    st=0
    end=len(arr)-1
    while st<=end:
        mid=(st+end)//2
        if target < arr[mid]:
            end = mid-1
        elif target > arr[mid]:
            st=mid+1
        else:
            return mid
    return -1
arr = [2, 3, 4, 10, 40]
target = 10
print(b_search(arr,target))











