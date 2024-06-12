def calculate_statistics():
    data = [23, 45, 12, 67, 34, 89, 23, 45, 23, 34]
    total_sum = sum(data)
    count = len(data)
    average = total_sum / count
    
    data_sorted = sorted(data)
    if count % 2 == 0:
        median = (data_sorted[count // 2 - 1] + data_sorted[count // 2]) / 2
    else:
        median = data_sorted[count // 2]

    occurrences = {}
    for num in data:
        if num in occurrences:
            occurrences[num] += 1
        else:
            occurrences[num] = 1
    mode = max(occurrences, key=occurrences.get)

    print("Sum:", total_sum)
    print("Average:", average)
    print("Median:", median)
    print("Mode:", mode)

# Calculate statistics for the specific data set
calculate_statistics()
