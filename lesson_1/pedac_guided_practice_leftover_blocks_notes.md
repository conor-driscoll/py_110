## P: Understand the problem
    - Input: Integer of available blocks
    - Output: Integer of blocks left over

    - Explicit:
        - Build tallest possible valid structure
        - Blocks are cubes
        - Structure built in layers
        - Top layer in single block
        - Upper layer block supported by 4 lower blocks
        - Lower blocks may support more than 1 upper block
        - No gaps

    - Implicit:
        - The first layer will be a 1x1 grid, the second layer will be a 2x2 grid, the third layer will be a 3x3 grid, etc.
        - Therefore, the blocks in a layer = 
        layer number (from top) * layer number (from top)


## E: Examples and Test Cases
    print(calculate_leftover_blocks(0) == 0)  # True (0 blocks)
    print(calculate_leftover_blocks(1) == 0)  # True
    print(calculate_leftover_blocks(2) == 1)  # True
    print(calculate_leftover_blocks(4) == 3)  # True
    print(calculate_leftover_blocks(5) == 0)  # True
    print(calculate_leftover_blocks(6) == 1)  # True
    print(calculate_leftover_blocks(14) == 0) # True
        - assumptions are proven valid by test cases


## D: Data Structures
    [
        1,
        4,
        9,
        16,
        ...
    ]


## Algorithms:
    
    - 1. Define calculate_leftover_blocks function w/ integer of argument available_blocks passed in as parameter available_blocks

    - 2. Initialize current_blocks_used variable and set to the integer 0 

    - 3. Loop for layer_number in range of 0 to (available_blocks + 1):
        - a. layer_block_number = layer_number**2
        - b. current_blocks_used += layer_block
        - c. if current_blocks_used == available_blocks:
            d. return 0
        - e. if current_blocks_used > available_blocks:
            f. break
    
    - 4. Return (available_blocks - ((layer_number - 1)**2))  