def binary_search(list, item):
    # low and high follow part of the list we are searching
    low = 0 
    high = len(list) - 1
    # While couldn't reach a single element...
    while low <= high:
        # ...checks the element in the middle
        mid = (low + high) // 2
        guess = list[mid]
        # Find the item
        if guess == item:
            return mid
        # Guess was too high
        if guess > item:
            high = mid - 1
            # Guess was too low
        else: 
            low = mid + 1
            # The item doesn't exist
    return None  

# Let's test it!
my_list = [1, 3, 5, 7, 9]

# Remember, lists starts at 0. The next element has index 1.
print (binary_search(my_list, 3)) # => 1

# "None" means null in Python. It indicates thatthe item wasn't found
print (binary_search(my_list, -1)) # => None