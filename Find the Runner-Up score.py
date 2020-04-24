n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
m=arr[0]
for i in range(1,n):
    if(m>arr[i]):
        break
print(arr[i])
