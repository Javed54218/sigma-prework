def maximum(array_of_numbers):
    """
    returns the maximum of an array without max()
    """
    max_number = array_of_numbers[0]
    for number in array_of_numbers:
        if number > max_number:
            max_number = number

    return max_number


def minimum(array_of_numbers):
    """
    returns the minimum of an array without min()
    """
    min_number = array_of_numbers[0]
    for number in array_of_numbers:
        if number < min_number:
            min_number = number

    return min_number


def max_min_array(array_of_numbers):
    """
    constructs an array of the max and min number
    """
    max_number = maximum(array_of_numbers)
    min_number = minimum(array_of_numbers)
    array = [min_number, max_number]

    return array


print(max_min_array([2, 4, 1, 0, 2, -1]))
print(max_min_array([20, 50, 12, 6, 14, 8]))
print(max_min_array([-100, 100]))
