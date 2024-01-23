n = int(input("Enter the number of processes: "))  
mat = [[0 for j in range(2)] for i in range(n)]  
print("Enter the Burst Time of the processes:")  

for i in range(n):   
  mat[i][1] = int(input(f"P{i + 1}: "))  
  mat[i][0] = i + 1 
  
for i in range(n):   
  ind = i  
  for j in range(i + 1, n):  
    if mat[j][1] < mat[ind][1]:  
      ind = j  
  a = mat[i][1]  
  mat[i][1] = mat[ind][1]  
  mat[ind][1] = a  
  a = mat[i][0]  
  mat[i][0] = mat[ind][0]  
  mat[ind][0] = a  
  
print("Process BurstTime")  
for i in range(n):  
  print(f"P{mat[i][0]} {mat[i][1]}") 