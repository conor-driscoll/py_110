## P: Understand the problem
    - Input: 1 list of strings
    - Outputs: 1 sorted list of strings

    - Explicit:
        - Sort based on highest number of consecutive adjacent consonants
        - When adjacent consonant count is equal between two words, they should maintain their original position in the list in relation to each other
        - Consonants are still considered adjacent if they belong to two different words and are separated by a space

    - Implicit:
        - Strings may contain single or multiple words
        - Strings may be empty
        - Strings may have no adjacent consonants
        - Sort in descending order
        - Case is not relevant
        - Single consonants don't affect order

    - Questions:
        - When is 'y' a consonant?
        - Ascending or descending sort?       # Descending
        - Can strings contain a single word?  # Yes
        - Can strings be empty?
        - Is it possible to have no adjacent consonants in a string?                                            # Yes
        - How to handle cases in which multiple space characters are present between words?
        - Is case important?
    

## E: Examples and test cases
    my_list = ['aa', 'baa', 'ccaa', 'dddaa']
    print(sort_by_consonant_count(my_list))
    # ['dddaa', 'ccaa', 'aa', 'baa']

    my_list = ['can can', 'toucan', 'batman', 'salt pan']
    print(sort_by_consonant_count(my_list))
    # ['salt pan', 'can can', 'batman', 'toucan']

    my_list = ['bar', 'car', 'far', 'jar']
    print(sort_by_consonant_count(my_list))
    # ['bar', 'car', 'far', 'jar']

    my_list = ['day', 'week', 'month', 'year']
    print(sort_by_consonant_count(my_list))
    # ['month', 'day', 'week', 'year']

    my_list = ['xxxa', 'xxxx', 'xxxb']
    print(sort_by_consonant_count(my_list))
    # ['xxxx', 'xxxb', 'xxxa']


## D: Data structures
    - Using the input list, a sorted output list will need to be created
    - A list of consonants will also need to be created to check characters against


## A: Algorithms
    - Create a list of LOWERCASE_VOWELS
    - Create a copy of the input list to sort
    - Create and utilize a helper function to count the number of consecutive adjacent consonants in each string (count_adjacent_consonants)
        - remove spaces between words in string argument
        - initialize maximum_adjacent_consonants, current_adjacent_consonants, & previous_char_consonant variables
        - iterate through the string's characters to determine if each character is an adjacent consonant or not
            - if a character is a consonant, and there is a consonant before or after, increment the current_adjacent_consonants variable
            - if the current_adjacent_consonants value exceeds the maximum_adjacents_consonant value, set the latter equal to the former
            - at the end of each iteration through the loop, update the previous_char_consonant variable to True or False, and set current_adjacent_consonants equal to 0, if the current character is a vowel 
        - return value of maximum_adjacent_consonants
    - Use helper function as a key and reverse=True for the list.sort method
    - Return sorted list of strings