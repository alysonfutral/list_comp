
# MUST USE LIST COMPREHENSIONS TO IMPLEMENT FOLLOWING:

# all_even(lst) -- return a list of even numbers occurring in the list lst,
    # in the same order as they appear in lst

def all_even(lst):
    # list comp - [expresssion FOR control_var IN collection]
    # return even numbers (modulus)
    return [even_num for even_num in lst if even_num % 2 == 0]


# all_not_multiple(lst, n) -- return a list of the numbers in lst that
    # are not multiples of n, in the same order as they appear in lst

def all_not_multiple(lst, n):
    # https://stackoverflow.com/questions/60586263/write-a-function-that-takes-a-list-of-integers-but-only-returns-those-that-are
    # list comp - [expresssion FOR control_var IN collection]
    # return list of num that is not multiples of n (must remain in same order of list)
    return [not_mul for not_mul in lst if not_mul % n != 0]


# max_from_2_tuples(tuples) -- tuples is a list of 2-tuples.
    # Return a 2-tuple that contains the MAX of the first element of each tuple
#   # AND the MAX of the second element of each tuple.
    #  For example, max_from_2_tuples([(-1, 5), (13, 2)]) would return (13, 5).

def max_from_2_tuples(tuples):
    # https://stackoverflow.com/questions/66607775/getting-the-correct-max-value-from-a-list-of-tuples
    # use list comp, use max() function to return max
    # [expression FOR control_var IN collection]
    # first element finds first index of tuple and uses list comp to return max
    first_ele_max = max(tpl[0] for tpl in tuples)
    # second element finds second index of tuple and uses list comp to return max
    second_ele_max = max(tpl[1] for tpl in tuples)
    return (first_ele_max, second_ele_max)


# lower_case_words(sentence) -- return a list of words in sentence converted
    # to lower case.  Do not include any empty strings in your result.
    # Words are separated by one or more space characters.

def lower_case_words(sentence):
    # https://www.w3schools.com/python/ref_string_split.asp
    list_of_words = sentence.split()
    # https://www.geeksforgeeks.org/python-remove-empty-strings-from-list-of-strings/
    while("" in list_of_words):
        list_of_words.remove("")
    # use list comp
    # "automate the boring stuff with python" Al Sweigart [.lower()]
    return [value.lower() for value in list_of_words]


# baby_names(names, last_name) -- names is a non-empty list of distinct
        # strings, last_name is a string.
    # Return a list of "full names" containing
        # all possible pairs of distinct names in names, with last_name
        # appended (and a space between each part of the name).
    # For example [[[baby_names(["Fred", "James"], "Smith") would return ["Fred James Smith", "James Fred Smith"]]]

def baby_names(names, last_name):
    # https://www.geeksforgeeks.org/python-program-to-get-all-pairwise-combinations-from-a-list/
    # https://www.geeksforgeeks.org/python-all-possible-pairs-in-list/
    # https://www.tutorialspoint.com/python-unique-pairs-in-list
    # create a list to store name values
    result_list = []
    # use two loops to iterate through values
    # iterate though first_names indices
    for first_name in range(len(names)):
        # iterate though second_names indices
        for second_name in range(first_name + 1, len(names)):
            # append the last name to the first (distinct) names and use spaces " "
            result_list.append(names[first_name] + " " + names[second_name] + " " + last_name)
        return result_list


