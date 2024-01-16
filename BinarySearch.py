# the function takes a sorted array and an item, if the item is in the array, the function return its position

def binary_search(list, item):
    # The below code keeps track of which part of the list you will search, so we will search from 0 position to last
    low = 0
    high = len(list) -1

    while low <= high:  # The function enters a while loop that continues
                            # until the search range is narrowed down to a single element (when low becomes greater than high)
        mid = (low + high) // 2 # let's find the midpoint index to minimize the guesses, better performance
        guess = list[mid]  # retrieves the value at the midpoint indexes from the list

        if guess == item: # If the guess is equal to the item, the function returns the index (mid) where the item is found
            return mid

        if guess > item: # if midpoint value is higher than item, then we know that we can eliminate any number
                         # greater than the midpoint, and set the new high to be mid-1, now we're working on lower half
            high = mid - 1

        else: # if midpoint(guess) is lower than the item, then we know that we can eliminate any number less than
                #midpoint, and set the new low to be mid+1
             low = mid + 1

    return None

my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 7))
