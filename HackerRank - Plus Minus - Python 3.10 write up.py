##    Given an array of integers, calculate the ratios of its elements that
##    are positive, negative, and zero. Print the decimal value of each
##    fraction on a new line with places after the decimal.

##    Print the ratios of positive, negative and zero values in the array.
##    Each value should be printed on a separate line with 6 digits after the
##    decimal. The function should not return a value.

##### ##### ##### #####

#   An iterative solution
#   O(n).  n is the length of integer_array.
#   Iterates through integer_array and keeps track of the
#   number of positive, negative and zero integers in a dictionary.
#   Calculates the ratios, then prints them with correct formatting.
#   Key Concepts:
#       Using a dictionary to reduce the number of passes through the array.
#       Using the format function to correctly format the output.

def solutionOne(integer_array):

    count_table = {'positive':0,
                   'negative':0,
                   'zero':0}

    for integer in integer_array:

        if integer > 0:
            count_table['positive'] += 1

        elif integer < 0:
            count_table['negative'] += 1

        else:
            count_table['zero'] += 1

    positive_ratio = count_table['positive'] / len(integer_array)
    negative_ratio = count_table['negative'] / len(integer_array)
    zero_ratio = count_table['zero'] / len(integer_array)

    print(format(positive_ratio, '.6f'))
    print(format(negative_ratio, '.6f'))
    print(format(zero_ratio, '.6f'))

##### ##### ##### ####

def test():

    border = '##### ##### ##### #####'

    test_array_one = [1,1,0,-1,-1]

    print()
    print(border)
    print()

    solutionOne(test_array_one)

    print()
    print(border)
    print()

    return None
