arr = [10, 11, 11, 13, 12, 140, 15, 12, 13, 13, 15, 15, 15, 15, 140, 140, 140, 140]

element_count = {}

for element in arr:
    if element in element_count:
    
     element_count[element] += 1
    else:
        element_count[element] = 1
for key, value in element_count.items():
    print(f'{key}: {value}')