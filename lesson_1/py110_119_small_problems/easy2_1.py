# P:
# input: floating point number representing 0 <= angle(in degrees) <= 360
# output: string formatted as seen in the test cases
# implicit:
# explicit:

# E:
# Test cases provided below

# D:

# A:
# def dms(float_angle):
#     convert argument to string and assign this value to the new
#     float_angle_str variable

#     Initialize num_str with the value of empty string
#     Initialize dec_str with the value of empty string
#     Initialize dec_int with the value of empty string
#     Initialize before_dec_pt with the value of True
    
#     for each character in float_angle_string (starting from the beginning)
#         if the char is a digit and before_dec_pt is True:
#             add char to the num_str variable
#         if a non-digit is encountered: 
#             reassign before_dec_pt to False
#         else:
#             add char to the dec_str variable

#     if len(num_str) == 0:
#         num_str = '0'
    
#     if len(dec_str) == 0:
#         min_str = '00'
#     else:  
#         reassign dec_int variable the value of int(dec_str)

#         min_str = str((dec_int * 60) // 100)
#         if len(mins_str) == 0:
#             min_str = '00'
#         if len(min_str) == 1:
#             min_str = '0' + min_str

#     if len(dec_int) == 0:
#         sec_str = '00'
#     else:
#         min_remainder = (dec_int * 60) % 100
#         sec_str = str((min_remainder * 60) // 100)
#         if len(sec_str) == 0:
#             sec_str = '00'
#         if len(sec_str) == 1:
#             sec_str = '0' + sec_str

#     return an f-string comprising num_str + degree symbol + min_str +
#            "'" + sec_str + "\" + """

# C:

def dms(float_angle):
    float_angle_str = str(float_angle)

    num_str = ''
    dec_str = ''
    before_dec_pt = True
    
    for char in float_angle_str:
        if char.isdigit() and before_dec_pt:
            num_str += char
        elif not char.isdigit(): 
            before_dec_pt = False
        else:
            dec_str += char 

    if num_str == '':
        num_str = '0'
    
    if dec_str == '':
        min_str = '00'
        sec_str = '00'
    else:  
        if len(dec_str) == 1:
            dec_str += '0'
        
        if len(dec_str) > 2:
            dec_str = dec_str[:2] + '.' + dec_str[2:]
        
        dec_float = float(dec_str)
        
        min_str = str(int((dec_float * 60) // 100))

        if len(min_str) == 1:
            min_str = '0' + min_str

        min_remainder = (dec_float * 60) % 100

        sec_str = str(int((min_remainder * 60) // 100))
        
        if len(sec_str) == 1:
            sec_str = '0' + sec_str

    return f"{num_str}{chr(176)}{min_str}'{sec_str}\""


# All of these examples should print True
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"" or dms(254.6) == "254°36'00\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")
