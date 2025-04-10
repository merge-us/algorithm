import math

n = int(input())
nums = [int(input()) for _ in range(n)]

count = 0
least_dist = nums[n-1]
for i in range(1,n):
    dist = nums[i]-nums[i-1]
    if math.gcd(dist,least_dist)==1:
        least_dist = min(dist,least_dist)
    else:
        least_dist = math.gcd(dist,least_dist)

for i in range(nums[0],nums[n-1],least_dist):
    if i not in nums :
        count+=1
    else :
        continue
print(count)