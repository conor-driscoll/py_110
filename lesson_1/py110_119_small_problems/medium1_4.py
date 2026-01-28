# * P:
#     * input: string containing integers and stack-and-register programming
#              commands, separated by single spaces
#     * output: print appropriate integer or nothing, based on commands
#     * commands: use provided index to program commands
# * E: see below
# * D & A:
# * C:  
def minilang(int_command_str):
    int_or_command = int_command_str.split()

    stack = []
    register = 0

    for item in int_or_command:   
        try:
            register = int(item)
            continue
        except ValueError:
            pass

        if (item in {'ADD', 'SUB', 'MULT', 'DIV', 'REMAINDER', 'POP'}
                and not stack):
            return 'Error: Attempted value retrieval from empty stack'
        
        match item:
            case 'PUSH':
                stack.append(register)
            case 'PRINT':
                print(register)  
            case 'ADD':
                register += stack.pop()
            case 'SUB':
                register -= stack.pop()
            case 'MULT':
                register *= stack.pop()
            case 'DIV':
                register //= stack.pop()
            case 'REMAINDER':
                register %= stack.pop()
            case 'POP':
                register = stack.pop()
            case _:
                return f"Error: '{item}' is invalid token"

    return None
            


minilang('PRINT')
# 0

minilang('5 PUSH 3 MULT PRINT')
# 15

minilang('5 PRINT PUSH 3 PRINT ADD PRINT')
# 5
# 3
# 8

minilang('5 PUSH POP PRINT')
# 5

minilang('3 PUSH 4 PUSH 5 PUSH PRINT ADD PRINT POP PRINT ADD PRINT')
# 5
# 10
# 4
# 7

minilang('3 PUSH PUSH 7 DIV MULT PRINT')
# 6

minilang('4 PUSH PUSH 7 REMAINDER MULT PRINT')
# 12

minilang('-3 PUSH 5 SUB PRINT')
# 8

minilang('6 PUSH')
# (nothing is printed)