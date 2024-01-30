nums = []
n = int(input("Enter Total Number Of Element You Want To Store In List:"))
print("Enter Elements for the List: ")
for i in range(n):
  nums.append(int(input()))
  
print("Original List is: ")
for i in range(n):
    print(nums[i],end=" ")
  

for i in range(n-1):
    chk = 0
    small = nums[i]
    for j in range(i+1, n):
        if small > nums[j]:
            small = nums[j]
            chk = chk + 1
            index = j
    if chk != 0:
        temp = nums[i]
        nums[i] = small
        nums[index] = temp

print("\nSorted List is: ")
for i in range(n):
    print(nums[i],end=" ")