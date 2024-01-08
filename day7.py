def process_operations(input_string):
    # Define the operations as lambda functions
    operations = {
        '&': lambda b: '00' if b == '0' else '01',  # &0 -> 00 and &1 -> 01
        '|': lambda b: '11' if b == '1' else '01',  # |1 -> 11 and |0 -> 01
        '^': lambda b: '10' if b == '1' else '01',  # ^1 -> 10 and ^0 -> 01
        '!': lambda _: '10'                        # ! -> 10
    }

    output = ""
    i = 0
    while i < len(input_string):
        char = input_string[i]

        if char in operations:
            if char == '!':  # NOT operation doesn't have a following number
                output += operations[char](None)
            else:
                i += 1  # Move to the next character to get the bit
                output += operations[char](input_string[i])
        i += 1

    return output

# Example inputs and expected outputs
examples = {
    "&1^0^1^0^1&1|1|1|1|0&0&1&1&1!": "010110011001111111010001010110",
    "|1|1|1|1|1|1|1": "11111111111111",
    "&0&0&0&0&1&1&1&1": "0000000001010101",
    "^1^1^1^1^0^1^0^1^1^1^1^1": "101010100110011010101010",
    "^0!&1&1|0|0|1&1&0|0|1|0&0^0|0^1|0^0|1|1|1&0!|0|0^1|0&1|0|1|0!^1&0!|1&1|0&1!^0|0^0&0^1^0^1!&0|1^0!|1^0|1&1&1|1^0|1&0&1&1^1!^1|0&1&0&1^1!|1|0^0^1!|0^1|1" : "1"
}

# Validate the function with the example inputs
for input_string, expected_output in examples.items():
    result = process_operations(input_string)
    print(f"Input: {input_string}\nExpected: {expected_output}\nResult: {result}\nMatch: {result == expected_output}\n")
