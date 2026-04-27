* def bouncyCount(input_lst):
* if list is empty, return 0
* convert argument integer list to string list and name str_int
* if length of str_int < 3:
    * return 0
* initialize result_lst
* initialize up and down variables and set them both to False
* initialize previous_num and set to first num in input_lst
* iterate through each num in str_int
    * if previous_num > and down is True:
        * append num to result_lst
        * set up to True
    * elif num < previous_num and up is True:
        * append num to result_lst
        * set down to False
    * set up and down to False
    * previous_num = num
* return len(result_lst)
        
    
4, 2, 4