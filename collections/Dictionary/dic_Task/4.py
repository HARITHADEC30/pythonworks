# 4. Write a dictionary comprehension to create a dictionary where the keys are numbers from 1 to 10 
# and the values are the squares of those numbers.
arr=[1,2,3,4,5,6,7,8,9,10]
#dictionary compration    
results={num:num**2 for num in arr}

print(results)  
