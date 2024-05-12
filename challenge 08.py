 
n = int(input())
arr = map(int, input().split())

arr1 = list(arr)
arr1.sort()
arr2 = list(set(arr1))
length = len(arr2)
print(arr2[length-2])
    
  