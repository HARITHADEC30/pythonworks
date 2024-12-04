arr =[-4, -2, 1, 4, 8]

closest_number = arr[0]
min_distance = abs(arr[0])

for i in arr:
    distance = abs(i)
    if  distance < min_distance:
        min_distance = distance
        closest_number = i
    elif distance == min_distance and i > closest_number: 
        closest_number = i

print(closest_number) 