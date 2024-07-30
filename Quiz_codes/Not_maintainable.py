import numpy

def process_list(data):
    return [2 *numpy.sqrt(x) + 3 for x in data if x * 1.5 < 5]

# Example usage
input_data = [1, 2, 3, 4, 5, 6]
result = process_list(input_data)
print("Processed list:", result)







