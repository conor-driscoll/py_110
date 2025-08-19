def calculate_leftover_blocks(available_blocks):

    current_blocks_used_count = 0

    for layer_count in range(available_blocks + 1):

        layer_block_count = layer_count**2
        current_blocks_used_count += layer_block_count

        if current_blocks_used_count == available_blocks:
            return 0

        if current_blocks_used_count > available_blocks:
            break

    return (available_blocks - (current_blocks_used_count - layer_block_count))


print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True