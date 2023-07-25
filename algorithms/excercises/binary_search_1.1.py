# Considring you have a list with 128 names and you are doing a binary search. 
# What would be the maximum number of steps you would take to find the desired name?

def binary_search(list, item):
    low = 0 
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else: 
            low = mid + 1
    return None  

my_array = [None for _ in range(128)]
my_array = [None] * 128

for i in range(len(my_array)):
    my_array[i] = i

my_list = my_array

print (binary_search(my_list, 54))