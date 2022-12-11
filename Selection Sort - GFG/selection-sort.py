#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here 
        for j in range(len(arr)):
            i = arr[j]
            for y in range(j,len(arr)):
                if i>arr[y]:
                    i=arr[y]
            index1 = arr.index(i)
            arr[index1], arr[j] = arr[j], arr[index1]
            return i
    
    def selectionSort(self, arr,n):
        #code here
        for j in range(n):
            i = arr[j]
            for y in range(j,n):
                if i>arr[y]:
                    i=arr[y]
            temp =arr[j]
            arr[j]=i
            for k in range(j+1,len(arr)):
                if i == arr[k]:
                    arr[k]=temp
                    break

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends